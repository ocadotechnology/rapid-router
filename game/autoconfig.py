"""Game autoconfig"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEFAULT_SETTINGS = {"STATIC_URL": "/static/"}

SETTINGS = {
    "PIPELINE": {
        "SASS_ARGUMENTS": "--quiet",
        "COMPILERS": ("game.pipeline_compilers.LibSassCompiler",),
        "STYLESHEETS": {
            "game-scss": {
                "source_filenames": ("game/sass/game.scss",),
                "output_filename": "game.css",
            }
        },
        "CSS_COMPRESSOR": None,
    },
    "STATICFILES_FINDERS": ["pipeline.finders.PipelineFinder"],
    "STATICFILES_STORAGE": "pipeline.storage.PipelineStorage",
    "INSTALLED_APPS": [
        "game",
        "pipeline",
        "portal",
        "common",
        "django.contrib.admin",
        "django.contrib.admindocs",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django_js_reverse",
        "foundation_scss",
        "rest_framework",
    ],
    "LANGUAGES": [("lol-us", "Localisation")],
    "LOCALE_PATHS": [
        # This shouldn't be needed, but it looks like there's an issue with
        # using a language code that's not in `django/conf/locale` - the
        # check_for_language function doesn't recognise it.
        os.path.join(os.path.dirname(__file__), "locale")
    ],
    "TEMPLATES": [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": ["django.template.context_processors.request"]
            },
        }
    ],
    "USE_TZ": True,
}
