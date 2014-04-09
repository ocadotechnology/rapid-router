# flake8: noqa
import io
import os
import sys
from fnmatch import fnmatch
from optparse import make_option
from copy import copy

from django.core.management.base import NoArgsCommand, CommandError
from django.template import (Context, Template,
                             TemplateDoesNotExist, TemplateSyntaxError)
from django.utils import six
from django.utils.datastructures import SortedDict
from django.utils.importlib import import_module
from django.template.base import Node, VariableNode, TextNode, NodeList
from django.template.defaulttags import IfNode
from django.template.loader import get_template  # noqa Leave this in to preload template locations
from django.template.loader_tags import (ExtendsNode, BlockNode, BlockContext)

try:
    from django.template.loaders.cached import Loader as CachedLoader
except ImportError:
    CachedLoader = None  # noqa

from compressor.cache import get_offline_hexdigest, write_offline_manifest
from compressor.conf import settings
from compressor.exceptions import OfflineGenerationError
from compressor.templatetags.compress import CompressorNode

if six.PY3:
    # there is an 'io' module in python 2.6+, but io.StringIO does not
    # accept regular strings, just unicode objects
    from io import StringIO
else:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO


def handle_extendsnode(extendsnode, block_context=None):
    """Create a copy of Node tree of a derived template replacing
    all blocks tags with the nodes of appropriate blocks.
    Also handles {{ block.super }} tags.
    """
    if block_context is None:
        block_context = BlockContext()
    blocks = dict((n.name, n) for n in
                  extendsnode.nodelist.get_nodes_by_type(BlockNode))
    block_context.add_blocks(blocks)

    context = Context(settings.COMPRESS_OFFLINE_CONTEXT)
    compiled_parent = extendsnode.get_parent(context)
    parent_nodelist = compiled_parent.nodelist
    # If the parent template has an ExtendsNode it is not the root.
    for node in parent_nodelist:
        # The ExtendsNode has to be the first non-text node.
        if not isinstance(node, TextNode):
            if isinstance(node, ExtendsNode):
                return handle_extendsnode(node, block_context)
            break
    # Add blocks of the root template to block context.
    blocks = dict((n.name, n) for n in
                  parent_nodelist.get_nodes_by_type(BlockNode))
    block_context.add_blocks(blocks)

    block_stack = []
    new_nodelist = remove_block_nodes(parent_nodelist, block_stack, block_context)
    return new_nodelist


def remove_block_nodes(nodelist, block_stack, block_context):
    new_nodelist = NodeList()
    for node in nodelist:
        if isinstance(node, VariableNode):
            var_name = node.filter_expression.token.strip()
            if var_name == 'block.super':
                if not block_stack:
                    continue
                node = block_context.get_block(block_stack[-1].name)
        if isinstance(node, BlockNode):
            expanded_block = expand_blocknode(node, block_stack, block_context)
            new_nodelist.extend(expanded_block)
        else:
            # IfNode has nodelist as a @property so we can not modify it
            if isinstance(node, IfNode):
                node = copy(node)
                for i, (condition, sub_nodelist) in enumerate(node.conditions_nodelists):
                    sub_nodelist = remove_block_nodes(sub_nodelist, block_stack, block_context)
                    node.conditions_nodelists[i] = (condition, sub_nodelist)
            else:
                for attr in node.child_nodelists:
                    sub_nodelist = getattr(node, attr, None)
                    if sub_nodelist:
                        sub_nodelist = remove_block_nodes(sub_nodelist, block_stack, block_context)
                        node = copy(node)
                        setattr(node, attr, sub_nodelist)
            new_nodelist.append(node)
    return new_nodelist


def expand_blocknode(node, block_stack, block_context):
    popped_block = block = block_context.pop(node.name)
    if block is None:
        block = node
    block_stack.append(block)
    expanded_nodelist = remove_block_nodes(block.nodelist, block_stack, block_context)
    block_stack.pop()
    if popped_block is not None:
        block_context.push(node.name, popped_block)
    return expanded_nodelist


