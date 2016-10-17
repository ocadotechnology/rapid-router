# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
import os
import time

from django.core.urlresolvers import reverse
from hamcrest import assert_that, equal_to, contains_string, starts_with, ends_with
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from portal.tests.pageObjects.portal.base_page import BasePage


class GamePage(BasePage):
    def __init__(self, browser):
        super(GamePage, self).__init__(browser)

        assert self.on_correct_page('game_page')

        self._dismiss_initial_dialog()

    def _dismiss_initial_dialog(self):
        self.dismiss_dialog("play_button")
        return self

    def dismiss_dialog(self, button_id):
        self.wait_for_element_to_be_clickable((By.ID, button_id))
        self.browser.find_element_by_id(button_id).click()
        self.wait_for_element_to_be_invisible((By.ID, button_id))

    def load_solution(self, workspace_id):
        self.browser.find_element_by_id("load_tab").click()
        selector = "#loadWorkspaceTable tr[value=\'" + str(workspace_id) + "\']"
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
        time.sleep(1)
        return self

    def assert_level_number(self, level_number):
        path = reverse('play_default_level', kwargs={'levelName': str(level_number)})
        assert_that(self.browser.current_url, ends_with(path))

    def assert_episode_number(self, episode_number):
        path = reverse('start_episode', kwargs={'episodeId': str(episode_number)})
        assert_that(self.browser.current_url, ends_with(path))

    def assert_is_green_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "green")

    def assert_is_red_light(self, traffic_light_index):
        self._assert_light_is_on(traffic_light_index, "red")

    def _assert_light_is_on(self, traffic_light_index, colour):
        image = self.browser.find_element_by_id("trafficLight_%s_%s" % (traffic_light_index, colour))

        assert_that(image.get_attribute("opacity"), equal_to("1"))

    def run_program(self, wait_for_element_id="modal-content"):
        self.browser.find_element_by_id("fast_tab").click()

        try:
            self.wait_for_element_to_be_clickable((By.ID, wait_for_element_id), 45)
        except TimeoutException as e:
            import time
            millis = int(round(time.time() * 1000))
            screenshot_filename = '/tmp/game_tests_%s-%s.png' % (os.getenv("BUILD_NUMBER", "nonumber"), str(millis))
            print("Saved screenshot to " + screenshot_filename)
            self.browser.get_screenshot_as_file(screenshot_filename)
            raise e

        return self

    def run_crashing_program(self):
        return self._run_failing_program("What went wrong")

    def run_cow_crashing_program(self):
        return self._run_failing_program("You ran into a cow!")

    def run_program_that_runs_out_of_instructions(self):
        return self._run_failing_program("The van ran out of instructions before it reached a destination.")

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
        self.run_program('try_again_button')
        error_message = self.browser.find_element_by_id('myModal-lead').text
        assert_that(error_message, contains_string(text))
        return self

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
