import json

from common.models import Teacher
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from game.models import Level
from deploy import captcha
from django.core import mail
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse
from hamcrest import assert_that, equal_to

from game.tests.utils.level import create_save_level
from game.tests.utils.teacher import add_teacher_to_school, create_school


class LevelEditorTestCase(TestCase):
    LEVEL_DATA1 = {
        "origin": '{"coordinate":[3,5],"direction":"S"}',
        "pythonEnabled": False,
        "decor": [],
        "blocklyEnabled": True,
        "blocks": [
            {"type": "move_forwards"},
            {"type": "turn_left"},
            {"type": "turn_right"},
        ],
        "max_fuel": "50",
        "pythonViewEnabled": False,
        "character": "3",
        "name": "abc",
        "theme": 1,
        "anonymous": False,
        "cows": "[]",
        "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
        '"connectedNodes":[0]}]',
        "traffic_lights": "[]",
        "destinations": "[[3,4]]",
    }

    @classmethod
    def setUpClass(cls):
        cls.orig_captcha_enabled = captcha.CAPTCHA_ENABLED
        captcha.CAPTCHA_ENABLED = False
        super(LevelEditorTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        captcha.CAPTCHA_ENABLED = cls.orig_captcha_enabled
        super(LevelEditorTestCase, cls).tearDownClass()

    def setUp(self):
        self.client = Client()

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

    def get_sharing_information(self, level_id):
        url = reverse("get_sharing_information_for_editor", args=[level_id])
        response = self.client.get(url)
        return response

    def share_level_for_editor(self, level_id):
        url = reverse("share_level_for_editor", args=[level_id])
        response = self.client.post(url)
        return response

    def test_level_saving_school_student(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        response = self.client.post(url, {"data": json.dumps(self.LEVEL_DATA1)})

        assert_that(response.status_code, equal_to(200))
        sharing_info1 = json.loads(
            self.get_sharing_information(json.loads(response.content)["id"]).getvalue()
        )
        assert_that(sharing_info1["teacher"]["shared"], equal_to(True))
        assert_that(len(mail.outbox), equal_to(1))

    def test_anonymous_level_saving_school_student(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data1 = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "pythonEnabled": False,
            "decor": [],
            "blocklyEnabled": True,
            "blocks": [
                {"type": "move_forwards"},
                {"type": "turn_left"},
                {"type": "turn_right"},
            ],
            "max_fuel": "50",
            "pythonViewEnabled": False,
            "character": "3",
            "name": "abc",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
            '"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data1)})

        assert_that(response.status_code, equal_to(200))
        sharing_info1 = json.loads(
            self.get_sharing_information(json.loads(response.content)["id"]).getvalue()
        )
        assert_that(sharing_info1["teacher"]["shared"], equal_to(True))
        assert_that(len(mail.outbox), equal_to(0))

    def test_level_sharing_with_no_school(self):
        email1, password1 = signup_teacher_directly()
        teacher1 = Teacher.objects.get(new_user__email=email1)
        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(0))

    def test_level_sharing_with_school(self):
        email1, password1 = signup_teacher_directly()
        email2, _ = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)
        add_teacher_to_school(teacher2, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(1))

    def test_level_sharing_with_empty_school(self):
        email1, password1 = signup_teacher_directly()
        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(0))

    def test_level_can_only_be_shared_by_owner(self):
        email1, password1 = signup_teacher_directly()
        email2, password2 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)

        self.logout()
        self.login(email2, password2)

        url = reverse("share_level_for_editor", args=[level_id])
        data = {"recipientIDs[]": [teacher2.id], "action": ["share"]}
        response = self.client.post(url, {"data": data})

        assert_that(response.status_code, equal_to(403))

    def test_level_can_only_be_edited_by_owner(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, _, access_code = create_class_directly(email)
        student_name, student_password, student = create_school_student_directly(
            access_code
        )
        hacker_name, hacker_password, hacker = create_school_student_directly(
            access_code
        )

        new_level = Level.objects.create(
            owner_id=student.user_id, name="my_custom_level"
        )

        self.student_login(hacker_name, access_code, hacker_password)
        resp = self.client.get(
            reverse("level_editor_chosen_level", kwargs={"levelId": new_level.id})
        )

        self.assertNotIn("level", resp.context)

        self.logout()

        self.student_login(student_name, access_code, student_password)
        resp = self.client.get(
            reverse("level_editor_chosen_level", kwargs={"levelId": new_level.id})
        )

        self.assertIn("level", resp.context)

    def test_no_character_set_defaults_to_van(self):

        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data_with_no_character = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "pythonEnabled": False,
            "decor": [],
            "blocklyEnabled": True,
            "blocks": [
                {"type": "move_forwards"},
                {"type": "turn_left"},
                {"type": "turn_right"},
            ],
            "max_fuel": "50",
            "pythonViewEnabled": False,
            "name": "abc",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
            '"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data_with_no_character)})

        assert_that(response.status_code, equal_to(200))
        new_level = Level.objects.get(name="abc")
        assert_that(new_level.character.name, equal_to("Van"))

    def test_level_loading(self):
        email1, password1 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)
        level_id = create_save_level(teacher1)
        url = reverse("load_level_for_editor", kwargs={"levelID": level_id})
        response = self.client.get(url)

        assert_that(response.status_code, equal_to(200))

    def test_level_of_anonymised_teacher_is_hidden(self):
        # Create 2 teacher accounts
        email1, password1 = signup_teacher_directly()
        email2, password2 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        # Add teachers to the same school
        school = create_school()
        add_teacher_to_school(teacher1, school)
        add_teacher_to_school(teacher2, school)

        # Create a level as `teacher2` and share it with `teacher1`
        self.login(email2, password2)
        create_save_level(teacher2, shared_with=[teacher1.new_user])

        # Log in as `teacher1`
        self.logout()
        self.login(email1, password1)

        # Check `teacher1` can see `teacher2`'s shared level
        levels_url = reverse("levels")
        response = self.client.get(levels_url)
        assert len(response.context["shared_levels"]) == 1

        # Make teacher2 inactive
        teacher2.new_user.is_active = 0
        teacher2.new_user.save()

        # `teacher1` shouldn't see any shared levels now
        response = self.client.get(levels_url)
        assert len(response.context["shared_levels"]) == 0

    def test_level_of_anonymised_student_is_hidden(self):
        # Create a teacher and a student
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, _, access_code = create_class_directly(email)
        student_name, student_password, student = create_school_student_directly(
            access_code
        )

        teacher = Teacher.objects.get(new_user__email=email)

        # Create a level as student and share it with teacher
        self.student_login(student_name, access_code, student_password)
        create_save_level(student, shared_with=[teacher.new_user])

        # Log in as teacher
        self.logout()
        self.login(email, password)

        # Check teacher can see student's shared level
        levels_url = reverse("levels")
        response = self.client.get(levels_url)
        assert len(response.context["shared_levels"]) == 1

        # Make student inactive
        student.new_user.is_active = 0
        student.new_user.save()

        # Teacher shouldn't see any shared levels now
        response = self.client.get(levels_url)
        assert len(response.context["shared_levels"]) == 0
