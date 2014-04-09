'''Nuit autoconfig'''

SETTINGS = {
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
        'nuit.context_processors.nuit',
    ],
    'INSTALLED_APPS': [
        'django.contrib.staticfiles',
        'compressor',
        'foundation_scss',
        'foundation_icons',
        'jquery',
        'bourbon',
    ],
}

# We need to add this globally as we're making a new ExtendsNode
# and this needs to be the first node in the template.
from django.template.base import add_to_builtins
add_to_builtins('nuit.templatetags.nuit')
