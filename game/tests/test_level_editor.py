import json
from unittest.mock import patch

from common.models import Teacher, User
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from deploy import captcha
from django.core import mail
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse

from game.models import Level
from game.tests.utils.level import create_save_level, create_save_level_with_multiple_houses, multiple_house_data
from game.tests.utils.teacher import add_teacher_to_school, create_school


class LevelEditorTestCase(TestCase):
    LEVEL_DATA1 = {
        "origin": '{"coordinate":[3,5],"direction":"S"}',
        "python_enabled": False,
        "decor": [],
        "blockly_enabled": True,
        "blocks": [{"type": "move_forwards"}, {"type": "turn_left"}, {"type": "turn_right"}],
        "max_fuel": "50",
        "python_view_enabled": False,
        "character": "3",
        "name": "abc",
        "theme": 1,
        "anonymous": False,
        "cows": "[]",
        "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],' '"connectedNodes":[0]}]',
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
            {"auth-username": email, "auth-password": password, "teacher_login_view-current_step": "auth"},
            follow=True,
        )

    def logout(self):
        self.client.post(reverse("logout_view"), follow=True)

    def student_login(self, name, access_code, password):
        self.client.post(
            reverse("student_login", kwargs={"access_code": access_code}),
            {"username": name, "password": password},
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

        assert response.status_code == 200

        level = Level.objects.all().last()
        teacher_user = User.objects.get(email=email)

        assert level.needs_approval == True
        assert level.shared_with.count() == 1
        assert level.shared_with.filter(id=teacher_user.id).exists()
        assert len(mail.outbox) == 1

        level.needs_approval = False
        level.save()

        sharing_info1 = json.loads(self.get_sharing_information(json.loads(response.content)["id"]).getvalue())
        assert sharing_info1["teacher"]["shared"]

    def test_anonymous_level_saving_school_student(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data1 = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "python_enabled": False,
            "decor": [],
            "blockly_enabled": True,
            "blocks": [{"type": "move_forwards"}, {"type": "turn_left"}, {"type": "turn_right"}],
            "max_fuel": "50",
            "python_view_enabled": False,
            "character": "3",
            "name": "abc",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],' '"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data1)})

        level = Level.objects.all().last()
        level.needs_approval = False
        level.save()

        assert response.status_code == 200
        sharing_info1 = json.loads(self.get_sharing_information(json.loads(response.content)["id"]).getvalue())
        assert sharing_info1["teacher"]["shared"]
        assert len(mail.outbox) == 0

    def test_level_sharing_with_no_school(self):
        email1, password1 = signup_teacher_directly()
        teacher1 = Teacher.objects.get(new_user__email=email1)
        self.login(email1, password1)
        level = create_save_level(teacher1)

        sharing_info1 = json.loads(self.get_sharing_information(level.id).getvalue())
        assert len(sharing_info1["teachers"]) == 0

    def test_level_sharing_with_school(self):
        email1, password1 = signup_teacher_directly()
        email2, _ = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        self.login(email1, password1)
        level = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)
        add_teacher_to_school(teacher2, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level.id).getvalue())
        assert len(sharing_info1["teachers"]) == 1

    def test_level_sharing_with_empty_school(self):
        email1, password1 = signup_teacher_directly()
        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)
        level = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level.id).getvalue())
        assert len(sharing_info1["teachers"]) == 0

    def test_level_sharing_permissions(self):
        email1, password1 = signup_teacher_directly()
        email2, password2 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        self.login(email1, password1)
        level = create_save_level(teacher1)
        share_url = reverse("share_level_for_editor", args=[level.id])

        school1 = create_school()
        add_teacher_to_school(teacher1, school1, is_admin=True)
        add_teacher_to_school(teacher2, school1)

        # Create a class and 2 students for the second teacher
        _, class_name2, access_code2 = create_class_directly(email2)
        student_name1, student_password1, student1 = create_school_student_directly(access_code2)
        student_name2, student_password2, student2 = create_school_student_directly(access_code2)

        self.logout()
        self.login(email2, password2)

        # Second teacher can't share the level as it's not been shared with them yet
        response = self.client.post(share_url, {"recipientIDs[]": [student1.new_user.id], "action": ["share"]})
        assert response.status_code == 403

        # Log in as the first teacher again
        self.logout()
        self.login(email1, password1)

        # Share the level with the second teacher
        response = self.client.post(share_url, {"recipientIDs[]": [teacher2.new_user.id], "action": ["share"]})
        assert response.status_code == 200

        # Log in as the second teacher
        self.logout()
        self.login(email2, password2)

        # Now the second teacher should be able to share the level
        response = self.client.post(share_url, {"recipientIDs[]": [student1.new_user.id], "action": ["share"]})
        assert response.status_code == 200
        # and load it
        load_level_url = reverse("load_level_for_editor", kwargs={"levelID": level.id})
        response = self.client.get(load_level_url)
        assert response.status_code == 200

        # Log in as the first student
        self.logout()
        self.student_login(student_name1, access_code2, student_password1)

        # Check that the student cannot share the level
        sharing_info = json.loads(self.get_sharing_information(level.id).getvalue())
        assert sharing_info["detail"] == "You do not have permission to perform this action."

        # Check the student can view the level
        response = self.client.get(reverse("play_custom_level", args=[level.id]))
        assert response.status_code == 200

        # Log in as first teacher again
        self.logout()
        self.login(email1, password1)

        # Share the level with the second student of teacher 2
        response = self.client.post(share_url, {"recipientIDs[]": [student2.new_user.id], "action": ["share"]})
        assert response.status_code == 200

        # Log in as the second student
        self.logout()
        self.student_login(student_name2, access_code2, student_password2)

        # Check that the student cannot share the level
        sharing_info = json.loads(self.get_sharing_information(level.id).getvalue())
        assert sharing_info["detail"] == "You do not have permission to perform this action."

        # Check the student can view the level
        response = self.client.get(reverse("play_custom_level", args=[level.id]))
        assert response.status_code == 200

        self.logout()

    def test_level_can_only_be_edited_by_owner(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, _, access_code = create_class_directly(email)
        student_name, student_password, student = create_school_student_directly(access_code)
        hacker_name, hacker_password, hacker = create_school_student_directly(access_code)

        new_level = Level.objects.create(owner_id=student.user_id, name="my_custom_level")

        self.student_login(hacker_name, access_code, hacker_password)
        resp = self.client.get(reverse("level_editor_chosen_level", kwargs={"levelId": new_level.id}))

        assert "level" not in resp.context

        self.logout()

        self.student_login(student_name, access_code, student_password)
        resp = self.client.get(reverse("level_editor_chosen_level", kwargs={"levelId": new_level.id}))

        assert "level" in resp.context

    def test_no_character_set_defaults_to_van(self):

        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data_with_no_character = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "python_enabled": False,
            "decor": [],
            "blockly_enabled": True,
            "blocks": [{"type": "move_forwards"}, {"type": "turn_left"}, {"type": "turn_right"}],
            "max_fuel": "50",
            "python_view_enabled": False,
            "name": "abc",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],' '"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data_with_no_character)})

        assert response.status_code == 200
        new_level = Level.objects.get(name="abc")
        assert new_level.character.name == "Van"

    def test_language_set_appropriately(self):

        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data_with_split_language = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "python_enabled": False,
            "decor": [],
            "blockly_enabled": True,
            "blocks": [
                {"type": "move_forwards"},
                {"type": "turn_left"},
                {"type": "turn_right"},
            ],
            "max_fuel": "50",
            "python_view_enabled": True,
            "name": "abc",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
            '"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data_with_split_language)})

        assert response.status_code == 200
        new_level = Level.objects.get(name="abc")

        assert new_level.python_view_enabled
        assert not new_level.python_enabled
        assert new_level.blockly_enabled

    def test_level_loading(self):
        email1, password1 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)
        level = create_save_level(teacher1)
        url = reverse("load_level_for_editor", kwargs={"levelID": level.id})
        response = self.client.get(url)

        assert response.status_code == 200

    def test_level_saving_with_multiple_houses(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data_with_multiple_houses = {
            "origin": '{"coordinate":[3,5],"direction":"S"}',
            "python_enabled": False,
            "decor": [],
            "blockly_enabled": True,
            "blocks": [{"type": "move_forwards"}, {"type": "turn_left"}, {"type": "turn_right"}],
            "max_fuel": "50",
            "python_view_enabled": False,
            "name": "multiple_houses",
            "theme": 1,
            "anonymous": True,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0,2]}, {"coordinate":[3,3],"connectedNodes":[1]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4],[3,3]]",
        }
        response = self.client.post(url, {"data": json.dumps(data_with_multiple_houses)})

        assert response.status_code == 200
        new_level = Level.objects.get(name="multiple_houses")
        assert new_level.destinations == "[[3,4],[3,3]]"

    def test_level_loading_with_multiple_houses(self):

        email1, password1 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)
        level = create_save_level_with_multiple_houses(teacher1)
        url = reverse("load_level_for_editor", kwargs={"levelID": level.id})
        response = self.client.get(url)
        response_data = response.json()

        assert response.status_code == 200
        assert response_data["level"]["destinations"] == "[[3,4], [3,3]]"

    @patch("game.level_management.save_level")
    def test_custom_level_scoring(self, mock_save_level):
        email1, password1 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)

        self.login(email1, password1)

        level = create_save_level_with_multiple_houses(teacher1)

        save_url = reverse("save_level_for_editor", kwargs={"levelId": level.id})
        response = self.client.post(save_url, {"data": json.dumps(multiple_house_data)})

        disable_algorithm_score = mock_save_level.call_args.args[1]["disable_algorithm_score"]

        assert response.status_code == 200
        assert disable_algorithm_score

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
        assert len(response.context["directly_shared_levels"]) == 1

        # Make teacher2 inactive
        teacher2.new_user.is_active = 0
        teacher2.new_user.save()

        # `teacher1` shouldn't see any shared levels now
        response = self.client.get(levels_url)
        assert len(response.context["directly_shared_levels"]) == 0

    def test_level_of_anonymised_student_is_hidden(self):
        # Create a teacher and a student
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, _, access_code = create_class_directly(email)
        student_name, student_password, student = create_school_student_directly(access_code)

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
        assert len(response.context["directly_shared_levels"]) == 1

        # Make student inactive
        student.new_user.is_active = 0
        student.new_user.save()

        # Teacher shouldn't see any shared levels now
        response = self.client.get(levels_url)
        assert len(response.context["directly_shared_levels"]) == 0
