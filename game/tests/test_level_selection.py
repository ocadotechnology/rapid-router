from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse
from hamcrest import *

from game.tests.utils.locale import add_new_language


class LevelSelectionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_episodes_with_translated_episode_names(self):
        with add_new_language():
            url = reverse("levels")
            response = self.client.get(url, **{"HTTP_ACCEPT_LANGUAGE": "foo-br"})

            assert_that(response.status_code, equal_to(200))
            self._assert_that_response_contains_episode_name(
                response, "crwdns4197:0crwdne4197:0"
            )
            self._assert_that_response_contains_level_with_title(
                response, "crwdns3456:0crwdne3456:0"
            )

    def test_list_episodes(self):
        url = reverse("levels")
        response = self.client.get(url)

        assert_that(response.status_code, equal_to(200))
        self._assert_that_response_contains_episode_name(response, "Getting Started")
        self._assert_that_response_contains_level_with_title(
            response, "Can you help the van get to the house? "
        )

    def _assert_that_response_contains_episode_name(self, response, expected):
        assert_that(response.context["episodeData"][0]["name"], equal_to(expected))

    def _assert_that_response_contains_level_with_title(self, response, expected):
        assert_that(
            response.context["episodeData"][0]["levels"][0]["title"], equal_to(expected)
        )