class Command(NoArgsCommand):
    help = "Compress content outside of the request/response cycle"
    option_list = NoArgsCommand.option_list + (
        make_option('--extension', '-e', action='append', dest='extensions',
            help='The file extension(s) to examine (default: ".html", '
                'separate multiple extensions with commas, or use -e '
                'multiple times)'),
        make_option('-f', '--force', default=False, action='store_true',
            help="Force the generation of compressed content even if the "
                "COMPRESS_ENABLED setting is not True.", dest='force'),
        make_option('--follow-links', default=False, action='store_true',
            help="Follow symlinks when traversing the COMPRESS_ROOT "
                "(which defaults to STATIC_ROOT). Be aware that using this "
                "can lead to infinite recursion if a link points to a parent "
                "directory of itself.", dest='follow_links'),
    )

    requires_model_validation = False

    def get_loaders(self):
        from django.template.loader import template_source_loaders
        if template_source_loaders is None:
            try:
                from django.template.loader import (
                    find_template as finder_func)
            except ImportError:
                from django.template.loader import (
                    find_template_source as finder_func)  # noqa
            try:
                # Force django to calculate template_source_loaders from
                # TEMPLATE_LOADERS settings, by asking to find a dummy template
                source, name = finder_func('test')
            except TemplateDoesNotExist:
                pass
            # Reload template_source_loaders now that it has been calculated ;
            # it should contain the list of valid, instanciated template loaders
            # to use.
            from django.template.loader import template_source_loaders
        loaders = []
        # If template loader is CachedTemplateLoader, return the loaders
        # that it wraps around. So if we have
        # TEMPLATE_LOADERS = (
        #    ('django.template.loaders.cached.Loader', (
        #        'django.template.loaders.filesystem.Loader',
        #        'django.template.loaders.app_directories.Loader',
        #    )),
        # )
        # The loaders will return django.template.loaders.filesystem.Loader
        # and django.template.loaders.app_directories.Loader
        for loader in template_source_loaders:
            if CachedLoader is not None and isinstance(loader, CachedLoader):
                loaders.extend(loader.loaders)
            else:
                loaders.append(loader)
        return loaders

    def compress(self, log=None, **options):
        """
        Searches templates containing 'compress' nodes and compresses them
        "offline" -- outside of the request/response cycle.

        The result is cached with a cache-key derived from the content of the
        compress nodes (not the content of the possibly linked files!).
        """
        extensions = options.get('extensions')
        extensions = self.handle_extensions(extensions or ['html'])
        verbosity = int(options.get("verbosity", 0))
        if not log:
            log = StringIO()
        if not settings.TEMPLATE_LOADERS:
            raise OfflineGenerationError("No template loaders defined. You "
                                         "must set TEMPLATE_LOADERS in your "
                                         "settings.")
        paths = set()
        for loader in self.get_loaders():
            try:
                module = import_module(loader.__module__)
                get_template_sources = getattr(module,
                    'get_template_sources', None)
                if get_template_sources is None:
                    get_template_sources = loader.get_template_sources
                paths.update(list(get_template_sources('')))
            except (ImportError, AttributeError):
                # Yeah, this didn't work out so well, let's move on
                pass
        if not paths:
            raise OfflineGenerationError("No template paths found. None of "
                                         "the configured template loaders "
                                         "provided template paths. See "
                                         "http://django.me/template-loaders "
                                         "for more information on template "
                                         "loaders.")
        if verbosity > 1:
            log.write("Considering paths:\n\t" + "\n\t".join(paths) + "\n")
        templates = set()
        for path in paths:
            for root, dirs, files in os.walk(path,
                    followlinks=options.get('followlinks', False)):
                templates.update(os.path.join(root, name)
                    for name in files if not name.startswith('.') and
                        any(fnmatch(name, "*%s" % glob) for glob in extensions))
        if not templates:
            raise OfflineGenerationError("No templates found. Make sure your "
                                         "TEMPLATE_LOADERS and TEMPLATE_DIRS "
                                         "settings are correct.")
        if verbosity > 1:
            log.write("Found templates:\n\t" + "\n\t".join(templates) + "\n")

        compressor_nodes = SortedDict()
        for template_name in templates:
            try:
                with io.open(template_name, mode='rb') as file:
                    template = Template(file.read().decode(settings.FILE_CHARSET))
            except IOError:  # unreadable file -> ignore
                if verbosity > 0:
                    log.write("Unreadable template at: %s\n" % template_name)
                continue
            except TemplateSyntaxError as e:  # broken template -> ignore
                if verbosity > 0:
                    log.write("Invalid template %s: %s\n" % (template_name, e))
                continue
            except TemplateDoesNotExist:  # non existent template -> ignore
                if verbosity > 0:
                    log.write("Non-existent template at: %s\n" % template_name)
                continue
            except UnicodeDecodeError:
                if verbosity > 0:
                    log.write("UnicodeDecodeError while trying to read "
                              "template %s\n" % template_name)
            try:
                nodes = list(self.walk_nodes(template))
            except (TemplateDoesNotExist, TemplateSyntaxError) as e:
                # Could be an error in some base template
                if verbosity > 0:
                    log.write("Error parsing template %s: %s\n" % (template_name, e))
                continue
            if nodes:
                template.template_name = template_name
                compressor_nodes.setdefault(template, []).extend(nodes)

        if not compressor_nodes:
            raise OfflineGenerationError(
                "No 'compress' template tags found in templates."
                "Try running compress command with --follow-links and/or"
                "--extension=EXTENSIONS")

        if verbosity > 0:
            log.write("Found 'compress' tags in:\n\t" +
                      "\n\t".join((t.template_name
                                   for t in compressor_nodes.keys())) + "\n")

        log.write("Compressing... ")
        count = 0
        results = []
        offline_manifest = SortedDict()
        for template, nodes in compressor_nodes.items():
            context = Context(settings.COMPRESS_OFFLINE_CONTEXT)
            for node in nodes:
                context.push()
                key = get_offline_hexdigest(node.nodelist.render(context))
                try:
                    result = node.render(context, forced=True)
                except Exception as e:
                    raise CommandError("An error occured during rendering %s: "
                                       "%s" % (template.template_name, e))
                offline_manifest[key] = result
                context.pop()
                results.append(result)
                count += 1

        write_offline_manifest(offline_manifest)

        log.write("done\nCompressed %d block(s) from %d template(s).\n" %
                  (count, len(compressor_nodes)))
        return count, results

    def get_nodelist(self, node):
        if isinstance(node, ExtendsNode):
            return handle_extendsnode(node)
        # Check if node is an ```if``` switch with true and false branches
        nodelist = []
        if isinstance(node, Node):
            for attr in node.child_nodelists:
                nodelist += getattr(node, attr, [])
        else:
            nodelist = getattr(node, 'nodelist', [])
        return nodelist

    def walk_nodes(self, node):
        for node in self.get_nodelist(node):
            if isinstance(node, CompressorNode) and node.is_offline_compression_enabled(forced=True):
                yield node
            else:
                for node in self.walk_nodes(node):
                    yield node

    def handle_extensions(self, extensions=('html',)):
        """
        organizes multiple extensions that are separated with commas or
        passed by using --extension/-e multiple times.

        for example: running 'django-admin compress -e js,txt -e xhtml -a'
        would result in a extension list: ['.js', '.txt', '.xhtml']

        >>> handle_extensions(['.html', 'html,js,py,py,py,.py', 'py,.py'])
        ['.html', '.js']
        >>> handle_extensions(['.html, txt,.tpl'])
        ['.html', '.tpl', '.txt']
        """
        ext_list = []
        for ext in extensions:
            ext_list.extend(ext.replace(' ', '').split(','))
        for i, ext in enumerate(ext_list):
            if not ext.startswith('.'):
                ext_list[i] = '.%s' % ext_list[i]
        return set(ext_list)

    def handle_noargs(self, **options):
        if not settings.COMPRESS_ENABLED and not options.get("force"):
            raise CommandError(
                "Compressor is disabled. Set the COMPRESS_ENABLED "
                "setting or use --force to override.")
        if not settings.COMPRESS_OFFLINE:
            if not options.get("force"):
                raise CommandError(
                    "Offline compression is disabled. Set "
                    "COMPRESS_OFFLINE or use the --force to override.")
        self.compress(sys.stdout, **options)
