from selenium import webdriver
import os

headless_chrome_options = webdriver.ChromeOptions()
headless_chrome_options.add_argument("--headless")
headless_chrome_options.add_argument("--no-sandbox")

SELENIUM_WEBDRIVERS = {
    "default": {"callable": webdriver.Chrome, "args": (), "kwargs": {}},
    "chrome": {"callable": webdriver.Firefox, "args": (), "kwargs": {}},
    "chrome-headless": {"callable": webdriver.Chrome, "args": (), "kwargs": {
        'options': headless_chrome_options
    }},
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
