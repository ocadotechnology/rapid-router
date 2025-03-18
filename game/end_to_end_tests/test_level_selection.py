from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from hamcrest import assert_that, ends_with, equal_to
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from game.end_to_end_tests.base_game_test import BaseGameTest
from game.models import Attempt, Episode


class TestLevelSelection(BaseGameTest):
    def test_coins(self):

        # Set up student
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        klass, name, access_code = create_class_directly(email)
        name, password, student = create_school_student_directly(access_code)

        # Student has perfect score for each level in an episode
        episode = Episode.objects.get(name="Loops with Conditions")
        for a_level in episode.levels:
            attempt = Attempt(student=student, score=20.0, level=a_level)
            attempt.save()

        #  Student logs in
        code_page = self.go_to_homepage().go_to_student_login_page()
        student_login_page = code_page.student_input_access_code(access_code)
        page = student_login_page.student_login(name, password)

        # Goes to rapid router levels
        page = self.go_to_reverse("levels")

        # The coin images for the levels
        level_coin_images = page.browser.find_elements(
            By.CSS_SELECTOR, ("#collapse-4 div img")
        )
        # There are 4 levels in this episode, each with gold coin
        assert_that(len(level_coin_images), equal_to(4))

        for image in level_coin_images:
            assert_that(
                image.get_attribute("src"),
                ends_with("/static/game/image/coins/coin_gold.svg"),
            )

        # So the episode has a gold coin too
        episode_coin_image = page.browser.find_element(
            By.CSS_SELECTOR, "#episode-4 > p > img"
        )
        assert_that(
            episode_coin_image.get_attribute("src"),
            ends_with("/static/game/image/coins/coin_gold.svg"),
        )

        try:
            image_for_uncomplete_episode = page.browser.find_element(
                By.CSS_SELECTOR, "#episode-3 > p > img"
            )
        except NoSuchElementException as this_should_happen:
            pass

    def test_redirect_to_levelless_episode(self):
        levels_page = self.go_to_reverse("python_levels")
        expected_url = levels_page.browser.current_url

        page = self.go_to_level_without_dismissing_dialog(26, True)
        self.selenium.find_element(By.ID, "next_button").click()

        current_url = page.browser.current_url
        assert current_url == expected_url

        episode_20_header = self.selenium.find_element(By.ID, "collapse-20")
        episode_20_expanded = episode_20_header.get_attribute("class")
        assert episode_20_expanded == "collapse"
