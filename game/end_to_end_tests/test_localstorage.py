from django.urls.base import reverse
from .base_game_test import BaseGameTest
from selenium.webdriver.common.by import By


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def items(self):
        items = self.driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; "
        )
        return items

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")


class TestLocalStorage(BaseGameTest):
    def level_in_localstorage(self, level_number):
        items = LocalStorage(self.selenium).items()
        return (f"blocklyWorkspaceXml-{level_number}" in items) and (
            f"pythonWorkspace-{level_number}" in items
        )

    def test_localstorage_if_logged_in(self):
        self.login_once()
        self._complete_level(1)
        self.assertTrue(self.level_in_localstorage(1))

    def test_nothing_in_localstorage_if_not_logged_in(self):
        page = self.go_to_homepage()
        page.teacher_logout()

        level1 = self.go_to_level(1)

        ls = LocalStorage(self.selenium)
        ls.clear()

        solution = self.read_solution("once_forwards")
        script = f"""
            const xml = `{solution}`;
            Blockly.Xml.clearWorkspaceAndLoadFromXml(Blockly.Xml.textToDom(xml), Blockly.mainWorkspace);
            """
        self.selenium.execute_script(script)
        self.selenium.find_element_by_id("fast_tab").click()

        level1.wait_for_element_to_be_clickable((By.CSS_SELECTOR, "#next_level_button"))
        level1.next_level()
        self.assertFalse(self.level_in_localstorage(1))
