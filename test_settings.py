import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

SELENIUM_WEBDRIVERS = {
    'default': {
        'callable': webdriver.Chrome,
        'args': (),
        'kwargs': {'chrome_options': chrome_options},
    },
    'chrome': {
        'callable': webdriver.Firefox,
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
