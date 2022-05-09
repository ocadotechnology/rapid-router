"""
Patch SeleniumTestCase from django-selenium-clean package.

Instead of inheriting from StaticLiveServerTestCase, we inherit from LiveServerTestCase.
This solves a bug introduced when upgrading to Django 1.11,
see more information here: https://github.com/jazzband/django-pipeline/issues/593
"""

from django.core.servers.basehttp import WSGIServer
from django.test.testcases import (
    LiveServerTestCase,
    LiveServerThread,
    QuietWSGIRequestHandler,
)
from django_selenium_clean import SeleniumTestCase


class NonThreadedLiveServerThread(LiveServerThread):
    """
    Replaces ThreadedWSGIServer with WSGIServer as the threaded one doesn't close the DB connections properly, thus
    triggering random "DB table locked" errors.
    """

    def _create_server(self):
        return WSGIServer(
            (self.host, self.port), QuietWSGIRequestHandler, allow_reuse_address=False
        )


SeleniumTestCase.__bases__ = (LiveServerTestCase,)
SeleniumTestCase.server_thread_class = NonThreadedLiveServerThread
