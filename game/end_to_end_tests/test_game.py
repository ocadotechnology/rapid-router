# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Limited
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

from portal.models import UserProfile
from game.models import Workspace
from portal.tests.base_test import BaseTest
from portal.tests.utils.organisation import create_organisation_directly
from portal.tests.utils.teacher import signup_teacher_directly

class TestGame(BaseTest):

    already_logged_on = False

    def test_level1(self):
        self.run_level_test(1)

    def test_level2(self):
        self.run_level_test(2)

    def test_level3(self):
        self.run_level_test(3)

    def test_level4(self):
        self.run_level_test(4)

    def test_level5(self):
        self.run_level_test(5)

    def test_level6(self):
        self.run_level_test(6)

    def test_level7(self):
        self.run_level_test(7)

    def test_level8(self):
        self.run_level_test(8)

    def test_level9(self):
        self.run_level_test(9)

    def test_level10(self):
        self.run_level_test(10)

    def test_level11(self):
        self.run_level_test(11)

    def test_level12(self):
        self.run_level_test(12)

    def test_level13(self):
        self.run_level_test(13)

    def test_level14(self):
        self.run_level_test(14)

    def test_level15(self):
        self.run_level_test(15)

    def test_level16(self):
        self.run_level_test(16)

    def test_level17(self):
        self.run_level_test(17)

    def test_level18(self):
        self.run_level_test(18)

    def test_level19(self):
        self.run_level_test(19)

    def test_level20(self):
        self.run_level_test(20)

    def test_level21(self):
        self.run_level_test(21)

    def run_level_test(self, level):
        user_profile = self.login_once()

        workspace_id = self.persist_workspace(level, user_profile)

        self .go_to_level(level) \
            .load_solution(workspace_id) \
            .run_program() \
            .assert_route_score("10/10") \
            .assert_algorithm_score("10/10")

    def persist_workspace(self, level, user_profile):
        solution = self.read_solution(level)
        workspace_name = "Level " + str(level)
        workspace_id = Workspace.objects.create(name=workspace_name, owner=user_profile, contents=solution).id
        return workspace_id

    def login_once(self):
        if not TestGame.already_logged_on:
            email, password = signup_teacher_directly()
            create_organisation_directly(email)
            self.go_to_homepage().go_to_teach_page().login(email, password)
            email = email
            TestGame.user_profile = UserProfile.objects.get(user__email=email)

            TestGame.already_logged_on = True

        return TestGame.user_profile

    BLOCKLY_SOLUTIONS_DIR = os.path.join(os.path.dirname(__file__), 'data/blockly_solutions')

    def datafile(self, filename):
        return os.path.join(TestGame.BLOCKLY_SOLUTIONS_DIR, filename)

    def read_solution(self, level):
        filename = self.datafile("level_" + str(level) + ".xml")
        if filename:
            f = open(filename, 'r')
            data = f.read()
            f.close()

        return data

    def _fixture_teardown(self):
        pass
