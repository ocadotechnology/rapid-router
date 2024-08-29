import os
import socket
import time
from builtins import str

from common.models import UserProfile
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from django.urls import reverse
from portal.tests.pageObjects.portal.base_page import BasePage
from portal.tests.pageObjects.portal.home_page import HomePage

from game.models import Workspace
from . import custom_handler
from .editor_page import EditorPage
from .game_page import GamePage
from .selenium_test_case import SeleniumTestCase

custom_handler.monkey_patch()


class BaseGameTest(SeleniumTestCase):
    BLOCKLY_SOLUTIONS_DIR = os.path.join(
        os.path.dirname(__file__), "data/blockly_solutions"
    )

    already_logged_on = False
    user_profile = None

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

    def _complete_level(self, level_number, from_python_den=False, **kwargs):
        page = self.go_to_level(level_number, from_python_den)
        (self.complete_and_check_level(level_number, page, from_python_den, **kwargs))

    def complete_and_check_level(
        self,
        level_number,
        page,
        from_python_den=False,
        next_episode=None,
        redirects=False,
        check_algorithm_score=True,
        check_route_score=True,
        final_level=False,
    ):
        page.solution_button().run_program().assert_success()
        if check_algorithm_score:
            page.assert_algorithm_score(10)
        if check_route_score:
            if level_number < 13 and not from_python_den:
                page.assert_route_score(20)
            else:
                page.assert_route_score(10)
        if final_level:
            return page
        if next_episode is None:
            if redirects:
                page.next_level_redirected(from_python_den)
            else:
                page.next_level(from_python_den)
                page.assert_level_number(level_number + 1, from_python_den)
        else:
            page.next_episode()
            page.assert_episode_number(next_episode, from_python_den)
        return page

    def go_to_reverse(self, url_reverse):
        path = reverse(url_reverse)
        self._go_to_path(path)
        return BasePage(self.selenium)

    def go_to_homepage(self):
        path = reverse("home")
        self._go_to_path(path)
        return HomePage(self.selenium)

    def go_to_level(self, level_name, from_python_den=False):
        viewname = (
            "play_python_default_level" if from_python_den else "play_default_level"
        )

        path = reverse(viewname, kwargs={"level_name": str(level_name)})
        self._go_to_path(path)

        return GamePage(self.selenium)

    def go_to_level_without_dismissing_dialog(self, level_name, from_python_den=False):
        viewname = (
            "play_python_default_level" if from_python_den else "play_default_level"
        )

        path = reverse(viewname, kwargs={"level_name": str(level_name)})
        self._go_to_path(path)

        return BasePage(self.selenium)

    def go_to_custom_level(self, level):
        path = reverse("play_custom_level", kwargs={"levelId": str(level.id)})
        self._go_to_path(path)

        return GamePage(self.selenium)

    def go_to_level_editor(self):
        path = reverse("level_editor")
        self._go_to_path(path)
        return EditorPage(self.selenium)

    def go_to_episode(self, episodeId):
        if int(episodeId) > 9:
            path = reverse("start_python_episode", kwargs={"episodeId": str(episodeId)})
        else:
            path = reverse("start_episode", kwargs={"episodeId": str(episodeId)})
        self._go_to_path(path)

        return GamePage(self.selenium)

    def deliver_everywhere_test(self, level):
        self.login_once()

        return self.go_to_level(level).solution_button().run_program()

    def try_again_if_not_full_score_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return self.go_to_level(level).load_solution(workspace_id).run_retry_program()

    def run_crashing_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level).load_solution(workspace_id).run_crashing_program()
        )

    def run_animal_sound_horn_test(self, level):
        return self.go_to_custom_level(level).run_animal_sound_horn_program()

    def running_out_of_instructions_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level)
            .load_solution(workspace_id)
            .run_out_of_instructions_program()
        )

    def running_out_of_fuel_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level)
            .load_solution(workspace_id)
            .run_out_of_fuel_program()
        )

    def running_a_red_light_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level)
            .load_solution(workspace_id)
            .run_a_red_light_program()
        )

    def not_delivered_everywhere_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level)
            .load_solution(workspace_id)
            .run_not_delivered_everywhere_program()
        )

    def undefined_procedure_test(self, level, workspace_file):
        user_profile = self.login_once()

        workspace_id = self.use_workspace(workspace_file, user_profile)

        return (
            self.go_to_level(level)
            .load_solution(workspace_id)
            .run_undefined_procedure_program()
        )

    def use_workspace(self, workspace_file, user_profile):
        solution = self.read_solution(workspace_file)
        workspace_id = Workspace.objects.create(
            name=workspace_file, owner=user_profile, contents=solution
        ).id
        return workspace_id

    def login_once(self):
        if not BaseGameTest.already_logged_on:
            email, password = signup_teacher_directly()
            create_organisation_directly(email)
            klass, name, access_code = create_class_directly(email)
            create_school_student_directly(access_code)
            login_page = self.go_to_homepage().go_to_teacher_login_page()
            login_page.login(email, password)
            email = email
            BaseGameTest.user_profile = UserProfile.objects.get(user__email=email)

            BaseGameTest.already_logged_on = True

        return BaseGameTest.user_profile

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(BaseGameTest, cls).tearDownClass()
        BaseGameTest.user_profile = None
        BaseGameTest.already_logged_on = False

    def solution_file_path(self, filename):
        return os.path.join(BaseGameTest.BLOCKLY_SOLUTIONS_DIR, filename + ".xml")

    def read_solution(self, filename):
        path = self.solution_file_path(filename)
        if path:
            f = open(path, "r")
            data = f.read()
            f.close()
        return data

    def _fixture_teardown(self):
        pass
