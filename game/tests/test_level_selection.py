# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2018, Ocado Innovation Limited
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
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.test.testcases import TestCase
from django.test.client import Client

from hamcrest import *

from game.tests.utils.locale import add_new_language


class LevelSelectionTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_episodes_with_translated_episode_names(self):
        cache.clear()
        with add_new_language():
            url = reverse('levels')
            response = self.client.get(url, **{'HTTP_ACCEPT_LANGUAGE': 'foo-br'})

            assert_that(response.status_code, equal_to(200))
            self._assert_that_response_contains_episode_name(response, 'crwdns4197:0crwdne4197:0')

    def test_list_episodes(self):
        url = reverse('levels')
        response = self.client.get(url)

        assert_that(response.status_code, equal_to(200))
        self._assert_that_response_contains_episode_name(response, 'Getting Started')

    def _assert_that_response_contains_episode_name(self, response, expected):
        assert_that(response.context['episodeData'][0]['name'], equal_to(expected))
