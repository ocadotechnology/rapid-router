from __future__ import division
from django import template
from django.template.loader import get_template
from django.template.base import token_kwargs, FilterExpression
from django.template.loader_tags import do_extends, ExtendsNode
from django.template.defaultfilters import slugify
from django.contrib.messages import constants
from ast import literal_eval

# pylint: disable=C0103

register = template.Library()

NoneFilterExpression = FilterExpression("None", None)
FalseFilterExpression = FilterExpression("False", None)
TrueFilterExpression = FilterExpression("True", None)

MESSAGE_LEVELS = {
    constants.ERROR: 'alert',
}

@register.filter
def message_class(msg):
    '''
    Return the foundation alert class for a message level.
    '''
    try:
        return MESSAGE_LEVELS[msg.level]
    except KeyError:
        try:
            return constants.DEFAULT_TAGS[msg.level]
        except KeyError:
            return msg.level

@register.simple_tag
def set_active_menu(active_menu):
    '''
    Inserts a span with a class of .nuit-active-menu that is picked up by Javascript
    to highlight the correct menu item.
    '''
    return "<span style='display: none' class='nuit-active-menu'>%s</span>" % active_menu


class ExtendNode(ExtendsNode):
    '''
    Template node that extends another template with additional variables.
    '''

    def __init__(self, node, kwargs):
        super(ExtendNode, self).__init__(node.nodelist, node.parent_name, node.template_dirs)
        self.kwargs = dict(("nuit_%s" % key, value) for key, value in kwargs.iteritems())

    def __repr__(self):
        return '<ExtendNode: extends %s with args: %r>' % (super(ExtendNode, self).__repr__(), self.kwargs)

    def render(self, context):
        kwargs = dict((key, value.resolve(context)) for key, value in self.kwargs.iteritems())
        context.update(kwargs)
        try:
            return super(ExtendNode, self).render(context)
        finally:
            context.pop()

@register.tag
def extend(parser, token):
    '''
    Extends another template, passing additional variables to the parent.
    '''
    bits = token.split_contents()
    kwargs = token_kwargs(bits[2:], parser)
    token.contents = " ".join(bits[:2])
    return ExtendNode(do_extends(parser, token), kwargs)


class MenuSectionNode(template.Node):
    '''
    Template node that renders a menu section.
    '''
    # pylint: disable=W0622

    def __init__(self, nodelist, title=NoneFilterExpression, is_list=FalseFilterExpression, link_name=NoneFilterExpression, id=NoneFilterExpression):
        self.nodelist = nodelist
        self.title = title
        self.is_list = is_list
        self.link_name = link_name
        self.link_id = id

    def render(self, context):
        content = self.nodelist.render(context)
        bare_title = self.title.resolve(context)
        title = '<h5>%s</h5>' % bare_title if bare_title else ''
        link_name = self.link_name.resolve(context) or bare_title
        resolved_link_id = self.link_id.resolve(context)
        return '''
            <section class='right-menu-reveal' {reveal} data-link='{link_name}' id='{id}'>
                <div>
                {title}
                {list_begin}
                {content}
                {list_end}
                </div>
                <hr />
            </section>
        '''.format(
            title = title,
            content = content,
            link_name = link_name,
            id = resolved_link_id or slugify(link_name),
            list_begin = "<nav><ul class='side-nav'>" if self.is_list.resolve(context) else '',
            list_end = '</ul></nav>' if self.is_list.resolve(context) else '',
            reveal = 'data-reveal' if not self.is_list.resolve(context) else '',
        )



@register.tag
def menu_section(parser, token):
    '''
    Renders the correct HTML for a menu section.
    '''
    args = token.split_contents()
    kwargs = {}
    for kwarg in args[1:]:
        if '=' not in kwarg:
            kwargs['title'] = kwarg
            continue
        before, after = kwarg.split('=')
        kwargs[before] = after
    nodelist = parser.parse(('end_menu_section',))
    parser.delete_first_token()
    kwargs = dict((key, parser.compile_filter(value)) for key, value in kwargs.iteritems())
    return MenuSectionNode(nodelist, **kwargs)


