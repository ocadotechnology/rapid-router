"""Django settings for example_project project."""
import os

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'debug': DEBUG,
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.abspath(os.path.dirname(__file__)),'db.sqlite3'),  # Or path to database file if using sqlite3.
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
LANGUAGES = (('en-gb', 'English'),)
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'
SECRET_KEY = 'not-a-secret'

ROOT_URLCONF = 'example_project.urls'

WSGI_APPLICATION = 'example_project.wsgi.application'

INSTALLED_APPS = (
    'game',
)

ALLOWED_HOSTS = ['*']
PIPELINE_ENABLED = False

# This is used in common to enable/disable the OneTrust cookie management script
COOKIE_MANAGEMENT_ENABLED = False

try:
    from example_project.local_settings import *  # pylint: disable=E0611
except ImportError:
    pass

from django_autoconfig import autoconfig
autoconfig.configure_settings(globals())
