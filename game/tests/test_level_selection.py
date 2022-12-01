import json

from common.models import Teacher
from common.tests.utils.classes import create_class_directly
from common.tests.utils.student import create_school_student_directly
from common.tests.utils.teacher import signup_teacher_directly
from deploy import captcha
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse

from game.models import Level
from game.permissions import can_play_level
from game.tests.utils.level import create_save_level
from game.tests.utils.teacher import add_teacher_to_school, create_school
from game.views.level import _next_level_url, _prev_level_url


class LevelSelectionTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orig_captcha_enabled = captcha.CAPTCHA_ENABLED
        captcha.CAPTCHA_ENABLED = False
        super(LevelSelectionTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        captcha.CAPTCHA_ENABLED = cls.orig_captcha_enabled
        super(LevelSelectionTestCase, cls).tearDownClass()

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
            {"username": name, "password": password},
            follow=True,
        )

    def level_data(self, levelID):
        data = {
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
            "name": f"level{levelID}",
            "theme": 1,
            "anonymous": False,
            "cows": "[]",
            "path": '[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],"connectedNodes":[0]}]',
            "traffic_lights": "[]",
            "destinations": "[[3,4]]",
        }
        return json.dumps(data)

    def test_list_episodes(self):
        url = reverse("levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.context["blocklyEpisodes"][0]["name"] == "Getting Started"
        assert (
            response.context["blocklyEpisodes"][0]["levels"][0]["title"]
            == "Can you help the van get to the house?"
        )

    def test_custom_levels_access(self):
        email1, password1 = signup_teacher_directly()
        email2, password2 = signup_teacher_directly()

        teacher1 = Teacher.objects.get(new_user__email=email1)
        teacher2 = Teacher.objects.get(new_user__email=email2)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1, is_admin=True)
        add_teacher_to_school(teacher2, school1)

        # Create a class and a student for each teacher
        _, class_name1, access_code1 = create_class_directly(email1)
        _, class_name2, access_code2 = create_class_directly(email2)
        student_name1, student_password1, student1 = create_school_student_directly(
            access_code1
        )
        student_name2, student_password2, student2 = create_school_student_directly(
            access_code2
        )

        save_url = "save_level_for_editor"

        # Login as the second teacher
        self.login(email2, password2)
        teacher2_level = create_save_level(teacher2)
        save_level_url = reverse(save_url)

        response = self.client.post(
            save_level_url, {"data": self.level_data(teacher2_level.id)}
        )

        assert response.status_code == 200

        # Login as the first student
        self.logout()
        self.student_login(student_name1, access_code1, student_password1)

        student1_level = create_save_level(student1)

        response = self.client.post(
            save_level_url, {"data": self.level_data(student1_level.id)}
        )

        assert response.status_code == 200

        # Login as the second student
        self.logout()
        self.student_login(student_name2, access_code2, student_password2)

        student2_level = create_save_level(student2)

        response = self.client.post(
            save_level_url, {"data": self.level_data(student2_level.id)}
        )

        assert response.status_code == 200

        # Login as first teacher again and check they have access to all the levels created above
        self.logout()
        self.login(email1, password1)

        url = reverse("levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.context["directly_shared_levels"]) == 1
        assert (
            response.context["directly_shared_levels"][0]["owner"] == student1.new_user
        )
        assert response.context["indirectly_shared_levels"][teacher2.new_user]
        assert len(response.context["indirectly_shared_levels"][teacher2.new_user]) == 2
        assert (
            response.context["indirectly_shared_levels"][teacher2.new_user][0]["owner"]
            == teacher2.new_user
        )
        assert (
            response.context["indirectly_shared_levels"][teacher2.new_user][1]["owner"]
            == student2.new_user
        )

        # Login as second teacher again and check they have access to only their student's level
        self.logout()
        self.login(email2, password2)

        url = reverse("levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.context["directly_shared_levels"]) == 1
        assert (
            response.context["directly_shared_levels"][0]["owner"] == student2.new_user
        )
        assert response.context["indirectly_shared_levels"] == {}

    def test_cannot_access_locked_level(self):
        email, password = signup_teacher_directly()

        teacher = Teacher.objects.get(new_user__email=email)

        school = create_school()
        add_teacher_to_school(teacher, school, is_admin=True)

        class1, _, access_code1 = create_class_directly(email)
        class2, _, access_code2 = create_class_directly(email)
        _, _, student1 = create_school_student_directly(access_code1)
        _, _, student2 = create_school_student_directly(access_code2)

        level1 = Level.objects.get(id=1)

        level1.locked_for_class.add(class1)

        assert not can_play_level(student1.new_user, level1, False)
        assert can_play_level(student2.new_user, level1, False)

    def test_next_level_for_locked_levels(self):
        email, password = signup_teacher_directly()

        teacher = Teacher.objects.get(new_user__email=email)

        school = create_school()
        add_teacher_to_school(teacher, school, is_admin=True)

        klass, _, access_code = create_class_directly(email)
        _, _, student = create_school_student_directly(access_code)

        level1 = Level.objects.get(name="1")
        level2 = Level.objects.get(name="2")
        level3 = Level.objects.get(name="3")
        level4 = Level.objects.get(name="4")
        level106 = Level.objects.get(name="106")
        level107 = Level.objects.get(name="107")
        level108 = Level.objects.get(name="108")
        level109 = Level.objects.get(name="109")

        level2.locked_for_class.add(klass)
        level3.locked_for_class.add(klass)
        level107.locked_for_class.add(klass)
        level108.locked_for_class.add(klass)
        level109.locked_for_class.add(klass)

        next_level_url = _next_level_url(level1, student.new_user, False)

        assert next_level_url == f"/rapidrouter/{level4.name}/"

        prev_level_url = _prev_level_url(level4, student.new_user, False)
        assert prev_level_url == f"/rapidrouter/{level1.name}/"

        next_level_url = _next_level_url(level106, student.new_user, False)

        assert next_level_url == f"/rapidrouter/{level109.name}/"

        prev_level_url = _prev_level_url(level109, student.new_user, False)
        assert prev_level_url == f"/rapidrouter/{level106.name}/"
