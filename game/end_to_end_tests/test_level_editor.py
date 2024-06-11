from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from game.end_to_end_tests.base_game_test import BaseGameTest
from game.views.level_editor import available_blocks

DELAY_TIME = 10


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
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        origin_space = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#ff0000']")
        assert len(origin_space) == 1

        page.go_to_scenery_tab()

        draggable_cow = self.selenium.find_element(By.ID, "cow")
        ActionChains(self.selenium).click_and_hold(draggable_cow).move_to_element(road_start).perform()
        start_space_warning = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#e35f4d'][fill-opacity='0.7'][x='130'][y='530']")
        assert len(start_space_warning) == 1

    def test_cow_on_house(self):
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        house_space = self.selenium.find_elements(By.CSS_SELECTOR, "rect[fill='#0000ff']")
        assert len(house_space) == 1
        assert road_end == house_space[0]

        page.go_to_scenery_tab()

        draggable_cow = self.selenium.find_elements(By.ID, "cow")
        assert len(draggable_cow) == 1
        ActionChains(self.selenium).click_and_hold(draggable_cow[0]).move_to_element(road_end).perform()
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

    def test_draggable_cow(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_cow = self.selenium.find_element(By.ID, "cow")
        end_space = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='130'][y='530']")
        ActionChains(self.selenium).drag_and_drop(source_cow, end_space).perform()

        scenery_cow = self.selenium.find_elements(By.CSS_SELECTOR, "image[x='0'][y='0']")
        cloned_source_cow = self.selenium.find_elements(By.ID, "cow")
        assert len(scenery_cow) == 1
        assert len(cloned_source_cow) == 1

    def test_draggable_traffic_light(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_light = self.selenium.find_element(By.ID, "trafficLightRed")
        end_space = self.selenium.find_element(By.CSS_SELECTOR, "rect[x='130'][y='530']")
        ActionChains(self.selenium).drag_and_drop(source_light, end_space).perform()

        scenery_light = self.selenium.find_elements(By.CSS_SELECTOR, "image[x='0'][y='0']")
        cloned_source_light = self.selenium.find_elements(By.ID, "trafficLightRed")
        assert len(scenery_light) == 1
        assert len(cloned_source_light) == 1

    def test_custom_instruction_and_hint(self):
        # login
        self.login_once()

        # go to level editor and set up basic map
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        # fill in custom instruction and hint fields
        page.go_to_instruction_tab()
        self.selenium.find_element(By.ID, "aim").send_keys("test aim")
        self.selenium.find_element(By.ID, "instruction").send_keys("test lesson")

        page.go_to_hint_tab()
        Select(self.selenium.find_element(By.ID, "hint_timer_minutes")).select_by_value("1")
        Select(self.selenium.find_element(By.ID, "hint_trigger_attempts")).select_by_value("2")
        self.selenium.find_element(By.ID, "hint").send_keys("test hint")

        # save level and choose to play it
        page.go_to_save_tab()
        self.selenium.find_element(By.ID, "levelNameInput").send_keys("test level")
        self.selenium.find_element(By.ID, "saveLevel").click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "play_button"))
        )
        self.selenium.find_element(By.ID, "play_button").click()

        # check to see if custom aim and lesson appear on the initial popup
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "myModal-lead"))
        )
        modal_text = self.selenium.find_element(By.ID, "myModal-lead").get_attribute("innerHTML")
        assert "test aim test lesson" in modal_text
        self.selenium.find_element(By.ID, "close-modal").click()

        # wait for modal to disappear 
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.none_of(EC.visibility_of_all_elements_located((By.ID, "myModal-mainText")))
        )

        # check to see if the timed hint appears by waiting
        assert WebDriverWait(self.selenium, 65).until(
            EC.visibility_of_element_located((By.ID, "myModal-mainText"))
        )
        hint_modal_text_one = self.selenium.find_element(By.ID, "myModal-mainText").get_attribute("innerHTML")
        assert "test hint" in hint_modal_text_one
        # assert WebDriverWait(self.selenium, DELAY_TIME).until(
        #     EC.text_to_be_present_in_element_attribute((By.ID, "myModal-mainText"), "innerHTML", "test hint")
        # )
        self.selenium.find_element(By.ID, "play_button").click()

        # check to see if triggered hint appears by making a few failed attempts
        fast_tab = self.selenium.find_element(By.ID, "fast_tab")
        fast_tab.click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "try_again_button"))
        )
        self.selenium.find_element(By.ID, "try_again_button").click()

        fast_tab.click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "try_again_button"))
        )
        hint_modal_text_two = self.selenium.find_element(By.ID, "hintBtnPara").get_attribute("innerHTML")
        assert "test hint" in hint_modal_text_two
        self.selenium.find_element(By.ID, "try_again_button").click()

        # check to see if the custom hint appears on the hint popup
        self.selenium.find_element(By.ID, "help_tab").click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "myModal-mainText"))
        )
        hint_modal_text_three = self.selenium.find_element(By.ID, "myModal-mainText").get_attribute("innerHTML")
        assert "test hint" in hint_modal_text_three
