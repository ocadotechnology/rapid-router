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
from .utils.level import create_save_level


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

        _, _, student = create_school_student_directly(access_code)

        create_save_level(student, level_name)

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

        _, _, student = create_school_student_directly(access_code)

        create_save_level(student, level_name)

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
