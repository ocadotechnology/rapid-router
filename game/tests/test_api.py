from django.urls import reverse
from hamcrest import *
from hamcrest.core.base_matcher import BaseMatcher
from rest_framework import status
from rest_framework.test import APITestCase

from game.character import get_all_character
from game.decor import get_all_decor
from game.tests.utils.locale import add_new_language
from game.theme import get_all_themes
from .utils.user import get_superuser


class APITests(APITestCase):
    def test_list_decors(self):
        url = reverse("decor-list")
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data, has_length(len(get_all_decor())))

    def test_known_decor_detail(self):
        decor_id = 1
        url = reverse("decor-detail", kwargs={"pk": decor_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data["id"], equal_to(decor_id))

    def test_unknown_decor_detail(self):
        decor_id = 0
        url = reverse("decor-detail", kwargs={"pk": decor_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_404_NOT_FOUND))

    def test_levels_for_known_episode(self):
        episode_id = 1
        url = reverse("level-for-episode", kwargs={"pk": episode_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data, has_length(greater_than(0)))

    def test_levels_for_unknown_episode(self):
        episode_id = 0
        url = reverse("level-for-episode", kwargs={"pk": episode_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data, has_length(0))

    def test_list_themes(self):
        url = reverse("theme-list")
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data, has_length(len(get_all_themes())))

    def test_known_theme_detail(self):
        theme_id = 1
        url = reverse("theme-detail", kwargs={"pk": theme_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data["id"], equal_to(theme_id))

    def test_unknown_theme_detail(self):
        theme_id = 0
        url = reverse("theme-detail", kwargs={"pk": theme_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_404_NOT_FOUND))

    def test_list_characters(self):
        url = reverse("character-list")
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data, has_length(len(get_all_character())))

    def test_known_character_detail(self):
        character_id = 1
        url = reverse("character-detail", kwargs={"pk": character_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data["id"], equal_to(character_id))

    def test_unknown_character_detail(self):
        character_id = 0
        url = reverse("character-detail", kwargs={"pk": character_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_404_NOT_FOUND))

    def test_list_episodes(self):
        url = reverse("episode-list")
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data[0]["name"], equal_to("Getting Started"))

    def test_list_episodes_with_translated_episode_names(self):
        with add_new_language():
            url = reverse("episode-list")
            superuser = get_superuser()
            self.client.force_authenticate(user=superuser)
            response = self.client.get(url, **{"HTTP_ACCEPT_LANGUAGE": "foo-br"})
            assert_that(response, has_status_code(status.HTTP_200_OK))
            assert_that(response.data[0]["name"], equal_to("crwdns4197:0crwdne4197:0"))

    def test_episode_details(self):
        episode_id = 1
        url = reverse("episode-detail", kwargs={"pk": episode_id})
        superuser = get_superuser()
        self.client.force_authenticate(user=superuser)
        response = self.client.get(url)
        assert_that(response, has_status_code(status.HTTP_200_OK))
        assert_that(response.data["name"], equal_to("Getting Started"))

    def test_episode_details_with_translated_episode_name(self):
        with add_new_language():
            episode_id = 1
            url = reverse("episode-detail", kwargs={"pk": episode_id})
            superuser = get_superuser()
            self.client.force_authenticate(user=superuser)
            response = self.client.get(url, **{"HTTP_ACCEPT_LANGUAGE": "foo-br"})
            assert_that(response, has_status_code(status.HTTP_200_OK))
            assert_that(response.data["name"], equal_to("crwdns4197:0crwdne4197:0"))


def has_status_code(status_code):
    return HasStatusCode(status_code)


class HasStatusCode(BaseMatcher):
    def __init__(self, status_code):
        self.status_code = status_code

    def _matches(self, response):
        return response.status_code == self.status_code

    def describe_to(self, description):
        description.append_text("has status code ").append_text(self.status_code)

    def describe_mismatch(self, response, mismatch_description):
        mismatch_description.append_text("had status code ").append_text(
            response.status_code
        )
