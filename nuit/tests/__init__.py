'''Tests for nuit'''
# pylint: disable=R0904
from django.test import TestCase, RequestFactory
from django.test.utils import override_settings
from django.contrib.messages import constants
from django.core.paginator import Paginator
from django.template import Template, Context, TemplateSyntaxError
from bs4 import BeautifulSoup as soup

from .forms import TestForm
from ..context_processors import nuit as nuit_context_processor
from ..templatetags.nuit import message_class, set_active_menu, menu_item, calculate_widths, pagination_menu
from ..views import SearchableListView

from django.db import models

import string

def setup_view(view, request, *args, **kwargs):
    """Mimic as_view() returned callable, but returns view instance.

    args and kwargs are the same you would pass to ``reverse()``

    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

class NuitViews(TestCase):
    '''Tests Nuit's views'''

    def setUp(self):
        for letter in string.ascii_uppercase:
            Publisher(
                name = 'Publisher %s' % letter,
                address = 'Address %s' % letter,
                city = 'City %s' % letter,
                state_province = 'State %s' % letter,
                website = 'http://www.publisher%s.com' % letter,
            ).save()

    def setup_list_view(self, query_string=None, search_fields=None):
        request = RequestFactory().get('/fake-path/?%s' % query_string)
        view = SearchableListView()
        view.model = Publisher
        if search_fields:
            view.search_fields = search_fields
        return setup_view(view, request)

    def test_searchable_list_view_context_no_fields(self):
        view = self.setup_list_view()
        context = view.get_context_data(object_list=[])
        self.assertTrue('search' not in context)
        self.assertTrue('search_query' not in context)

    def test_searchable_list_view_context_no_search(self):
        view = self.setup_list_view(search_fields=('name', 'address',))
        context = view.get_context_data(object_list=[])
        self.assertTrue(context['search'])

    def test_searchable_list_view_context_search(self):
        view = self.setup_list_view('q=isher%20A', ('name', 'address',))
        context = view.get_context_data(object_list=[])
        self.assertTrue(context['search'])
        self.assertEqual('isher A', context['search_query'])

    def test_searchable_list_view_queryset_no_fields(self):
        view = self.setup_list_view()
        self.assertEqual(Publisher.objects.count(), view.get_queryset().count())

    def test_searchable_list_view_queryset_no_search(self):
        view = self.setup_list_view(search_fields=('name', 'address',))
        self.assertEqual(Publisher.objects.count(), view.get_queryset().count())

    def test_searchable_list_view_queryset_search(self):
        view = self.setup_list_view('q=isher%20A', ('name', 'address',))
        self.assertEqual(1, view.get_queryset().count())

    def test_searchable_list_view_queryset_different_lookup(self):
        view = self.setup_list_view('q=isher%20A', (('name', 'startswith'),))
        self.assertEqual(0, view.get_queryset().count())

class NuitContextProcessors(TestCase):
    '''Tests Nuit's context processors'''

    sample_settings = {
        'NUIT_APPLICATIONS': [{'name': 'Link', 'link': 'http://www.google.com'}],
        'NUIT_GLOBAL_TITLE': 'Title',
        'NUIT_GLOBAL_LINK': 'http://www.google.com',
        'NUIT_LARGE_LOGO': 'logo.png',
        'NUIT_SMALL_LOGO': 'small_logo.png',
    }

    def test_nuit_context_processor(self):
        with self.settings(**self.sample_settings):
            resulting_dict = nuit_context_processor(None)
        expected_resulting_settings = self.sample_settings
        expected_resulting_settings['NUIT_LOGIN_URL'] = '/accounts/login/'
        expected_resulting_settings['NUIT_LOGOUT_URL'] = '/accounts/logout/'
        self.assertEqual(resulting_dict, expected_resulting_settings)

class NuitHandlers(TestCase):
    '''Tests Nuit's handlers'''
    urls = 'nuit.tests.urls'

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_400(self):
        response = self.client.get('/error400/')
        self.assertEqual(response.status_code, 400)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_403(self):
        response = self.client.get('/error403/')
        self.assertEqual(response.status_code, 403)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_404(self):
        response = self.client.get('/error404/')
        self.assertEqual(response.status_code, 404)

    @override_settings(COMPRESS_OFFLINE=False)
    def test_error_500(self):
        response = self.client.get('/error500/')
        self.assertEqual(response.status_code, 500)

class FakeMessage(object):
    def __init__(self, level):
        self.level = level

class NuitTemplateFilters(TestCase):
    '''Tests Nuit's template filters'''

    def test_message_class(self):
        self.assertEqual('alert', message_class(FakeMessage(constants.ERROR)))
        self.assertEqual('info', message_class(FakeMessage(constants.INFO)))
        self.assertEqual('invalid-level', message_class(FakeMessage('invalid-level')))

class NuitTemplateTags(TestCase):
    '''Tests Nuit's template tags'''

    def test_pagination_menu(self):

        for letter in string.ascii_uppercase:
            Publisher(
                name = 'Publisher %s' % letter,
                address = 'Address %s' % letter,
                city = 'City %s' % letter,
                state_province = 'State %s' % letter,
                website = 'http://www.publisher%s.com' % letter,
            ).save()

        paginator = Paginator(Publisher.objects.all(), 2)

        context = pagination_menu({}, paginator.page(1))
        self.assertEqual([1, 2, 3, None, 12, 13], context['page_list'])

        context = pagination_menu({}, paginator.page(7))
        self.assertEqual([1, 2, None, 5, 6, 7, 8, 9, None, 12, 13], context['page_list'])

        context = pagination_menu({}, paginator.page(12))
        self.assertEqual([1, 2, None, 10, 11, 12, 13], context['page_list'])

    def test_set_active_menu(self):
        output = soup(set_active_menu('bob')).find('span')
        self.assertEqual('bob', output.text)
        self.assertTrue('nuit-active-menu' in output.attrs['class'])
        self.assertTrue('display: none' in output.attrs['style'])

    def test_menu_item(self):
        output = soup(menu_item(link='/', name='bob')).find('li')
        self.assertEqual('bob', output.text)
        self.assertTrue('menu-bob' in output.attrs['class'])
        self.assertEqual('/', output.find('a').attrs['href'])

        output = soup(menu_item(link='/', name='bob', id='bobby', current=True, unavailable=True)).find('li')
        self.assertEqual('bob', output.text)
        self.assertTrue('menu-bobby' in output.attrs['class'])
        self.assertTrue('current' in output.attrs['class'])
        self.assertTrue('unavailable' in output.attrs['class'])
        self.assertEqual('/', output.find('a').attrs['href'])

    def test_calculate_widths(self):
        self.assertEqual([4, 4, 4], calculate_widths(3))
        self.assertEqual([3, 3, 3, 3], calculate_widths(4))
        self.assertEqual([2, 2, 2, 2, 4], calculate_widths(5))
        self.assertEqual([1], calculate_widths(1, 1))

    def test_menu_section(self):
        template = Template('''
            {% load nuit %}
            {% menu_section %}
                Section 1
            {% end_menu_section %}
            {% menu_section "Section 2" %}
                Section 2
            {% end_menu_section %}
            {% menu_section title=section_3 is_list=True %}
                <li>Section 3</li>
            {% end_menu_section %}
            {% menu_section link_name="Section 4" id="section-4-id" %}
                Section 4
            {% end_menu_section %}
        '''.strip())
        rendered = soup(template.render(Context({'section_3': 'Section 3'})))
        sections = rendered.findAll('section')

        expected_section_data = [
            {
                'header': False,
                'list': False,
                'attrs': {
                    'id': 'none',
                    'data-link': 'None',
                },
            },
            {
                'header': 'Section 2',
                'list': False,
                'attrs': {
                    'id': 'section-2',
                    'data-link': 'Section 2',
                },
            },
            {
                'header': 'Section 3',
                'list': True,
                'attrs': {
                },
            },
            {
                'header': False,
                'list': False,
                'attrs': {
                    'id': 'section-4-id',
                    'data-link': 'Section 4',
                },
            }
        ]

        self.assertEqual(4, len(sections))

        for section, data in zip(sections, expected_section_data):
            self.assertTrue('right-menu-reveal' in section.attrs['class'])
            if not data['list']:
                self.assertTrue('data-reveal' in section.attrs)
            else:
                self.assertEqual(1, len(section.findAll('nav')))
                self.assertEqual(1, len(section.find('nav').findAll('ul')))
                self.assertTrue('side-nav' in section.find('nav').find('ul').attrs['class'])
            if data['header']:
                self.assertEqual(1, len(section.findAll('h5')))
                self.assertEqual(data['header'], section.find('h5').text)
            for key, value in data['attrs'].iteritems():
                self.assertEqual(value, section.attrs[key])

    def test_app_menu(self):
        template = Template('''
            {% load nuit %}
            {% app_menu %}{% end_app_menu %}
            {% app_menu "Title" %}{% end_app_menu %}
            {% app_menu title %}content{% end_app_menu %}
        '''.strip())
        rendered = soup(template.render(Context({'title': 'Title 2'})))
        sections = rendered.findAll('section')

        self.assertEqual(3, len(sections))

        for section in sections:
            self.assertTrue('main-nav' in section.attrs['class'])
            self.assertEqual(1, len(section.findAll('nav')))
            self.assertEqual(1, len(section.find('nav').findAll('ul')))
            self.assertTrue('side-nav' in section.find('nav').find('ul').attrs['class'])

        self.assertTrue(1, len(sections[1].findAll('h5')))
        self.assertEqual('Title', sections[1].find('h5').text)
        self.assertTrue(1, len(sections[2].findAll('h5')))
        self.assertEqual('Title 2', sections[2].find('h5').text)

        with self.assertRaises(TemplateSyntaxError):
            Template('{% load nuit %}{% app_menu "one" "two" %}{% end_app_menu %}').render(Context())

def get_soup(template_contents, context_dict):
    return soup(Template(template_contents).render(Context(context_dict)))

class NuitFormTags(TestCase):
    '''Tests Nuit's form rendering - it's complex!'''

    def setUp(self):
        self.form = TestForm()

    def assert_on_widths(self, form_html, expected_fields_and_widths):
        for field, small, medium, large in expected_fields_and_widths:
            element = form_html.find('input', attrs={'name': field})
            parent_row = element.findParent('div', attrs={'class': 'columns'})
            self.assertTrue('small-%d' % small in parent_row.attrs['class'])
            self.assertTrue('medium-%d' % medium in parent_row.attrs['class'])
            self.assertTrue('large-%d' % large in parent_row.attrs['class'])

    def test_empty_form_tag(self):
        # pylint: disable=E1101
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, ((field, 12, 12, 12) for field in self.form.fields))

    def test_some_fields_defined(self):
        # pylint: disable=E1101
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            title

            firstname
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, ((field, 12, 12, 12) for field in self.form.fields))

    def test_fields_on_same_row(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            title; firstname; lastname
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('title', 12, 4, 4),
            ('firstname', 12, 4, 4),
            ('lastname', 12, 4, 4),
        ))

    def test_specifying_a_width(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            title {'medium': 2}; firstname;; lastname
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('title', 12, 2, 2),
            ('firstname', 12, 5, 5),
            ('lastname', 12, 5, 5),
        ))

    def test_resetting_higher_width(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            title {'small': 2, 'medium': 0}; firstname; lastname
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('title', 2, 4, 4),
            ('firstname', 5, 4, 4),
            ('lastname', 5, 4, 4),
        ))

    def test_prefix(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            url {'prefix': 'http://'}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('url', 9, 9, 9),
        ))

    def test_postfix(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            url {'postfix': '.com'}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('url', 9, 9, 9),
        ))

    def test_prefix_custom_widths(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            url {'prefix': 'http://', 'prefix_small': 4, 'prefix_medium': 5, 'prefix_large': 2}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('url', 8, 7, 10),
        ))

    def test_postfix_custom_widths(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form %}
            url {'postfix': '.com', 'postfix_small': 4, 'postfix_medium': 5, 'postfix_large': 2}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assert_on_widths(form_html, (
            ('url', 8, 7, 10),
        ))

    def test_no_csrf(self):
        form_html = get_soup('''
            {% load nuit %}
            {% foundation_form form csrf_enabled=False %}
            {% end_foundation_form %}
        ''', {'form': self.form})
        self.assertTrue('csrf' not in form_html)

    def test_invalid_field(self):
        with self.assertRaises(TemplateSyntaxError):
            get_soup('''
                {% load nuit %}
                {% foundation_form form %}
                this_field_does_not_exist
                {% end_foundation_form %}
            ''', {'form': self.form})

    def test_invalid_field_data(self):
        with self.assertRaises(TemplateSyntaxError):
            get_soup('''
                {% load nuit %}
                {% foundation_form form %}
                title invalid-field-data!!!; firstname; lastname
                {% end_foundation_form %}
            ''', {'form': self.form})

    def test_invalid_call(self):
        with self.assertRaises(TemplateSyntaxError):
            get_soup('''
                {% load nuit %}
                {% foundation_form %}
                {% end_foundation_form %}
            ''', {'form': self.form})
