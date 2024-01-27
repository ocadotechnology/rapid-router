import socket
import time
from builtins import str

from common.models import UserProfile
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from django.urls import reverse
from portal.tests.pageObjects.portal.home_page import HomePage

from . import custom_handler
from .game_page import GamePage
from .selenium_test_case import SeleniumTestCase
import random
import string

custom_handler.monkey_patch()

class TestSavingGame(SeleniumTestCase):
    already_logged_on = False
    user_profile = None

    def test_logging_in(self):
        self.login_once()
        level = 10
        random_save_entry_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return self.go_to_level(level).save_solution(random_save_entry_name).load_solution_by_name(random_save_entry_name)

    def _go_to_path(self, path):
        socket.setdefaulttimeout(20)
        attempts = 0
        while True:
            try:
                self.selenium.get(self.live_server_url + path)
            except socket.timeout:
                attempts += 1
                if attempts > 2:
                    raise
                time.sleep(10)
            else:
                break

    def go_to_level(self, level_name):
        path = reverse("play_default_level", kwargs={"levelName": str(level_name)})
        self._go_to_path(path)
        self.selenium.execute_script("ocargo.animation.FAST_ANIMATION_DURATION = 1;")

        return GamePage(self.selenium)

    def login_once(self):
        if not TestSavingGame.already_logged_on:
            email, password = signup_teacher_directly()
            create_organisation_directly(email)
            klass, name, access_code = create_class_directly(email)
            create_school_student_directly(access_code)
            login_page = self.go_to_homepage().go_to_teacher_login_page()
            login_page.login(email, password)
            email = email
            TestSavingGame.user_profile = UserProfile.objects.get(user__email=email)

            TestSavingGame.already_logged_on = True

        return TestSavingGame.user_profile

    def go_to_homepage(self):
        path = reverse("home")
        self._go_to_path(path)
        return HomePage(self.selenium)