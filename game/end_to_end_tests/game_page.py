from __future__ import print_function

import os
import time
from builtins import str

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

        self.browser.execute_script(
            "ocargo.animation.FAST_ANIMATION_DURATION = 1;"
        )

        assert self.on_correct_page("game_page")

        self._dismiss_initial_dialog()

    def _dismiss_initial_dialog(self):
        self.dismiss_dialog("play_button")
        return self

    def dismiss_dialog(self, button_id):
        self.wait_for_element_to_be_clickable(
            (By.ID, button_id), wait_seconds=15
        )
        self.browser.find_element(By.ID, button_id).click()
        self.wait_for_element_to_be_invisible(
            (By.ID, button_id), wait_seconds=15
        )

    def save_solution(self, workspace_name):
        self.browser.find_element(By.ID, "save_tab").click()
        self.browser.find_element(By.ID, "workspaceNameInput").send_keys(
            workspace_name
        )
        self.browser.find_element(By.ID, "saveWorkspace").click()
        return self

    def load_solution_by_name(self, solution_name):
        self.browser.find_element(By.ID, "load_tab").click()
        time.sleep(1)
        self.browser.find_element(By.ID, solution_name).click()
        self.browser.find_element(By.ID, "loadWorkspace").click()
        time.sleep(1)
        return self

    def load_solution(self, workspace_id):
        self.browser.find_element(By.ID, "load_tab").click()
        selector = "#loadWorkspaceTable tr[value='" + str(workspace_id) + "']"
        self.wait_for_element_to_be_clickable((By.CSS_SELECTOR, selector))
        self.browser.find_element(By.CSS_SELECTOR, selector).click()
        self.browser.find_element(By.ID, "loadWorkspace").click()
        time.sleep(1)
        return self

    def clear(self):
        self.browser.find_element(By.ID, "clear_tab").click()
        return self

    def try_again(self):
        self.dismiss_dialog("try_again_button")
        return self

    def step(self):
        self.browser.find_element(By.ID, "step_tab").click()
        return self

    def solution_button(self):
        self.browser.find_element(By.ID, "solution_tab").click()
        solution_loaded = self.browser.execute_script(
            "return ocargo.solutionLoaded;"
        )
        timeout = time.time() + 30

        while not solution_loaded:
            solution_loaded = self.browser.execute_script(
                "return ocargo.solutionLoaded;"
            )
            if time.time() > timeout:
                break
        return self

    def python_commands_button(self):
        self.browser.find_element(By.ID, "van_commands_help").click()
        return self

    def clear_console_button(self):
        self.browser.find_element(By.ID, "clear_console").click()
        return self

    def assert_level_number(self, level_number, from_python_den):
        viewname = (
            "play_python_default_level"
            if from_python_den
            else "play_default_level"
        )

        path = reverse(viewname, kwargs={"level_name": str(level_number)})
        assert_that(
            self.browser.current_url.replace("#myModal", ""), ends_with(path)
        )

    def assert_episode_number(self, episode_number, from_python_den):
        viewname = (
            "start_python_episode" if from_python_den else "start_episode"
        )

        path = reverse(viewname, kwargs={"episodeId": str(episode_number)})
        assert_that(
            self.browser.current_url.replace("#myModal", ""), ends_with(path)
        )

    def assert_is_green_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "green")

    def assert_is_red_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "red")

    def _assert_light_is_on(self, traffic_light_index, colour):
        image = self.browser.find_element(
            By.ID, "trafficLight_%s_%s" % (traffic_light_index, colour)
        )

        assert_that(image.get_attribute("opacity"), equal_to("1"))

    def run_program(self, wait_for_element_id="modal-content"):
        self.browser.find_element(By.ID, "fast_tab").click()

        try:
            self.wait_for_element_to_be_clickable(
                (By.ID, wait_for_element_id), 45
            )
        except TimeoutException as e:
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
        modal_content = self.browser.find_element(By.ID, "modal-content").text
        assert_that(
            modal_content, contains_string("Try creating a simpler program.")
        )
        self.browser.find_element(By.ID, "try_again_button").click()
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
            "my_van.", "ParseError: bad input on line"
        )

    def run_attribute_error_program(self):
        return self._run_failing_python_program_console(
            "my_van.go()", "AttributeError: 'Van' object has no attribute"
        )

    def run_print_program(self):
        return self._run_failing_python_program_console(
            'print("hello world")', "hello world"
        )

    def run_invalid_import_program(self):
        return self._run_failing_python_program_popup(
            "from van import Va", "You can only import 'Van' from 'van'"
        )

    def run_animal_sound_horn_program(self):
        return self._run_working_program(
            """
while not my_van.at_destination():
  if my_van.is_animal_crossing():
    my_van.sound_horn()
  if my_van.is_road_forward():
    my_van.move_forwards()
  elif my_van.is_road_left():
    my_van.turn_left()
  else:
    my_van.turn_right()""",
        )

    def check_python_commands(self):
        self.python_commands_button()
        time.sleep(1)
        python_commands = self.browser.find_element(By.ID, "myModal-lead").text
        assert_that(
            python_commands,
            contains_string("Run the following commands on the van object v"),
        )
        return self

    def write_to_then_clear_console(self):
        self._write_code("my_van.")
        self.browser.find_element(By.ID, "fast_tab").click()
        time.sleep(1)
        console = self.browser.find_element(By.ID, "consoleOutput")
        self.clear_console_button()
        assert_that(console.text == "")
        return self

    def next_episode(self, from_python_den=False):
        self.assert_success()
        self.browser.find_element(By.ID, "next_episode_button").click()

        tabId = "python_tab" if from_python_den else "blockly_tab"

        WebDriverWait(self.browser, 10).until(
            presence_of_all_elements_located((By.ID, tabId))
        )
        return self

    def next_level(self, from_python_den=False):
        self.assert_success()
        self.browser.find_element(By.ID, "next_level_button").click()

        tabId = "python_tab" if from_python_den else "blockly_tab"

        WebDriverWait(self.browser, 10).until(
            presence_of_all_elements_located((By.ID, tabId))
        )
        return self

    def next_level_redirected(self, from_python_den=False):
        self.assert_success()
        self.browser.find_element(By.ID, "next_level_button").click()

        episodeId = "episode-16" if from_python_den else "episode-1"

        WebDriverWait(self.browser, 10).until(
            presence_of_all_elements_located((By.ID, episodeId))
        )
        return self

    def _run_failing_program(self, text):
        self.run_program("try_again_button")
        error_message = self.browser.find_element(By.ID, "myModal-lead").text
        assert_that(error_message, contains_string(text))
        return self

    def _run_failing_python_program_console(self, code, console_message):
        self._write_code(code)
        self.browser.find_element(By.ID, "fast_tab").click()
        time.sleep(1)
        console = self.browser.find_element(By.ID, "consoleOutput")
        assert_that(console.text, contains_string(console_message))
        return self

    def _run_failing_python_program_popup(self, code, text):
        self._write_code(code)
        self.browser.find_element(By.ID, "fast_tab").click()
        time.sleep(1)
        error_message = self.browser.find_element(By.ID, "myModal-lead").text
        assert_that(error_message, contains_string(text))
        return self

    def _run_working_program(self, code):
        self._write_code(code)
        self.browser.find_element(By.ID, "fast_tab").click()
        time.sleep(1)
        return self

    def _write_code(self, code):
        self.browser.execute_script(
            "ocargo.pythonControl.appendCode(arguments[0])", code
        )
        return self

    def _run_procedure_error_program(self, text):
        self.run_program("close_button")
        error_message = self.browser.find_element(
            By.ID, "myModal-mainText"
        ).text
        assert_that(error_message, contains_string(text))

    def _assert_score(self, element_id, score):
        score_text = self.browser.find_element(By.ID, element_id).text
        score_number = score_text.split("/")[0]
        assert_that(score_number, equal_to(str(score)))
        return self

    def assert_success(self):
        modal_content = self.browser.find_element(By.ID, "modal-content").text
        assert_that(modal_content, contains_string("Congratulations"))
        return self

    def assert_route_score(self, score):
        return self._assert_score("routeScore", score)

    def assert_algorithm_score(self, score):
        return self._assert_score("algorithmScore", score)
