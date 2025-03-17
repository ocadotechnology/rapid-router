from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from game.end_to_end_tests.base_game_test import BaseGameTest
from game.views.level_editor import available_blocks

DELAY_TIME = 10


class TestLevelEditor(BaseGameTest):
    def set_up_basic_map(self):
        self.test_level_editor_displays()

        add_road_button = self.selenium.find_element(By.ID, "add_road")
        add_road_button.click()

        road_start = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='130'][y='530']"
        )
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

        road_middle = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='230'][y='530']"
        )

        add_house_button = self.selenium.find_element(By.ID, "add_house")
        add_house_button.click()
        ActionChains(self.selenium).move_to_element(road_middle).click().perform()

        added_houses = self.selenium.find_elements(
            By.CSS_SELECTOR, "rect[fill='#0000ff']"
        )
        assert len(added_houses) == 2

        delete_house_button = self.selenium.find_element(By.ID, "delete_house")
        delete_house_button.click()
        ActionChains(self.selenium).move_to_element(road_middle).click().perform()
        ActionChains(self.selenium).move_to_element(road_start).perform()

        houses_after_delete = self.selenium.find_elements(
            By.CSS_SELECTOR, "rect[fill='#0000ff']"
        )
        assert len(houses_after_delete) == 1

    def test_cow_on_origin(self):
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        origin_space = self.selenium.find_elements(
            By.CSS_SELECTOR, "rect[fill='#ff0000']"
        )
        assert len(origin_space) == 1

        page.go_to_scenery_tab()

        draggable_cow = self.selenium.find_element(By.ID, "cow")
        ActionChains(self.selenium).click_and_hold(draggable_cow).move_to_element(
            road_start
        ).perform()
        start_space_warning = self.selenium.find_elements(
            By.CSS_SELECTOR,
            "rect[fill='#e35f4d'][fill-opacity='0.7'][x='130'][y='530']",
        )
        assert len(start_space_warning) == 1

    def test_cow_on_house(self):
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        house_space = self.selenium.find_elements(
            By.CSS_SELECTOR, "rect[fill='#0000ff']"
        )
        assert len(house_space) == 1
        assert road_end == house_space[0]

        page.go_to_scenery_tab()

        draggable_cow = self.selenium.find_elements(By.ID, "cow")
        assert len(draggable_cow) == 1
        ActionChains(self.selenium).click_and_hold(draggable_cow[0]).move_to_element(
            road_end
        ).perform()
        allowed_space = self.selenium.find_elements(
            By.CSS_SELECTOR, "rect[fill='#87e34d']"
        )
        assert len(allowed_space) == 0

    def test_draggable_decor(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_tree = self.selenium.find_element(By.ID, "tree2")
        end_space = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='130'][y='530']"
        )
        ActionChains(self.selenium).drag_and_drop(source_tree, end_space).perform()

        decor_tree = self.selenium.find_elements(By.CSS_SELECTOR, "image[x='0'][y='0']")
        cloned_source_tree = self.selenium.find_elements(By.ID, "tree2")
        assert len(decor_tree) == 1
        assert len(cloned_source_tree) == 1

    def test_draggable_cow(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_cow = self.selenium.find_element(By.ID, "cow")
        end_space = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='130'][y='530']"
        )
        ActionChains(self.selenium).drag_and_drop(source_cow, end_space).perform()

        scenery_cow = self.selenium.find_elements(
            By.CSS_SELECTOR, "image[x='0'][y='0']"
        )
        cloned_source_cow = self.selenium.find_elements(By.ID, "cow")
        assert len(scenery_cow) == 1
        assert len(cloned_source_cow) == 1

    def test_draggable_traffic_light(self):
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_light = self.selenium.find_element(By.ID, "trafficLightRed")
        end_space = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='130'][y='530']"
        )
        ActionChains(self.selenium).drag_and_drop(source_light, end_space).perform()

        scenery_light = self.selenium.find_elements(
            By.CSS_SELECTOR, "image[x='0'][y='0']"
        )
        cloned_source_light = self.selenium.find_elements(By.ID, "trafficLightRed")
        assert len(scenery_light) == 1
        assert len(cloned_source_light) == 1

    def test_custom_description_and_hint(self):
        # login
        self.login_once()

        # go to level editor and set up basic map
        page = self.go_to_level_editor()
        [road_start, road_end] = self.set_up_basic_map()

        # fill in custom description and hint fields
        page.go_to_description_tab()
        self.selenium.find_element(By.ID, "subtitle").send_keys("test subtitle")
        self.selenium.find_element(By.ID, "description").send_keys("test description")

        page.go_to_hint_tab()
        self.selenium.find_element(By.ID, "hint").send_keys("test hint")

        # save level and choose to play it
        page.go_to_save_tab()
        self.selenium.find_element(By.ID, "levelNameInput").send_keys("test level")
        self.selenium.find_element(By.ID, "saveLevel").click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "play_button"))
        )
        self.selenium.find_element(By.ID, "play_button").click()

        # check to see if custom subtitle and lesson appear on the initial popup
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "myModal-lead"))
        )
        modal_text = self.selenium.find_element(By.ID, "myModal-lead").get_attribute(
            "innerHTML"
        )
        assert "test subtitle" in modal_text
        assert "test description" in modal_text
        self.selenium.find_element(By.ID, "close-modal").click()

        # wait for modal to disappear
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.none_of(
                EC.visibility_of_all_elements_located((By.ID, "myModal-mainText"))
            )
        )

        # check to see if the custom hint appears on failure modal
        fast_tab = self.selenium.find_element(By.ID, "fast_tab")
        fast_tab.click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.visibility_of_element_located((By.ID, "hintPopupBtn"))
        )
        hint_button = self.selenium.find_element(By.ID, "hintPopupBtn")
        hint_button.click()

        hint_modal_text = self.selenium.find_element(By.ID, "hintText").get_attribute(
            "innerHTML"
        )
        hint_modal_style = self.selenium.find_element(By.ID, "hintText").get_attribute(
            "style"
        )
        assert "display: none" in hint_button.get_attribute("style")
        assert "display: block" in hint_modal_style
        assert "test hint" in hint_modal_text

        self.selenium.find_element(By.ID, "try_again_button").click()

        # check to see if the custom hint appears on the hint popup
        self.selenium.find_element(By.ID, "help_tab").click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.visibility_of_element_located((By.ID, "myModal-mainText"))
        )
        hint_modal_text_two = self.selenium.find_element(
            By.ID, "myModal-mainText"
        ).get_attribute("innerHTML")
        assert "test hint" in hint_modal_text_two

    def test_solar_panels(self):
        """test that the solar panels appear as a scenery option when clicking on the scenery tab
        """
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        solar_panel = self.selenium.find_element(
            By.ID, "solar_panel"
        )
        assert solar_panel.is_displayed()

    def test_electric_fuel_gauge(self):
        self.login_once()

        page = self.go_to_level_editor()

        [road_start, road_end] = self.set_up_basic_map()
        page.go_to_character_tab()

        # the electric van has dropdown value 7 - select the electric van as character
        Select(self.selenium.find_element(By.ID, "character_select")).select_by_value(
            "7"
        )

        # save level and choose to play it
        page.go_to_save_tab()
        self.selenium.find_element(By.ID, "levelNameInput").send_keys(
            "test electric van level"
        )
        self.selenium.find_element(By.ID, "saveLevel").click()
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.visibility_of_element_located((By.ID, "myModal-lead"))
        )
        self.selenium.find_element(By.ID, "play_button").click()

        # check to see if electric fuel gauge appears
        assert WebDriverWait(self.selenium, DELAY_TIME).until(
            EC.presence_of_element_located((By.ID, "electricFuelGauge"))
        )
        electric_fuel_gauge = self.selenium.find_element(By.ID, "electricFuelGauge")
        assert "visibility: visible" in electric_fuel_gauge.get_attribute("style")

    def test_pigeon(self):
        """Test that cows on the map automatically become pigeons when the theme is changed to "city" """
        page = self.go_to_level_editor()
        page.go_to_scenery_tab()

        source_cow = self.selenium.find_element(By.ID, "cow")
        end_space = self.selenium.find_element(
            By.CSS_SELECTOR, "rect[x='130'][y='530']"
        )
        ActionChains(self.selenium).drag_and_drop(source_cow, end_space).perform()

        scenery_cow = self.selenium.find_elements(
            By.CSS_SELECTOR, "image[x='0'][y='0']"
        )
        cow_link = scenery_cow[0].get_attribute("href")
        assert cow_link == "/static/game/raphael_image/Clarice.svg"

        Select(self.selenium.find_element(By.ID, "theme_select")).select_by_value(
            "city"
        )

        scenery_pigeon = self.selenium.find_elements(
            By.CSS_SELECTOR, "image[x='0'][y='0']"
        )
        pigeon_link = scenery_pigeon[0].get_attribute("href")
        assert pigeon_link == "/static/game/raphael_image/pigeon.svg"
