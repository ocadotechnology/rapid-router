# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
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

from django.core.urlresolvers import reverse
from django_selenium_clean import selenium, SeleniumTestCase
from unittest import skipUnless

from portal.models import UserProfile
from game.models import Workspace
from portal.tests.pageObjects.portal.game_page import GamePage
from portal.tests.pageObjects.portal.home_page import HomePage
from portal.tests.utils.organisation import create_organisation_directly
from portal.tests.utils.teacher import signup_teacher_directly

@skipUnless(selenium, "Selenium is unconfigured")
class BaseGameTest(SeleniumTestCase):
    BLOCKLY_SOLUTIONS_DIR = os.path.join(os.path.dirname(__file__), 'data/blockly_solutions')

    already_logged_on = False
    user_profile = None

    def _go_to_path(self, path):
        selenium.get(self.live_server_url + path)

    def go_to_homepage(self):
        path = reverse('home')
        self._go_to_path(path)
        return HomePage(selenium)

    def go_to_level(self, level_name):
        path = reverse('play_default_level', kwargs={'levelName': str(level_name)})
        self._go_to_path(path)

        return GamePage(selenium)

    def go_to_custom_level(self, level):
        path = reverse('play_custom_level', kwargs={'levelId': str(level.id)})
        self._go_to_path(path)

        return GamePage(selenium)

    def go_to_episode(self, episodeId):
        path = reverse('start_episode', kwargs={'episodeId': str(episodeId)})
        self._go_to_path(path)

        return GamePage(selenium)

    def score_element_id(self, route_score, algorithm_score):
        if route_score:
            return "routeScore"
        elif algorithm_score:
            return "algorithmScore"
        else:
            raise Exception

    def run_episode_test(self, episode_id, level, suffix=None, route_score="10/10", algorithm_score="10/10", page=None):
        def go_to_episode():
            return self.go_to_episode(episode_id)

        self._run_level_test(go_to_episode, level, suffix, route_score, algorithm_score, page)

    def run_level_test(self, level, suffix=None, route_score="10/10", algorithm_score="10/10", page=None):
        def go_to_level():
            return self.go_to_level(level)

        self._run_level_test(go_to_level, level, suffix, route_score, algorithm_score, page)

    def _run_level_test(self, go_to_level_function, level, suffix, route_score, algorithm_score, page):
        level_with_suffix = str(level)
        if suffix:
            level_with_suffix += "-%d" % suffix

        user_profile = self.login_once()
        workspace_id = self.use_workspace_of_level(level_with_suffix, user_profile)
        score_element_id = self.score_element_id(route_score, algorithm_score)

        if not page:
            page = go_to_level_function()

        page.load_solution(workspace_id) \
            .run_program(score_element_id)

        if route_score:
            page.assert_route_score(route_score)

        if algorithm_score:
            page.assert_algorithm_score(algorithm_score)

    def run_crashing_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return self.go_to_level(level) \
            .load_solution(workspace_id) \
            .run_crashing_program()

    def running_out_of_instructions_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return self.go_to_level(level) \
            .load_solution(workspace_id) \
            .run_program_that_runs_out_of_instructions()

    def use_workspace_of_level(self, level, user_profile):
        workspace_filename = self.solution_filename_for_level(level)
        return self.use_workspace(workspace_filename, user_profile)

    def use_workspace(self, workspace_file, user_profile):
        solution = self.read_solution(workspace_file)
        workspace_id = Workspace.objects.create(name=workspace_file, owner=user_profile, contents=solution).id
        return workspace_id

    def login_once(self):
        if not BaseGameTest.already_logged_on:
            email, password = signup_teacher_directly()
            create_organisation_directly(email)
            self.go_to_homepage().go_to_teach_page().login(email, password)
            email = email
            BaseGameTest.user_profile = UserProfile.objects.get(user__email=email)

            BaseGameTest.already_logged_on = True

        return BaseGameTest.user_profile

    def solution_file_path(self, filename):
        return os.path.join(BaseGameTest.BLOCKLY_SOLUTIONS_DIR, filename + ".xml")

    def solution_filename_for_level(self, level):
        return "level_" + str(level)

    def read_solution(self, filename):
        path = self.solution_file_path(filename)
        if path:
            f = open(path, 'r')
            data = f.read()
            f.close()
        return data

    def _fixture_teardown(self):
        pass
