from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly, join_teacher_to_organisation
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from deploy import captcha
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse

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

        level = create_save_level(student, level_name)

        self.teacher_login(email, password)

        level_moderation_url = reverse("level_moderation")
        response = self.client.get(level_moderation_url)
        assert class_name in response.content.decode()
        assert level_name in response.content.decode()

        # Test delete level
        delete_level_url = reverse("delete_level", kwargs={"levelID": level.id})
        self.client.post(delete_level_url)
        response = self.client.get(level_moderation_url)
        assert level_name not in response.content.decode()

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

    def test_moderation_empty_class_filter(self):
        level_name = "test_level1"
        email, password = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email)

        _, _, student = create_school_student_directly(access_code)

        create_save_level(student, level_name)

        self.teacher_login(email, password)

        url = reverse("level_moderation")
        response = self.client.post(url, {"classes": []})
        assert class_name in response.content.decode()
        assert level_name not in response.content.decode()
        assert "No levels found." in response.content.decode()

    def test_moderation_shared_with(self):
        level_name = "test_level1"
        email, password = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email)

        _, _, student = create_school_student_directly(access_code)
        _, _, student2 = create_school_student_directly(access_code)

        create_save_level(student, level_name, shared_with=[student2.new_user])

        self.teacher_login(email, password)

        url = reverse("level_moderation")
        response = self.client.get(url)
        assert class_name in response.content.decode()
        assert level_name in response.content.decode()
        assert student2.new_user.first_name in response.content.decode()

    def test_moderation_admin(self):
        level_moderation_url = reverse("level_moderation")
        level1_name = "test_level_student1"
        level2_name = "test_level_student2"

        # Create 2 teachers in the same school, one admin, one standard
        email1, password1 = signup_teacher_directly()
        email2, password2 = signup_teacher_directly()
        school = create_organisation_directly(email1)
        join_teacher_to_organisation(email2, school.name)

        # Create one class and student for each teacher
        _, class_name1, access_code1 = create_class_directly(email1)
        _, class_name2, access_code2 = create_class_directly(email2)
        _, _, student1 = create_school_student_directly(access_code1)
        _, _, student2 = create_school_student_directly(access_code2)

        # Create one level for each student
        level1 = create_save_level(student1, level1_name)
        level2 = create_save_level(student2, level2_name)

        # Log in as teacher2, check they cannot see student1's level and cannot delete it
        self.teacher_login(email2, password2)
        response = self.client.get(level_moderation_url)
        assert class_name1 not in response.content.decode()
        assert class_name2 in response.content.decode()
        assert level1_name not in response.content.decode()
        assert level2_name in response.content.decode()
        assert student1.new_user.first_name not in response.content.decode()
        assert student2.new_user.first_name in response.content.decode()
        # Try to delete level1, it shouldn't work
        delete_level1_url = reverse("delete_level_for_editor", kwargs={"levelId": level1.id})
        response = self.client.get(delete_level1_url)
        assert response.status_code == 401
        # Check level2 is still there
        response = self.client.get(level_moderation_url)
        assert level2_name in response.content.decode()
        self.client.logout()

        # Log in as teacher1, check they can see student2's level and can delete it
        self.teacher_login(email1, password1)
        response = self.client.get(level_moderation_url)
        assert class_name1 in response.content.decode()
        assert class_name2 in response.content.decode()
        assert level1_name in response.content.decode()
        assert level2_name in response.content.decode()
        assert student1.new_user.first_name in response.content.decode()
        assert student2.new_user.first_name in response.content.decode()
        # Delete level2
        delete_level2_url = reverse("delete_level_for_editor", kwargs={"levelId": level2.id})
        response = self.client.get(delete_level2_url)
        assert response.status_code == 200
        # Check level1 is still there and level2 is not there anymore
        response = self.client.get(level_moderation_url)
        assert level1_name in response.content.decode()
        assert level2_name not in response.content.decode()
        self.client.logout()

    def teacher_login(self, email, password):
        self.client.post(
            reverse("teacher_login"),
            {"auth-username": email, "auth-password": password, "teacher_login_view-current_step": "auth"},
            follow=True,
        )
