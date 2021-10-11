"""Game autoconfig"""
import os

from common.app_settings import domain

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
    # ----------------------------------------------------------------------------------
    # CSP CONFIG
    # ----------------------------------------------------------------------------------
    "CSP_DEFAULT_SRC": ("'self'",),
    # "CSP_CONNECT_SRC": (
    #     "'self'",
    #     "https://*.onetrust.com/",
    #     "https://euc-widget.freshworks.com/",
    #     "https://codeforlife.freshdesk.com/",
    # ),
    # "CSP_FONT_SRC": (
    #     "'self'",
    #     "https://fonts.gstatic.com/",
    #     "https://fonts.googleapis.com/",
    # ),
    "CSP_IMG_SRC": (
    #     "https://cdn-ukwest.onetrust.com/",
        f"{domain()}/static/game/image/",
        f"{domain()}/static/game/raphael_image/",
        f"{domain()}/static/game/js/blockly/media/",
    ),
    # "CSP_SCRIPT_SRC": (
    #     "'self'",
    #     "'unsafe-inline'",
    #     "https://*.onetrust.com/",
    #     "https://code.jquery.com/",
    #     "https://euc-widget.freshworks.com/",
    #     "https://cdn-ukwest.onetrust.com/",
    #     "https://code.iconify.design/2/2.0.3/iconify.min.js",
    #     "https://www.googletagmanager.com/gtm.js",
    #     "https://cdn.mouseflow.com/",
    #     "https://www.google-analytics.com/analytics.js",
    #     "https://www.recaptcha.net/",
    #     "https://www.google.com/recaptcha/",
    #     "https://www.gstatic.com/recaptcha/",
    #     f"{domain()}/static/portal/",
    #     f"{domain()}/static/common/",
    # ),
    # "CSP_STYLE_SRC": (
    #     "'self'",
    #     "'unsafe-inline'",
    #     "https://euc-widget.freshworks.com/",
    #     "https://cdn-ukwest.onetrust.com/",
    #     "https://fonts.googleapis.com/",
    #     f"{domain()}/static/hijack/",
    #     f"{domain()}/static/portal/",
    # ),
    "CSP_FRAME_SRC": (
        f"{domain()}/static/game/image/",
        "http://www.youtube-nocookie.com/",
    #     "https://www.recaptcha.net/",
    #     "https://www.google.com/recaptcha/",
    ),
    "CSP_OBJECT_SRC": (
        f"{domain()}/static/game/image/",
    ),
    "CSP_REPORT_ONLY": False,
}
