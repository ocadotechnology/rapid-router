'''Game autoconfig'''

SETTINGS = {
    'INSTALLED_APPS': [
        'game',
        'portal',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'nuit',
        'rest_framework',
    ],
}

# Keep this at the bottom
from django_autoconfig.autoconfig import configure_settings
configure_settings(globals())