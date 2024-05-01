from game.end_to_end_tests.base_game_test import BaseGameTest

from selenium.webdriver.common.by import By

class TestLanguageDropdown(BaseGameTest):
    def test_level_language_dropdown(self):
        page = self.go_to_level(1)
        assert page.element_exists_by_id("language_dropdown")

        self.selenium.find_element(By.ID, "language_dropdown").click()
        self.selenium.find_element(By.ID, "language_dropdown_fr").click()

        text_count = len(self.selenium.find_elements(By.XPATH, ("//*[contains(text(),'Move forwards')]")))
        assert text_count == 0
