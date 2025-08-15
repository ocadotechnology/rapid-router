from deploy import captcha
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse

from game import messages
from game.models import Worksheet


class PythonDenWorksheetTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.orig_captcha_enabled = captcha.CAPTCHA_ENABLED
        captcha.CAPTCHA_ENABLED = False
        super(PythonDenWorksheetTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        captcha.CAPTCHA_ENABLED = cls.orig_captcha_enabled
        super(PythonDenWorksheetTestCase, cls).tearDownClass()

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

    def independent_student_login(self, email, password):
        self.client.login(username=email, password=password)

    def test_page_permissions(self):
        response = self.client.get(reverse("worksheet", args="1"))

        assert response.status_code == 200
        assert (
            response.context["title"]
            == messages.no_permission_python_den_worksheet_title()
        )
        assert (
            response.context["message"]
            == messages.no_permission_python_den_worksheet_page()
        )

        self.login("alberteinstein@codeforlife.com", "Password1")

        response = self.client.get(reverse("worksheet", args="1"))

        assert response.status_code == 200
        assert response.context["worksheet"] == Worksheet.objects.get(pk=1)

        self.logout()
        self.student_login("Leonardo", "AB123", "Password1")

        response = self.client.get(reverse("worksheet", args="1"))

        assert response.status_code == 200
        assert response.context["worksheet"] == Worksheet.objects.get(pk=1)

        self.logout()
        self.independent_student_login("indianajones@codeforlife.com", "Password1")

        response = self.client.get(reverse("worksheet", args="1"))

        assert response.status_code == 200
        assert response.context["worksheet"] == Worksheet.objects.get(pk=1)

        self.logout()
