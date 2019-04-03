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
import random
import string
from django.core import mail
import sys
import email

from portal.models import Teacher, School
from portal.helpers.emails import generate_token


def generate_details(
    title="Mr", first_name="Test", last_name="Teacher", password="Password1"
):
    email_address = "testteacher%d@codeforlife.com" % random.randint(1, sys.maxint)
    return title, first_name, last_name, email_address, password


def signup_teacher_directly():
    title, first_name, last_name, email_address, password = generate_details()
    teacher = Teacher.objects.factory(
        title, first_name, last_name, email_address, password
    )
    generate_token(teacher.user.user, preverified=True)
    teacher.user.save()
    return teacher, email_address, password


def signup_teacher(page):
    page = page.go_to_teach_page()

    title, first_name, last_name, email_address, password = generate_details()
    page = page.signup(title, first_name, last_name, email_address, password, password)

    page = page.return_to_home_page()

    page = email.follow_verify_email_link_to_teach(page, mail.outbox[0])
    mail.outbox = []

    return page, email_address, password


def create_school():

    school = School()
    school.name = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
    school.postcode = "".join(random.choice(string.ascii_uppercase) for _ in range(7))
    school.country = "United Kingdom"
    school.save()

    return school


def add_teacher_to_school(teacher, school):

    teacher.user.teacher.school = school
    teacher.user.teacher.save()
