from common.tests.utils.classes import create_class_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from deploy import captcha
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse
from hamcrest import *


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
        email, password = signup_teacher_directly()
        klass, name, access_code = create_class_directly(email)

        student_name, _, student = create_school_student_directly(access_code)

        self.login(email, password)
        response = self.students_of_class(klass)
        assert_that(response.status_code, equal_to(200))
        assert_that(
            response.content.decode(),
            equal_to('{"%s": "%s"}' % (student.id, student_name)),
        )

    def test_moderation_another_class(self):
        email, password = signup_teacher_directly()

        email2, _ = signup_teacher_directly()
        klass2, _, access_code = create_class_directly(email2)

        student_name, _, student = create_school_student_directly(access_code)

        self.login(email, password)
        response = self.students_of_class(klass2)
        assert_that(response.status_code, equal_to(404))
        assert_that(response.content, empty)

    def students_of_class(self, klass):
        url = reverse("students_for_level_moderation", args=[klass.id])
        response = self.client.get(url)
        return response

    def login(self, email, password):
        self.client.post(
            reverse("teacher_login"),
            {
                "auth-username": email,
                "auth-password": password,
                "teacher_login_view-current_step": "auth",
            },
            follow=True,
        )
