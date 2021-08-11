# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2021, Ocado Innovation Limited
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

from django.urls.base import reverse
from .base_game_test import BaseGameTest
from selenium.webdriver.common.by import By


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def items(self):
        items = self.driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; "
        )
        return items

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

class TestLocalStorage(BaseGameTest):
    def level_in_localstorage(self, level_number):
        items = LocalStorage(self.selenium).items()
        return (f"blocklyWorkspaceXml-{level_number}" in items) and (
            f"pythonWorkspace-{level_number}" in items
        )

    def test_localstorage_if_logged_in(self):
        self.login_once()
        self._complete_level(1)
        self.assertTrue(self.level_in_localstorage(1))

    def test_nothing_in_localstorage_if_not_logged_in(self):
        page = self.go_to_homepage()
        page.teacher_logout()

        level1 = self.go_to_level(1)

        ls = LocalStorage(self.selenium)
        ls.clear()

        solution = self.read_solution("once_forwards")
        script = f"""
            const xml = `{solution}`;
            Blockly.Xml.clearWorkspaceAndLoadFromXml(Blockly.Xml.textToDom(xml), Blockly.mainWorkspace);
            """
        self.selenium.execute_script(script)
        self.selenium.find_element_by_id("fast_tab").click()

        level1.wait_for_element_to_be_clickable((By.CSS_SELECTOR, "#next_level_button"))
        level1.next_level()
        self.assertFalse(self.level_in_localstorage(1))
