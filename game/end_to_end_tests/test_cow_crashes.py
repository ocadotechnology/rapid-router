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
from game.end_to_end_tests.base_game_test import BaseGameTest
from game.models import Level, Block, LevelBlock

from game.theme import get_theme
from game.character import get_character


class TestCowCrashes(BaseGameTest):
    cow_level = None

    def test_crash_into_cow_going_forward(self):
        self.run_cow_crashing_test("crash_into_cow_going_forward")

    def test_crash_into_cow_turning_left(self):
        self.run_cow_crashing_test("crash_into_cow_turning_left")

    def test_crash_into_cow_turning_right(self):
        self.run_cow_crashing_test("crash_into_cow_turning_right")

    def test_crash_into_cow_on_t_junction(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction")

    def test_crash_into_cow_on_t_junction2(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction2")

    def test_crash_into_cow_on_t_junction3(self):
        self.run_cow_crashing_test("crash_into_cow_on_t_junction3")

    def test_crash_into_cow_on_crossroads_junction(self):
        self.run_cow_crashing_test("crash_into_cow_on_crossroads_junction")

    def run_cow_crashing_test(self, workspace_file):
        user_profile = self.login_once()
        TestCowCrashes.cow_level.owner = user_profile
        TestCowCrashes.cow_level.save()
        workspace_id = self.use_workspace(workspace_file, user_profile)
        self.go_to_custom_level(TestCowCrashes.cow_level) \
            .load_solution(workspace_id) \
            .run_cow_crashing_program()

    @classmethod
    def setUpClass(cls):
        BaseGameTest.setUpClass()
        grass = get_theme(name='grass')

        van = get_character('Van')

        TestCowCrashes.cow_level = Level(name='Cow crashing',
                                         anonymous=False,
                                         blocklyEnabled=True,
                                         character=van,
                                         cows='[{"minCows":"7","maxCows":"7","potentialCoordinates":[{"x":4,"y":4},{"x":2,"y":4},{"x":3,"y":7},{"x":4,"y":6},{"x":2,"y":6},{"x":3,"y":1},{"x":4,"y":2}],"type":"WHITE"}]',
                                         default=False,
                                         destinations='[[4,5]]',
                                         direct_drive=True,
                                         fuel_gauge=False,
                                         max_fuel=50,
                                         model_solution='[1]',
                                         origin='{"coordinate":[2,5],"direction":"E"}',
                                         path='[{"coordinate":[2,5],"connectedNodes":[1]},{"coordinate":[3,5],"connectedNodes":[0,4,2,5]},{"coordinate":[4,5],"connectedNodes":[1]},{"coordinate":[3,7],"connectedNodes":[4]},{"coordinate":[3,6],"connectedNodes":[8,3,6,1]},{"coordinate":[3,4],"connectedNodes":[10,1,11,16]},{"coordinate":[4,6],"connectedNodes":[4,7]},{"coordinate":[4,7],"connectedNodes":[6]},{"coordinate":[2,6],"connectedNodes":[9,4]},{"coordinate":[2,7],"connectedNodes":[8]},{"coordinate":[2,4],"connectedNodes":[13,5,12]},{"coordinate":[4,4],"connectedNodes":[5,14,15]},{"coordinate":[2,3],"connectedNodes":[10]},{"coordinate":[1,4],"connectedNodes":[10]},{"coordinate":[5,4],"connectedNodes":[11]},{"coordinate":[4,3],"connectedNodes":[11,19]},{"coordinate":[3,3],"connectedNodes":[5,17]},{"coordinate":[3,2],"connectedNodes":[18,16,19,20]},{"coordinate":[2,2],"connectedNodes":[17]},{"coordinate":[4,2],"connectedNodes":[17,15,23,22]},{"coordinate":[3,1],"connectedNodes":[21,17,22]},{"coordinate":[2,1],"connectedNodes":[20]},{"coordinate":[4,1],"connectedNodes":[20,19]},{"coordinate":[5,2],"connectedNodes":[19]}]',
                                         pythonEnabled=False,
                                         theme=grass,
                                         threads=1,
                                         traffic_lights='[]',
                                         )

        TestCowCrashes.cow_level.save()

        blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right"])

        for block in blocks:
            new_block = LevelBlock(type=block, number=None, level=TestCowCrashes.cow_level)
            new_block.save()
