import json

from common.tests.utils.classes import create_class_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from deploy import captcha
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse
from hamcrest import *

from .test_level_editor import LevelEditorTestCase


class LevelModerationTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orig_captcha_enabled = captcha.CAPTCHA_ENABLED
        captcha.CAPTCHA_ENABLED = False
        super(LevelModerationTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        captcha.CAPTCHA_ENABLED = cls.orig_captcha_enabled
        super(LevelModerationTestCase, cls).tearDownClass()

    def setUp(self):
        self.client = Client()

    def test_moderation_teachers_class(self):
        level_name = "test_level1"
        email, password = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email)

        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        self.create_custom_level(level_name=level_name)

        self.logout()

        self.teacher_login(email, password)

        url = reverse("level_moderation")
        response = self.client.get(url)
        assert class_name in response.content.decode()
        assert level_name in response.content.decode()

    def test_moderation_another_class(self):
        level_name = "test_level2"
        email, password = signup_teacher_directly()

        email2, _ = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email2)

        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        self.create_custom_level(level_name=level_name)

        self.logout()

        self.teacher_login(email, password)

        url = reverse("level_moderation")
        response = self.client.get(url)
        assert class_name not in response.content.decode()
        assert level_name not in response.content.decode()

    def teacher_login(self, email, password):
        self.client.post(
            reverse("teacher_login"),
            {
                "auth-username": email,
                "auth-password": password,
                "teacher_login_view-current_step": "auth",
            },
            follow=True,
        )

    def logout(self):
        self.client.post(reverse("logout_view"), follow=True)

    def student_login(self, name, access_code, password):
        self.client.post(
            reverse("student_login", kwargs={"access_code": access_code}),
            {
                "username": name,
                "password": password,
            },
            follow=True,
        )

    def create_custom_level(self, level_name):
        url = reverse("save_level_for_editor")
        level_data = LevelEditorTestCase.LEVEL_DATA1
        level_data["name"] = level_name
        response = self.client.post(url, {"data": json.dumps(level_data)})
        assert_that(response.status_code, equal_to(200))
