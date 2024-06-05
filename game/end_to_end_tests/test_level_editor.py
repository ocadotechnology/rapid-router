from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from game.end_to_end_tests.base_game_test import BaseGameTest
from game.views.level_editor import available_blocks


class TestLevelEditor(BaseGameTest):
    def set_up_basic_map(self):
        self.test_level_editor_displays()

        add_road_button = self.selenium.find_element(By.ID, "add_road")
        add_road_button.click()

        road_start = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='130'][y='530']")
        road_end = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='330'][y='530']")
        ActionChains(self.selenium).drag_and_drop(road_start, road_end).perform()

        mark_start_button = self.selenium.find_element(By.ID, "start")
        mark_start_button.click()
        ActionChains(self.selenium).move_to_element(road_start).click().perform()

        add_house_button = self.selenium.find_element(By.ID, "add_house")
        add_house_button.click()
        ActionChains(self.selenium).move_to_element(road_end).click().perform()

        return [road_start, road_end]

    def set_up_draggable_cow(self):
        scenery_tab = self.selenium.find_element(By.ID, "scenery_tab")
        scenery_tab.click()

        cow = self.selenium.find_element(By.CSS_SELECTOR, "img[id='cow']")
        cow.click()

        draggable_cow = self.selenium.find_element(By.CSS_SELECTOR, "image[x='0'][y='0']")

        return draggable_cow

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
        [road_start, road_end] = self.set_up_basic_map()

        road_middle = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='230'][y='530']")

        add_house_button = self.selenium.find_element(By.ID, "add_house")
        add_house_button.click()
        ActionChains(self.selenium).move_to_element(road_middle).click().perform()

        added_houses = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(added_houses) == 2

        delete_house_button = self.selenium.find_element(By.ID, "delete_house")
        delete_house_button.click()
        ActionChains(self.selenium).move_to_element(road_middle).click().perform()
        ActionChains(self.selenium).move_to_element(road_start).perform()

        houses_after_delete = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(houses_after_delete) == 1

    def test_cow_on_origin(self):
        [road_start, road_end] = self.set_up_basic_map()

        origin_space = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#ff0000']")
        assert len(origin_space) == 1

        draggable_cow = self.set_up_draggable_cow()
        ActionChains(self.selenium).click_and_hold(draggable_cow).move_to_element(road_start).perform()
        start_space_warning = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#e35f4d'][fill-opacity='0.7'][x='130'][y='530']")
        assert len(start_space_warning) == 1

    def test_cow_on_house(self):
        [road_start, road_end] = self.set_up_basic_map()

        house_space = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(house_space) == 1
        assert road_end == house_space[0]

        draggable_cow = self.set_up_draggable_cow()
        ActionChains(self.selenium).click_and_hold(draggable_cow).move_to_element(road_end).perform()
        allowed_space = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#87e34d']")
        assert len(allowed_space) == 0

    def test_draggable_decor(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_tree = self.selenium.find_element(By.ID, "tree2")
        end_space = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='130'][y='530']")
        ActionChains(self.selenium).drag_and_drop(source_tree, end_space).perform()

        decor_tree = self.selenium.find_elements(By.CSS_SELECTOR, "image[x='0'][y='0']")
        cloned_source_tree = self.selenium.find_elements(By.ID, "tree2")
        assert len(decor_tree) == 1
        assert len(cloned_source_tree) == 1
