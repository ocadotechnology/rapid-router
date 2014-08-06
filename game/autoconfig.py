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
    'NUIT_GLOBAL_TITLE': "Rapid Router",
    'NUIT_GLOBAL_LINK': "/game/",
}