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
                "g-recaptcha-response": "something",
                "teacher_login_view-current_step": "auth",
            },
            follow=True,
        )
