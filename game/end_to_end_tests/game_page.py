from __future__ import print_function
from builtins import str
import os
import time

from django.urls import reverse
from hamcrest import assert_that, equal_to, contains_string, ends_with
from portal.tests.pageObjects.portal.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import (
    presence_of_all_elements_located,
)
from selenium.webdriver.support.ui import WebDriverWait


class GamePage(BasePage):
    def __init__(self, browser):
        super(GamePage, self).__init__(browser)

        assert self.on_correct_page("game_page")

        self._dismiss_initial_dialog()

    def _dismiss_initial_dialog(self):
        self.dismiss_dialog("play_button")
        return self

    def dismiss_dialog(self, button_id):
        self.wait_for_element_to_be_clickable((By.ID, button_id), wait_seconds=15)
        self.browser.find_element_by_id(button_id).click()
        self.wait_for_element_to_be_invisible((By.ID, button_id), wait_seconds=15)

    def load_solution(self, workspace_id):
        self.browser.find_element_by_id("load_tab").click()
        selector = "#loadWorkspaceTable tr[value='" + str(workspace_id) + "']"
        self.wait_for_element_to_be_clickable((By.CSS_SELECTOR, selector))
        self.browser.find_element_by_css_selector(selector).click()
        self.browser.find_element_by_id("loadWorkspace").click()
        time.sleep(1)
        return self

    def clear(self):
        self.browser.find_element_by_id("clear_tab").click()
        return self

    def try_again(self):
        self.dismiss_dialog("try_again_button")
        return self

    def step(self):
        self.browser.find_element_by_id("step_tab").click()
        return self

    def solution_button(self):
        self.browser.find_element_by_id("solution_tab").click()
        solution_loaded = self.browser.execute_script("return ocargo.solutionLoaded;")
        timeout = time.time() + 30

        while not solution_loaded:
            solution_loaded = self.browser.execute_script(
                "return ocargo.solutionLoaded;"
            )
            if time.time() > timeout:
                break
        return self

    def python_commands_button(self):
        self.browser.find_element_by_id("van_commands_help").click()
        return self

    def clear_console_button(self):
        self.browser.find_element_by_id("clear_console").click()
        return self

    def assert_level_number(self, level_number):
        path = reverse("play_default_level", kwargs={"levelName": str(level_number)})
        assert_that(self.browser.current_url.replace("#myModal", ""), ends_with(path))

    def assert_episode_number(self, episode_number):
        path = reverse("start_episode", kwargs={"episodeId": str(episode_number)})
        assert_that(self.browser.current_url.replace("#myModal", ""), ends_with(path))

    def assert_is_green_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "green")

    def assert_is_red_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "red")

    def _assert_light_is_on(self, traffic_light_index, colour):
        image = self.browser.find_element_by_id(
            "trafficLight_%s_%s" % (traffic_light_index, colour)
        )

        assert_that(image.get_attribute("opacity"), equal_to("1"))

    def run_program(self, wait_for_element_id="modal-content"):
        self.browser.find_element_by_id("fast_tab").click()

        try:
            self.wait_for_element_to_be_clickable((By.ID, wait_for_element_id), 45)
        except TimeoutException as e:
            import time

            millis = int(round(time.time() * 1000))
            screenshot_filename = "/tmp/game_tests_%s-%s.png" % (
                os.getenv("BUILD_NUMBER", "nonumber"),
                str(millis),
            )
            print("Saved screenshot to " + screenshot_filename)
            self.browser.get_screenshot_as_file(screenshot_filename)
            raise e

        return self

    def run_retry_program(self):
        self.run_program("try_again_button")
        modal_content = self.browser.find_element_by_id("modal-content").text
        assert_that(modal_content, contains_string("Try creating a simpler program."))
        self.browser.find_element_by_id("try_again_button").click()
        time.sleep(1)
        return self

    def run_crashing_program(self):
        return self._run_failing_program("What went wrong")

    def run_cow_crashing_program(self):
        return self._run_failing_program("You ran into a cow!")

    def run_out_of_instructions_program(self):
        return self._run_failing_program(
            "The van ran out of instructions before it reached a destination."
        )

    def run_out_of_fuel_program(self):
        return self._run_failing_program("You ran out of fuel!")

    def run_a_red_light_program(self):
        return self._run_failing_program(
            "Uh oh, you just sent the van through a red light!"
        )

    def run_not_delivered_everywhere_program(self):
        return self._run_failing_program(
            "There are destinations that have not been delivered to."
        )

    def run_undefined_procedure_program(self):
        return self._run_procedure_error_program(
            "Your program doesn't look quite right..."
        )

    def run_parse_error_program(self):
        return self._run_failing_python_program_console(
            "v.", "ParseError: bad input on line"
        )

    def run_attribute_error_program(self):
        return self._run_failing_python_program_console(
            "v.go()", "AttributeError: 'Van' object has no attribute"
        )

    def run_print_program(self):
        return self._run_failing_python_program_console(
            'print("hello world")', "hello world"
        )

    def run_invalid_import_program(self):
        return self._run_failing_python_program_popup(
            "import va", "You're not allowed to import anything other than 'van'."
        )

    def check_python_commands(self):
        self.python_commands_button()
        time.sleep(1)
        python_commands = self.browser.find_element_by_id("myModal-lead").text
        assert_that(
            python_commands,
            contains_string("Run the following commands on the van object v"),
        )
        return self

    def write_to_then_clear_console(self):
        self._write_code("v.")
        self.browser.find_element_by_id("fast_tab").click()
        time.sleep(1)
        console = self.browser.find_element_by_id("consoleOutput")
        self.clear_console_button()
        assert_that(console.text == "")
        return self

    def next_episode(self):
        self.assert_success()
        self.browser.find_element_by_id("next_episode_button").click()
        WebDriverWait(self.browser, 10).until(
            presence_of_all_elements_located((By.ID, "blockly_tab"))
        )
        return self

    def next_level(self):
        self.assert_success()
        self.browser.find_element_by_id("next_level_button").click()
        WebDriverWait(self.browser, 10).until(
            presence_of_all_elements_located((By.ID, "blockly_tab"))
        )
        return self

    def _run_failing_program(self, text):
        self.run_program("try_again_button")
        error_message = self.browser.find_element_by_id("myModal-lead").text
        assert_that(error_message, contains_string(text))
        return self

    def _run_failing_python_program_console(self, code, console_message):
        self._write_code(code)
        self.browser.find_element_by_id("fast_tab").click()
        time.sleep(1)
        console = self.browser.find_element_by_id("consoleOutput")
        assert_that(console.text, contains_string(console_message))
        return self

    def _run_failing_python_program_popup(self, code, text):
        self._write_code(code)
        self.browser.find_element_by_id("fast_tab").click()
        time.sleep(1)
        error_message = self.browser.find_element_by_id("myModal-lead").text
        assert_that(error_message, contains_string(text))
        return self

    def _write_code(self, code):
        self.browser.execute_script(
            "ocargo.pythonControl.appendCode(arguments[0])", code
        )
        return self

    def _run_procedure_error_program(self, text):
        self.run_program("close_button")
        error_message = self.browser.find_element_by_id("myModal-mainText").text
        assert_that(error_message, contains_string(text))

    def _assert_score(self, element_id, score):
        score_text = self.browser.find_element_by_id(element_id).text
        score_number = score_text.split("/")[0]
        assert_that(score_number, equal_to(str(score)))
        return self

    def assert_success(self):
        modal_content = self.browser.find_element_by_id("modal-content").text
        assert_that(modal_content, contains_string("Congratulations"))
        return self

    def assert_route_score(self, score):
        return self._assert_score("routeScore", score)

    def assert_algorithm_score(self, score):
        return self._assert_score("algorithmScore", score)
