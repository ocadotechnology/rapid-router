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
        'foundation_scss',
        'foundation_icons',
        'bourbon',
        'compressor',
        'rest_framework',
    ],
    'COMPRESS_ENABLED': True,
    'COMPRESS_PRECOMPILERS': [
        ('text/x-sass', 'sass {infile} {outfile}'),
        ('text/x-scss', 'sass {infile} {outfile}'),
    ],
    'STATICFILES_FINDERS': [
        'compressor.finders.CompressorFinder',
    ],
    'TEMPLATE_CONTEXT_PROCESSORS': [
        'django.core.context_processors.request',
    ],
}