class AppMenuNode(template.Node):
    '''
    Template node that renders the main application menu for Nuit.
    '''

    def __init__(self, nodelist, title=None):
        self.nodelist = nodelist
        self.title = title

    def render(self, context):
        content = self.nodelist.render(context)
        title = '<h5>%s</h5>' % self.title.resolve(context) if self.title else ''
        return "<section class='main-nav'>{title}<nav><ul class='side-nav'>{content}</ul></nav><hr /></section>".format(title=title, content=content)

@register.tag
def app_menu(parser, token):
    '''
    Renders the main application menu for Nuit.
    '''
    bits = token.split_contents()
    if len(bits) > 2:
        raise template.TemplateSyntaxError('Wrong number of arguments for app_menu - expected 2 maximum')
    title = None
    if len(bits) == 2:
        title = parser.compile_filter(bits[1])
    nodelist = parser.parse(('end_app_menu',))
    parser.delete_first_token()
    return AppMenuNode(nodelist, title=title)

@register.simple_tag
def menu_item(link, name, id=None, current=False, unavailable=False):
    '''
    Renders an HTML anchor element in a list element.
    '''
    # pylint: disable=W0622
    if not id:
        id = slugify(name)
    classes = []
    if current:
        classes.append('current')
    if unavailable:
        classes.append('unavailable')
    return "<li class='menu-{id} {classes}'><a href='{link}'>{name}</a></li>".format(name=name, link=link, id=id, classes=' '.join(classes))


@register.inclusion_tag('nuit/includes/_pagination_menu.html', takes_context=True)
def pagination_menu(context, page_obj, show_totals=True):
    '''
    Renders the HTML required for the pagination options.
    '''
    total_pages = page_obj.paginator.page_range
    actual_numbers = [page for page in total_pages if page >= total_pages[-1] - 1 or page <= 2 or (page >= page_obj.number - 2 and page <= page_obj.number + 2)]
    page_list = []
    for i, number in enumerate(actual_numbers[:-1]):
        page_list.append(number)
        if actual_numbers[i + 1] != number + 1:
            page_list.append(None)
    page_list.append(actual_numbers[-1])
    return {
        'context': context,
        'page_obj': page_obj,
        'page_list': page_list,
        'show_totals': show_totals,
    }


def calculate_widths(parts, num=12):
    '''
    Generates a list of length parts containing integers, the sum of which is num.
    '''
    first = num // parts
    last  = num - (parts - 1) * first
    return (parts - 1) * [first] + [last]


class FoundationFormField(object):
    '''
    A form field, containing Foundation-markup specific parameters.
    '''
    # pylint: disable=R0902
    # pylint: disable=C0301

    def __init__(self, field, small=12, medium=None, large=None, prefix=None, prefix_small=3, prefix_medium=None, prefix_large=None, postfix=None, postfix_small=3, postfix_medium=None, postfix_large=None, show_label=True):
        # pylint: disable=R0913
        self.field = field
        self.small_width = small
        self.medium_width = medium or self.small_width
        self.large_width = large or self.medium_width
        self.prefix = prefix
        self.prefix_small_width = prefix_small
        self.prefix_medium_width = prefix_medium or self.prefix_small_width
        self.prefix_large_width = prefix_large or self.prefix_medium_width
        self.postfix = postfix
        self.postfix_small_width = postfix_small
        self.postfix_medium_width = postfix_medium or self.postfix_small_width
        self.postfix_large_width = postfix_large or self.postfix_medium_width
        self.show_label = show_label

        if self.prefix or self.postfix:
            self.fix_field_small_width = 12 - (self.prefix_small_width if self.prefix else 0) - (self.postfix_small_width if self.postfix else 0)
            self.fix_field_medium_width = 12 - (self.prefix_medium_width if self.prefix else 0) - (self.postfix_medium_width if self.postfix else 0)
            self.fix_field_large_width = 12 - (self.prefix_large_width if self.prefix else 0) - (self.postfix_large_width if self.postfix else 0)

