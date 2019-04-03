# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
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
from .test_play_through import complete_and_check_level


class TestCrashes(BaseGameTest):
    def test_crash_turning_left_on_straight_road(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_left_on_straight_road"
        )

    def test_crash_turning_left_on_right_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_left_on_right_turn"
        )

    def test_crash_turning_right_on_straight_road(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_right_on_straight_road"
        )

    def test_crash_turning_right_on_left_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_turning_right_on_left_turn"
        )

    def test_crash_going_forward_on_right_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_going_forward_on_right_turn"
        )

    def test_crash_going_forward_on_left_turn(self):
        self.run_crashing_test(
            level=6, workspace_file="crash_going_forward_on_left_turn"
        )

    def test_crash_going_forward_on_t_junction(self):
        self.run_crashing_test(
            level=13, workspace_file="crash_going_forward_on_t_junction"
        )

    def test_crash_going_left_on_t_junction(self):
        self.run_crashing_test(
            level=40, workspace_file="crash_going_left_on_t_junction"
        )

    def test_crash_going_right_on_t_junction(self):
        self.run_crashing_test(
            level=40, workspace_file="crash_going_right_on_t_junction"
        )

    def test_running_out_of_instructions(self):
        self.running_out_of_instructions_test(
            level=6, workspace_file="running_out_of_instructions"
        )

    def test_running_out_of_fuel(self):
        self.running_out_of_fuel_test(level=68, workspace_file="running_out_of_fuel")

    def test_running_a_red_light(self):
        self.running_a_red_light_test(level=44, workspace_file="running_a_red_light")

    def test_not_delivered_everywhere(self):
        self.not_delivered_everywhere_test(
            level=16, workspace_file="not_delivered_everywhere"
        )

    def test_procedure_undefined(self):
        self.undefined_procedure_test(level=63, workspace_file="undefined_procedure")

    def test_crash_turning_left_clear_and_pass_level(self):
        page = (
            self.run_crashing_test(
                level=6, workspace_file="crash_turning_left_on_straight_road"
            )
            .try_again()
            .clear()
        )

        complete_and_check_level(6, page)
