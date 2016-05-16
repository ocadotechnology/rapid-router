# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
'''Game autoconfig'''
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_SETTINGS = {
    'STATIC_URL': '/static/',
}

SETTINGS = {
    'PIPELINE_COMPILERS': (
        'pipeline.compilers.sass.SASSCompiler',
    ),
    'PIPELINE_CSS': {
        'game-scss': {
            'source_filenames': (
              'game.scss',
            ),
            'output_filename': 'game.css',
        },
    },
    'PIPELINE_CSS_COMPRESSOR': None,
    'INSTALLED_APPS': [
        'game',
        'pipeline',
        'portal',
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_js_reverse',
        'foundation_scss',
        'foundation_icons',
        'bourbon',
        'rest_framework',
    ],
    'LANGUAGES': [
        ('lol-us', 'Localisation'),
    ],
    'LOCALE_PATHS': [
        # This shouldn't be needed, but it looks like there's an issue with
        # using a language code that's not in `django/conf/locale` - the
        # check_for_language function doesn't recognise it.
        os.path.join(os.path.dirname(__file__), 'locale'),
    ],
    'PIPELINE_SASS_ARGUMENTS': '--quiet',
    'STATICFILES_FINDERS': [
        'pipeline.finders.PipelineFinder',
    ],
    'STATICFILES_STORAGE': 'pipeline.storage.PipelineStorage',
    'TEMPLATES': [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request'
                ]
            }
        }
    ],
    'USE_TZ': True,
}
