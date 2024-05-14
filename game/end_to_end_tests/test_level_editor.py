from game.end_to_end_tests.base_game_test import BaseGameTest
from game.views.level_editor import available_blocks
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestLevelEditor(BaseGameTest):
    def test_level_editor_displays(self):
        page = self.go_to_level_editor()

        assert page.element_exists_by_id("paper")

    def test_code_tab_blocks_load(self):
        page = self.go_to_level_editor()
        page.go_to_code_tab()

        block_types = [block.type for block in available_blocks()]

        for block_type in block_types:
            assert page.element_exists_by_id(f"{block_type}_checkbox")
            assert page.element_exists_by_id(f"{block_type}_image")

    def test_multiple_houses(self):
        add_road_button = self.selenium.find_element(By.ID, "add_road")
        add_road_button.click()

        road_start = self.selenium.find_element(By.CSS_SELECTOR, "image[x='130'][y='530']")
        road_end = self.selenium.find_element(By.CSS_SELECTOR, "image[x='330'][y='530']")
        ActionChains(self.selenium).drag_and_drop(road_start, road_end).perform()

        road_image = self.selenium.find_elements(By.CSS_SELECTOR, "image[href='/static/game/raphael_image/road_tiles/road/dead_end.svg']")
        assert len(road_image) > 0

        add_house_button = self.selenium.find_element(By.ID, "add_house")
        add_house_button.click()
        ActionChains(self.selenium).move_to_element(road_start).click().perform()
        ActionChains(self.selenium).move_to_element(road_end).click().perform()

        added_houses = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(added_houses) == 2

        delete_house_button = self.selenium.find_element(By.ID, "delete_house")
        delete_house_button.click()
        ActionChains(self.selenium).move_to_element(road_end).click().perform()

        houses_after_delete = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(houses_after_delete) == 1
