# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
import json

from deploy import captcha
from django.core import mail
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test.testcases import TestCase
from hamcrest import *
from portal.tests.utils.classes import create_class_directly
from portal.tests.utils.organisation import create_organisation_directly
from portal.tests.utils.student import create_school_student_directly

from game.tests.utils.level import create_save_level
from game.tests.utils.teacher import (
    signup_teacher_directly,
    create_school,
    add_teacher_to_school,
)


class LevelEditorTestCase(TestCase):
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
                "username": email,
                "password": password,
                "g-recaptcha-response": "something",
            },
            follow=True,
        )

    def logout(self):
        self.client.post(reverse("logout_view"), follow=True)

    def student_login(self, name, access_code, password):
        self.client.post(
            reverse("student_login"),
            {
                "username": name,
                "access_code": access_code,
                "password": password,
                "g-recaptcha-response": "something",
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
        _, email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data1 = {
            u"origin": u'{"coordinate":[3,5],"direction":"S"}',
            u"pythonEnabled": False,
            u"decor": [],
            u"blocklyEnabled": True,
            u"blocks": [
                {u"type": u"move_forwards"},
                {u"type": u"turn_left"},
                {u"type": u"turn_right"},
            ],
            u"max_fuel": u"50",
            u"pythonViewEnabled": False,
            u"character": u"3",
            u"name": u"abc",
            u"theme": 1,
            u"anonymous": False,
            u"cows": u"[]",
            u"path": u'[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
            u'"connectedNodes":[0]}]',
            u"traffic_lights": u"[]",
            u"destinations": u"[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data1)})

        assert_that(response.status_code, equal_to(200))
        sharing_info1 = json.loads(
            self.get_sharing_information(json.loads(response.content)["id"]).getvalue()
        )
        assert_that(sharing_info1["teacher"]["shared"], equal_to(True))
        assert_that(len(mail.outbox), equal_to(1))

    def test_anonymous_level_saving_school_student(self):
        _, email, password = signup_teacher_directly()
        create_organisation_directly(email)
        _, class_name, access_code = create_class_directly(email)
        student_name, student_password, _ = create_school_student_directly(access_code)

        self.student_login(student_name, access_code, student_password)
        url = reverse("save_level_for_editor")
        data1 = {
            u"origin": u'{"coordinate":[3,5],"direction":"S"}',
            u"pythonEnabled": False,
            u"decor": [],
            u"blocklyEnabled": True,
            u"blocks": [
                {u"type": u"move_forwards"},
                {u"type": u"turn_left"},
                {u"type": u"turn_right"},
            ],
            u"max_fuel": u"50",
            u"pythonViewEnabled": False,
            u"character": u"3",
            u"name": u"abc",
            u"theme": 1,
            u"anonymous": True,
            u"cows": u"[]",
            u"path": u'[{"coordinate":[3,5],"connectedNodes":[1]},{"coordinate":[3,4],'
            u'"connectedNodes":[0]}]',
            u"traffic_lights": u"[]",
            u"destinations": u"[[3,4]]",
        }
        response = self.client.post(url, {"data": json.dumps(data1)})

        assert_that(response.status_code, equal_to(200))
        sharing_info1 = json.loads(
            self.get_sharing_information(json.loads(response.content)["id"]).getvalue()
        )
        assert_that(sharing_info1["teacher"]["shared"], equal_to(True))
        assert_that(len(mail.outbox), equal_to(0))

    def test_level_sharing_with_no_school(self):
        teacher1, email1, password1 = signup_teacher_directly()
        teacher2, _, _ = signup_teacher_directly()

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(0))

    def test_level_sharing_with_school(self):
        teacher1, email1, password1 = signup_teacher_directly()
        teacher2, _, _ = signup_teacher_directly()

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)
        add_teacher_to_school(teacher2, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(1))

    def test_level_sharing_with_empty_school(self):
        teacher1, email1, password1 = signup_teacher_directly()
        teacher2, _, _ = signup_teacher_directly()

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)

        sharing_info1 = json.loads(self.get_sharing_information(level_id).getvalue())
        assert_that(len(sharing_info1["teachers"]), equal_to(0))

    def test_level_can_only_be_shared_by_owner(self):
        teacher1, email1, password1 = signup_teacher_directly()
        teacher2, email2, password2 = signup_teacher_directly()

        self.login(email1, password1)
        level_id = create_save_level(teacher1)

        school1 = create_school()
        add_teacher_to_school(teacher1, school1)

        self.logout()
        self.login(email2, password2)

        url = reverse("share_level_for_editor", args=[level_id])
        data = {u"recipientIDs[]": [teacher2.id], u"action": ["share"]}
        response = self.client.post(url, {"data": data})

        assert_that(response.status_code, equal_to(403))

    def test_level_loading(self):
        teacher1, email1, password1 = signup_teacher_directly()

        self.login(email1, password1)
        level_id = create_save_level(teacher1)
        url = reverse("load_level_for_editor", kwargs={"levelID": level_id})
        response = self.client.get(url)

        assert_that(response.status_code, equal_to(200))
