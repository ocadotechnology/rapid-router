from selenium import webdriver
import os

SELENIUM_WEBDRIVERS = {
    "default": {"callable": webdriver.Chrome, "args": (), "kwargs": {}},
    "chrome": {"callable": webdriver.Firefox, "args": (), "kwargs": {}},
}

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

INSTALLED_APPS = ["game"]
PIPELINE_ENABLED = False

ROOT_URLCONF = "example_project.example_project.urls"
STATIC_ROOT = os.path.join(
    os.path.dirname(__file__), "example_project/example_project", "static"
)
SECRET_KEY = "test"


from django_autoconfig.autoconfig import configure_settings

configure_settings(globals())
