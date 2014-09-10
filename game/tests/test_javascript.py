from casper.tests import CasperTestCase
import os.path


class JavascriptTest(CasperTestCase):
    def test_tests(self):
        self.assertTrue(self.casper(
            os.path.join(os.path.dirname(__file__), 'casper-tests/test.js')))