def normalise_row(row_data):
    # pylint: disable=R0912
    sizes = {
        'field': ('small', 'medium', 'large',)
    }
    sizes['prefixes'] = tuple('prefix_%s' % s for s in sizes['field'])
    sizes['postfixes'] = tuple('postfix_%s' % s for s in sizes['field'])

    # For each field in the row, for each type of size, propagate any given sizes upwards.
    for _field, field_data in row_data:
        for size_type in sizes.keys():
            current_size = None
            for size in sizes[size_type]:
                if size in field_data:
                    current_size = field_data[size]
                elif current_size:
                    field_data[size] = current_size

    # For each size option, set the width properties of each field as defined.
    # Default to all 12 for small sizes, and calculate any unspecified widths.
    for size in sizes['field']:
        total = sum(y[size] for x, y in row_data if size in y)
        unspecified = len([x for x, y in row_data if size not in y or not y[size]])
        if unspecified == len(row_data) and size == 'small':
            unspecified_widths = [12] * unspecified
        else:
            unspecified_widths = calculate_widths(unspecified, 12 - total)
        for _field, data in row_data:
            if size in data and data[size]:
                continue
            data[size] = unspecified_widths.pop(0)

    # For each field, set the prefix/postfix widths if not defined.
    for _field, field_data in row_data:
        for size_type in sizes.keys():
            if size_type == 'field':
                continue
            for size in sizes[size_type]:
                if size not in field_data or not field_data[size]:
                    field_data[size] = 3

class FoundationFormNode(template.Node):
    '''
    A template node for a form field capabale of rendering Foundation-specific markup.
    '''

    def __init__(self, form, nodelist, csrf_enabled=TrueFilterExpression, collapse_container=FalseFilterExpression):
        self.form = form
        self.nodelist = nodelist
        self.csrf_enabled = csrf_enabled
        self.collapse_container = collapse_container

    def render(self, context):
        # pylint: disable=R0912
        # pylint: disable=R0914
        form = self.form.resolve(context)
        form_template = get_template('nuit/includes/_form.html')

        layout_instructions = []
        for line in self.nodelist.render(context).splitlines():
            if not line.strip():
                continue
            row_data = []
            for field_data in line.split(';'):
                field_data = field_data.strip()
                if not field_data:
                    continue
                try:
                    field_name, data = [x.strip() for x in field_data.split(' ', 1)]
                except ValueError:
                    row_data.append((field_data, {}))
                else:
                    try:
                        row_data.append((field_name, literal_eval(data)))
                    except SyntaxError:
                        raise template.TemplateSyntaxError('Invalid parameters for field %s' % field_name)

            normalise_row(row_data)
            layout_instructions.append(row_data)

        all_fields = [field.name for field in form.visible_fields()]

        field_layout = []
        for field_line in layout_instructions:
            fields = []
            for field, data in field_line:
                try:
                    fields.append(FoundationFormField(form[field], **data))
                    all_fields.remove(field)
                except KeyError:
                    raise template.TemplateSyntaxError('Field %s not found in form' % field)
            field_layout.append(fields)

        if all_fields:
            remaining_fields = []
            for field in all_fields:
                remaining_fields.append(FoundationFormField(form[field]))
            field_layout.append(remaining_fields)

        context.update({
            'form': form,
            'fields': field_layout,
            'csrf_enabled': self.csrf_enabled.resolve(context),
            'collapse_container': self.collapse_container.resolve(context),
        })

        # Render the form. Template expects the form object, and a fields object
        # which is a list of list, each list representing a row of the form.
        # Each element in a row list is a FoundationFormField object.

        try:
            return form_template.render(context)
        finally:
            context.pop()

@register.tag
def foundation_form(parser, token):
    '''
    Renders a form with Foundation markup.
    '''
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError('Incorrect number of arguements for %s, Form object required' % bits[0])
    form = parser.compile_filter(bits[1])
    kwargs = token_kwargs(bits[2:], parser)
    nodelist = parser.parse(('end_foundation_form',))
    parser.delete_first_token()
    return FoundationFormNode(form, nodelist, **kwargs)

