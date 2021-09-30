import os

from django.test import modify_settings


def add_new_language():
    return modify_settings(
        LANGUAGES={"append": [("foo-br", "Test locale")]},
        LOCALE_PATHS={
            "append": os.path.join(os.path.dirname(__file__), "..", "locale")
        },
    )
