from time import sleep
from game.end_to_end_tests.base_game_test import BaseGameTest
from portal.tests.pageObjects.portal.base_page import BasePage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

DELAY_TIME = 10


class TestPythonLevels(BaseGameTest):
    def test_can_see_python_commands(self):
        self.run_python_commands_test(level=92)

    def test_clear_console(self):
        self.run_clear_console_test(level=92)

    def test_console_parse_error(self):
        self.run_console_parse_error_test(level=92)

    def test_console_attribute_error(self):
        self.run_console_attribute_error_test(level=92)

    def test_console_print(self):
        self.run_console_print_test(level=92)

    def test_invalid_import(self):
        self.run_invalid_import_test(level=109)

    def test_run_code(self):
        self.go_to_level(92)
        run_code = self.selenium.find_element_by_id("run-code-button")
        run_code.click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_all_elements_located((By.ID, "myModal-lead"))
        )
