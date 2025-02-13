import json
from datetime import datetime
from unittest.mock import patch

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
            "python_enabled": False,
            "decor": [],
            "blockly_enabled": True,
            "blocks": [
                {"type": "move_forwards"},
                {"type": "turn_left"},
                {"type": "turn_right"},
            ],
            "max_fuel": "50",
            "python_view_enabled": False,
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
        assert (
            response.context["blocklyEpisodes"][0]["name"] == "Getting Started"
        )
        assert (
            response.context["blocklyEpisodes"][0]["levels"][0]["title"]
            == "Can you help the van get to the house?"
        )

    def test_list_python_episodes(self):
        url = reverse("python_levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert (
            response.context["pythonEpisodes"][0]["name"]
            == "Output, Operators, and Data"
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
        (
            student_name1,
            student_password1,
            student1,
        ) = create_school_student_directly(access_code1)
        (
            student_name2,
            student_password2,
            student2,
        ) = create_school_student_directly(access_code2)

        save_url = "save_level_for_editor"

        # Log in as the second teacher
        self.login(email2, password2)
        teacher2_level = create_save_level(teacher2)
        save_level_url = reverse(save_url)

        response = self.client.post(
            save_level_url, {"data": self.level_data(teacher2_level.id)}
        )

        assert response.status_code == 200

        # Log in as the first student
        self.logout()
        self.student_login(student_name1, access_code1, student_password1)

        student1_level = create_save_level(student1)

        response = self.client.post(
            save_level_url, {"data": self.level_data(student1_level.id)}
        )

        assert response.status_code == 200

        # Log in as the second student
        self.logout()
        self.student_login(student_name2, access_code2, student_password2)

        student2_level = create_save_level(student2)

        response = self.client.post(
            save_level_url, {"data": self.level_data(student2_level.id)}
        )

        assert response.status_code == 200

        # Log in as first teacher again and check they have access to all the levels created above
        self.logout()
        self.login(email1, password1)

        url = reverse("levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.context["directly_shared_levels"]) == 1
        assert (
            response.context["directly_shared_levels"][0]["owner"]
            == student1.new_user
        )
        assert response.context["indirectly_shared_levels"][teacher2.new_user]
        assert (
            len(response.context["indirectly_shared_levels"][teacher2.new_user])
            == 2
        )
        assert (
            response.context["indirectly_shared_levels"][teacher2.new_user][0][
                "owner"
            ]
            == teacher2.new_user
        )
        assert (
            response.context["indirectly_shared_levels"][teacher2.new_user][1][
                "owner"
            ]
            == student2.new_user
        )

        # Log in as second teacher again and check they have access to only their student's level
        self.logout()
        self.login(email2, password2)

        url = reverse("levels")
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.context["directly_shared_levels"]) == 1
        assert (
            response.context["directly_shared_levels"][0]["owner"]
            == student2.new_user
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
        level76 = Level.objects.get(name="76")
        level77 = Level.objects.get(name="77")
        level78 = Level.objects.get(name="78")
        level79 = Level.objects.get(name="79")
        level1014 = Level.objects.get(name="1014")
        level1015 = Level.objects.get(name="1015")
        level1016 = Level.objects.get(name="1016")

        level2.locked_for_class.add(klass)
        level3.locked_for_class.add(klass)
        level77.locked_for_class.add(klass)
        level78.locked_for_class.add(klass)
        level1015.locked_for_class.add(klass)

        next_level_url = _next_level_url(level1, student.new_user, False, False)

        assert next_level_url == f"/rapidrouter/{level4.name}/"

        prev_level_url = _prev_level_url(level4, student.new_user, False, False)
        assert prev_level_url == f"/rapidrouter/{level1.name}/"

        next_level_url = _next_level_url(
            level76, student.new_user, False, False
        )

        assert next_level_url == f"/rapidrouter/{level79.name}/"

        prev_level_url = _prev_level_url(
            level79, student.new_user, False, False
        )
        assert prev_level_url == f"/rapidrouter/{level76.name}/"

        next_level_url = _next_level_url(
            level1014, student.new_user, False, True
        )

        assert next_level_url == f"/pythonden/16/"

        prev_level_url = _prev_level_url(
            level1016, student.new_user, False, True
        )
        assert prev_level_url == f"/pythonden/14/"

    @patch(
        "game.views.level.datetime",
        side_effect=lambda *args, **kw: datetime(*args, **kw),
    )
    def test_xmas_theme(self, mock_datetime):
        november = datetime(2023, 11, 1, 0, 0, 0, 0)
        mock_datetime.now.return_value = november

        response = self.client.get(f"{reverse('home')}/rapidrouter/1/")
        assert """CHARACTER_NAME = "Van"\n""" in response.content.decode(
            "utf-8"
        )
        assert (
            """CHARACTER_URL = "characters/top_view/Van.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """WRECKAGE_URL = "van_wreckage.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """BACKGROUND_URL = "decor/grass/tile1.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """HOUSE_URL = "decor/grass/house.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """CFC_URL = "decor/grass/cfc.svg"\n"""
            in response.content.decode("utf-8")
        )

        december = datetime(2023, 12, 1, 0, 0, 0, 0)
        mock_datetime.now.return_value = december

        response = self.client.get(f"{reverse('home')}/rapidrouter/1/")
        assert """CHARACTER_NAME = "Van"\n""" in response.content.decode(
            "utf-8"
        )
        assert (
            """CHARACTER_URL = "characters/top_view/Sleigh.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """WRECKAGE_URL = "sleigh_wreckage.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """BACKGROUND_URL = "decor/snow/tile1.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """HOUSE_URL = "decor/snow/house.svg"\n"""
            in response.content.decode("utf-8")
        )
        assert (
            """CFC_URL = "decor/snow/cfc.svg"\n"""
            in response.content.decode("utf-8")
        )
