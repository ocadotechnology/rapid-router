"""
Patch SeleniumTestCase from django-selenium-clean package.

Instead of inheriting from StaticLiveServerTestCase, we inherit from LiveServerTestCase.
This solves a bug introduced when upgrading to Django 1.11,
see more information here: https://github.com/jazzband/django-pipeline/issues/593
"""

from django.contrib.staticfiles.testing import LiveServerTestCase
from django_selenium_clean import SeleniumTestCase

SeleniumTestCase.__bases__ = (LiveServerTestCase,)
