from django.conf import settings
from django.contrib.staticfiles.testing import LiveServerTestCase
from django_selenium_clean import selenium


class SeleniumTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):

        super(SeleniumTestCase, cls).setUpClass()

        # Normally we would just do something like
        #     selenium.live_server_url = self.live_server_url
        # However, there is no "self" at this time, so we
        # essentially duplicate the code from the definition of
        # the LiveServerTestCase.live_server_url property.
        selenium.live_server_url = 'http://%s:%s' % (
            cls.server_thread.host, cls.server_thread.port)

    def __call__(self, result=None):
        if not selenium:
            return super(SeleniumTestCase, self).__call__(result)
        for width in getattr(settings, 'SELENIUM_WIDTHS', [1024]):
            selenium.set_window_size(width, 1024)
            super(SeleniumTestCase, self).__call__(result)
