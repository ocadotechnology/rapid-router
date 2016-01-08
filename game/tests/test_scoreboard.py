# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
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
from datetime import timedelta, datetime
from django.utils.timezone import utc

from django.test import TestCase
from hamcrest import *

from game.models import Level, Attempt
from game.views.scoreboard import StudentRow, scoreboard_data
from game.views.scoreboard_csv import scoreboard_csv_multiple_levels, scoreboard_csv_single_level
from portal.models import Class
from portal.tests.utils.classes import create_class_directly
from portal.tests.utils.student import create_school_student_directly
from portal.tests.utils.teacher import signup_teacher_directly

Headers = ['Class', 'Name', 'Total Score', 'Total Time', 'Started Levels %', 'Attempted levels %', 'Finished levels %']


class ScoreboardTestCase(TestCase):

    def test_teacher_multiple_students_multiple_levels(self):
        level_ids = ids_of_levels_named(["1", "2"])
        level1 = Level.objects.get(name="1")
        level2 = Level.objects.get(name="2")

        clas, student, student2 = set_up_data()

        create_attempt(student, level1, 10.5)
        create_attempt(student2, level1, 2.3)
        create_attempt(student2, level2, 16.7)

        student_data, headers = scoreboard_data(Teacher(), level_ids, [clas.id])

        assert_that(headers, equal_to(['Class', 'Name', 'Total Score', 'Total Time', 'Progress', u'Level 1', u'Level 2']))
        assert_that(student_data, has_length(2))

        assert_student_row(student_row=student_data[0],
                           class_name=clas.name,
                           student_name=student.user.user.first_name,
                           total_score=10.5,
                           total_time=timedelta(0),
                           progress=(0.0, 0.0, 50.0),
                           scores=[10.5, ''])

        assert_student_row(student_row=student_data[1],
                           class_name=clas.name,
                           student_name=student2.user.user.first_name,
                           total_score=19.0,
                           total_time=timedelta(0),
                           progress=(0.0, 50.0, 50.0),
                           scores=[2.3, 16.7])

    def test_teacher_multiple_students_single_level(self):
        level_ids = ids_of_levels_named(["1"])
        level1 = Level.objects.get(name="1")

        clas, student, student2 = set_up_data()

        create_attempt(student, level1, 10.5)
        create_attempt(student2, level1, 2.3)

        student_data, headers = scoreboard_data(Teacher(), level_ids, [clas.id])

        assert_that(headers, equal_to(['Class', 'Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']))
        assert_that(student_data, has_length(2))

        assert_student_row_single_level(student_row=student_data[0],
                                        class_name=clas.name,
                                        student_name=student.user.user.first_name,
                                        total_score=10.5,
                                        total_time=timedelta(0))

        assert_student_row_single_level(student_row=student_data[1],
                                        class_name=clas.name,
                                        student_name=student2.user.user.first_name,
                                        total_score=2.3,
                                        total_time=timedelta(0))

    def test_student_multiple_students_multiple_levels(self):
        level_ids = ids_of_levels_named(["1", "2"])
        level1 = Level.objects.get(name="1")
        level2 = Level.objects.get(name="2")

        clas, student, student2 = set_up_data(True)

        create_attempt(student, level1, 10.5)
        create_attempt(student2, level1, 2.3)
        create_attempt(student2, level2, 16.7)

        student_data, headers = scoreboard_data(Student(student), level_ids, [clas.id])

        assert_that(headers, equal_to(['Class', 'Name', 'Total Score', 'Total Time', 'Progress', u'Level 1', u'Level 2']))
        assert_that(student_data, has_length(2))

        assert_student_row(student_row=student_data[0],
                           class_name=clas.name,
                           student_name=student.user.user.first_name,
                           total_score=10.5,
                           total_time=timedelta(0),
                           progress=(0.0, 0.0, 50.0),
                           scores=[10.5, ''])

        assert_student_row(student_row=student_data[1],
                           class_name=clas.name,
                           student_name=student2.user.user.first_name,
                           total_score=19.0,
                           total_time=timedelta(0),
                           progress=(0.0, 50.0, 50.0),
                           scores=[2.3, 16.7])

    def test_student_multiple_students_single_level(self):
        level_ids = ids_of_levels_named(["2"])
        level2 = Level.objects.get(name="2")

        clas, student, student2 = set_up_data(True)

        create_attempt(student, level2, 10.5)
        create_attempt(student2, level2, 16.7)

        student_data, headers = scoreboard_data(Student(student), level_ids, [clas.id])

        assert_that(headers, equal_to(['Class', 'Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']))
        assert_that(student_data, has_length(2))

        assert_student_row_single_level(student_row=student_data[0],
                                        class_name=clas.name,
                                        student_name=student.user.user.first_name,
                                        total_score=10.5,
                                        total_time=timedelta(0))

        assert_student_row_single_level(student_row=student_data[1],
                                        class_name=clas.name,
                                        student_name=student2.user.user.first_name,
                                        total_score=16.7,
                                        total_time=timedelta(0))

    def test_student_multiple_students_multiple_levels_cannot_see_classmates(self):
        level_ids = ids_of_levels_named(["1", "2"])
        level1 = Level.objects.get(name="1")
        level2 = Level.objects.get(name="2")

        clas, student, student2 = set_up_data()
        create_attempt(student, level1, 10.5)
        create_attempt(student2, level1, 2.3)
        create_attempt(student2, level2, 16.7)

        student_data, headers = scoreboard_data(Student(student), level_ids, [clas.id])

        assert_that(headers, equal_to(['Class', 'Name', 'Total Score', 'Total Time', 'Progress', u'Level 1', u'Level 2']))
        assert_that(student_data, has_length(1))

        assert_student_row(student_row=student_data[0],
                           class_name=clas.name,
                           student_name=student.user.user.first_name,
                           total_score=10.5,
                           total_time=timedelta(0),
                           progress=(0.0, 0.0, 50.0),
                           scores=[10.5, ''])


