from portal.tests.pageObjects.portal.base_page import BasePage
from selenium.webdriver.common.by import By


class EditorPage(BasePage):
    def __init__(self, browser):
        super(EditorPage, self).__init__(browser)

        assert self.on_correct_page("editor_page")

        self._dismiss_initial_dialog()

    def _dismiss_initial_dialog(self):
        self.dismiss_dialog("close_button")
        return self

    def dismiss_dialog(self, button_id):
        self.wait_for_element_to_be_clickable((By.ID, button_id), wait_seconds=15)
        self.browser.find_element(By.ID, button_id).click()
        self.wait_for_element_to_be_invisible((By.ID, button_id), wait_seconds=15)

    def go_to_code_tab(self):
        self.browser.find_element(By.ID, "blocks_tab").click()

    def go_to_scenery_tab(self):
        self.browser.find_element(By.ID, "scenery_tab").click()

    def go_to_character_tab(self):
        self.browser.find_element(By.ID, "character_tab").click()

    def go_to_description_tab(self):
        self.browser.find_element(By.ID, "description_tab").click()

    def go_to_hint_tab(self):
        self.browser.find_element(By.ID, "hint_tab").click()

    def go_to_save_tab(self):
        self.browser.find_element(By.ID, "save_tab").click()
