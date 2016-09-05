import os
from selenium import webdriver

SELENIUM_WEBDRIVERS = {
    'default': {
        'callable': webdriver.Firefox,
        'args': (),
        'kwargs': {},
    },
    'chrome': {
        'callable': webdriver.Chrome,
        'args': (),
        'kwargs': {},
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
INSTALLED_APPS = ['game']
PIPELINE_ENABLED = False
ROOT_URLCONF = 'django_autoconfig.autourlconf'
SECRET_KEY = 'test'
STATIC_ROOT = '.tests_static/'

from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())