class ScoreboardCsvTestCase(TestCase):
    def test_multiple_levels(self):
        levels = Level.objects.sorted_levels()
        student_rows = [(self.student_row()), (self.student_row())]

        response = scoreboard_csv_multiple_levels(student_rows, levels)

        actual_header, actual_rows = self.actual_data(response.content)

        expected_header = self.expected_header(levels)
        expected_rows = self.expected_rows_multiple_levels(student_rows)

        assert_that(actual_header, equal_to(expected_header))

        assert_that(actual_rows, equal_to(expected_rows))

    def test_single_level(self):
        student_rows = [(self.student_row()), (self.student_row())]
        response = scoreboard_csv_single_level(student_rows)

        actual_header, actual_rows = self.actual_data(response.content)

        expected_header = 'Class,Name,Score,Total Time,Start Time,Finish Time'
        expected_rows = self.expected_rows_single_level(student_rows)

        assert_that(actual_header, equal_to(expected_header))

        assert_that(actual_rows, equal_to(expected_rows))

    def expected_rows_single_level(self, student_rows):
        return map(self.expected_row_single_level, student_rows) + [""]

    def expected_rows_multiple_levels(self, student_rows):
        return map(self.expected_row_multiple_levels, student_rows) + [""]

    def student_row(self):
        email, password = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email)
        _, _, student = create_school_student_directly(access_code)

        total_time = timedelta(0, 30)
        scores = [x for x in range(20)]
        total_score = sum(scores)
        progress = (0, 0, 0)

        all_scores = scores + [""] * 89

        row = StudentRow(student=student,
                         total_time=total_time,
                         total_score=total_score,
                         start_time=datetime.fromtimestamp(1435305072, tz=utc),
                         finish_time=datetime.fromtimestamp(1438305072, tz=utc),
                         progress=progress,
                         scores=all_scores,
                         class_field=Class(name="MyClass"))
        return row

    def expected_row_multiple_levels(self, student_row):
        beginning = "%s,%s,190,0:00:30,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19," \
                    % (student_row.class_field.name, student_row.name)
        padding = ','.join([""] * 89)
        return beginning + padding

    def expected_row_single_level(self, student_row):
        return "%s,%s,190,0:00:30,2015-06-26 07:51:12+00:00,2015-07-31 01:11:12+00:00" % (
            student_row.class_field.name, student_row.name)

    def expected_header(self, levels):
        level_strings = map(str, levels)
        all_header_strings = Headers + level_strings
        joined = ','.join(all_header_strings)
        return joined

    def actual_data(self, content):
        split = content.split("\r\n")
        header = split[0]
        rows = split[1:]
        return header, rows


class Student:
    def __init__(self, student):
        self.student = student

    def is_student(self): return True

    def is_teacher(self): return False

    def is_independent_student(self): return False


class Teacher:
    def is_student(self): return False

    def is_teacher(self): return True

    def is_independent_student(self): return False


def assert_student_row(student_row, class_name, student_name, total_score, total_time, progress, scores):
    assert_that(student_row.class_field.name, equal_to(class_name))
    assert_that(student_row.name, equal_to(student_name))
    assert_that(student_row.total_score, equal_to(total_score))
    assert_that(student_row.total_time, equal_to(total_time))
    assert_that(student_row.progress, equal_to(progress))
    assert_that(student_row.scores, equal_to(scores))


def assert_student_row_single_level(student_row, class_name, student_name, total_score, total_time):
    assert_that(student_row.class_field.name, equal_to(class_name))
    assert_that(student_row.name, equal_to(student_name))
    assert_that(student_row.total_score, equal_to(total_score))
    assert_that(student_row.total_time, equal_to(total_time))


def create_attempt(student, level, score):
    attempt = Attempt.objects.create(finish_time=datetime.fromtimestamp(1435305072),
                                     level=level,
                                     student=student,
                                     score=score,
                                     is_best_attempt=True)
    attempt.start_time=datetime.fromtimestamp(1435305072)
    attempt.save()

def ids_of_levels_named(names):
    levels = Level.objects.filter(name__in=names)
    assert_that(len(levels), equal_to(len(names)))
    level_ids = map(lambda x: x.id, levels)
    return level_ids


def set_up_data(classmates_data_viewable=False):
    email, password = signup_teacher_directly()
    clas, class_name, access_code = create_class_directly(email)
    if classmates_data_viewable:
        clas.classmates_data_viewable = True
        clas.save()
    _, _, student = create_school_student_directly(access_code)
    _, _, student2 = create_school_student_directly(access_code)
    create_random_school_data()
    return clas, student, student2


def create_random_school_data():
    email, password = signup_teacher_directly()
    clas, class_name, access_code = create_class_directly(email)
    create_school_student_directly(access_code)
    create_school_student_directly(access_code)
