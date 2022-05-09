from __future__ import unicode_literals

from builtins import map, range
from datetime import datetime, timedelta

from common.models import Class, Teacher, Student
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly
from common.tests.utils.student import (
    create_school_student_directly,
    create_independent_student_directly,
)
from common.tests.utils.teacher import signup_teacher_directly
from django.test import Client, TestCase
from django.urls import reverse

from game.models import Attempt, Level, Episode
from game.views.scoreboard import StudentRow, scoreboard_data, Headers, StudentInTrouble
from game.views.scoreboard_csv import scoreboard_csv, Headers as CSVHeaders


class ScoreboardTestCase(TestCase):
    def test_teacher_multiple_students_multiple_levels(self):
        episode_ids = [1]
        episode1 = Episode.objects.get(id=1)
        level_ids = [f"{x}" for x in range(1, len(episode1.levels) + 1)]
        level1 = Level.objects.get(name="1")
        level2 = Level.objects.get(name="2")

        clas, student, student2 = set_up_data()

        create_attempt(student, level1, 10)
        create_attempt(student2, level1, 2)
        create_attempt(student2, level2, 16)

        all_levels = [level1, level2]

        attempts_per_student = {
            student: Attempt.objects.filter(
                level__in=all_levels, student=student, is_best_attempt=True
            ).select_related("level"),
            student2: Attempt.objects.filter(
                level__in=all_levels, student=student2, is_best_attempt=True
            ).select_related("level"),
        }

        student_data, headers, level_headers, levels_sorted = scoreboard_data(
            episode_ids, attempts_per_student
        )

        assert headers == Headers
        assert level_headers == [f"L{id}" for id in level_ids]

        assert len(student_data) == 2

        student_row = student_data[0]
        assert student_row.class_field.name == clas.name
        assert student_row.name == student.user.user.first_name
        assert student_row.total_score == 10
        assert student_row.total_time == timedelta(0)
        assert student_row.level_scores[1]["score"] == 10
        assert student_row.completed == 1
        assert student_row.percentage_complete == 50.0

        student_row = student_data[1]
        assert student_row.class_field.name == clas.name
        assert student_row.name == student2.user.user.first_name
        assert student_row.total_score == 18
        assert student_row.total_time == timedelta(0)
        assert student_row.level_scores[1]["score"] == 2
        assert student_row.level_scores[2]["score"] == 16
        assert student_row.completed == 1
        assert student_row.percentage_complete == 45.0

    def test_scoreboard_loads(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        klass, name, access_code = create_class_directly(email)
        create_school_student_directly(access_code)

        url = reverse("scoreboard")
        c = Client()
        c.login(username=email, password=password)
        response = c.get(url)

        assert response.status_code == 200

    def test_student_can_see_classes(self):
        """A student should be able to see the classes they are in"""
        mr_teacher = Teacher.objects.factory(
            "Normal", "Teacher", "normal@school.edu", "secretpa$sword"
        )
        klass, name1, _ = create_class_directly(
            mr_teacher.user.user.email, class_name="Class 1"
        )
        _, name2, _ = create_class_directly(
            mr_teacher.user.user.email, class_name="Class 2"
        )
        student = Student.objects.schoolFactory(klass, "some student", "secret")

        c = Client()
        c.force_login(student.user.user)

        url = reverse("scoreboard")
        response = c.get(url)

        choices_in_form = [
            v for (k, v) in response.context["form"]["classes"].field.choices
        ]
        assert name1 in choices_in_form
        assert name2 not in choices_in_form
        assert len(choices_in_form) == 1

    def test_admin_teacher_can_see_all_classes(self):
        """An admin should be able to see all classes, not just the ones they teach"""
        normal_teacher = Teacher.objects.factory(
            "Normal", "Teacher", "normal@school.edu", "secretpa$sword"
        )
        admin_teacher = Teacher.objects.factory(
            "Admin", "Admin", "admin@school.edu", "secretpa$sword2"
        )

        admin_teacher.is_admin = True
        admin_teacher.save()

        _, name1, _ = create_class_directly(
            admin_teacher.user.user.email, class_name="Class 1"
        )
        _, name2, _ = create_class_directly(
            admin_teacher.user.user.email, class_name="Class 2"
        )
        _, name3, _ = create_class_directly(
            normal_teacher.user.user.email, class_name="Class 3"
        )

        c = Client()
        c.login(username=admin_teacher.user.user.email, password="secretpa$sword2")

        url = reverse("scoreboard")
        response = c.get(url)

        choices_in_form = [
            v for (k, v) in response.context["form"]["classes"].field.choices
        ]

        assert name1 in choices_in_form
        assert name2 in choices_in_form
        assert name3 in choices_in_form

    def test_non_admin_teacher_can_only_see_their_own_classes(self):
        """A teacher who is not an admin should only be able to see their classes, not ones taught by others"""
        teacher1 = Teacher.objects.factory(
            "First", "Teacher", "normal@school.edu", "secretpa$sword"
        )
        teacher2 = Teacher.objects.factory(
            "Second", "Teacher", "admin@school.edu", "secretpa$sword2"
        )

        _, name1, _ = create_class_directly(
            teacher2.user.user.email, class_name="Class 1"
        )
        _, name2, _ = create_class_directly(
            teacher2.user.user.email, class_name="Class 2"
        )
        _, name3, _ = create_class_directly(
            teacher1.user.user.email, class_name="Class 3"
        )

        c = Client()
        # First teacher logs in.  Should see only Class 3
        c.login(username="normal@school.edu", password="secretpa$sword")

        url = reverse("scoreboard")
        response = c.get(url)

        choices_in_form = [
            v for (k, v) in response.context["form"]["classes"].field.choices
        ]

        assert name3 in choices_in_form
        assert name1 not in choices_in_form
        assert name2 not in choices_in_form
        assert len(choices_in_form) == 1

        # Other teacher logs in.  Should see Class 1 and Class 2
        c.login(username="admin@school.edu", password="secretpa$sword2")

        response = c.get(url)
        choices_in_form = [
            v for (k, v) in response.context["form"]["classes"].field.choices
        ]

        assert name3 not in choices_in_form
        assert name1 in choices_in_form
        assert name2 in choices_in_form
        assert len(choices_in_form) == 2

    def test_independent_student_cannot_see_scoreboard(self):
        username, password, _ = create_independent_student_directly()

        c = Client()
        c.login(username=username, password=password)

        url = reverse("scoreboard")
        response = c.get(url)

        assert "Scoreboard is only visible to school students and teachers" in str(
            response.content
        )


class ScoreboardCsvTestCase(TestCase):
    def test_scoreboard_csv(self):
        levels = Level.objects.sorted_levels()[0:2]

        student_rows = [None, None]
        students = [None, None]
        student_rows[0], students[0] = self.student_row("secrète")
        student_rows[1], students[1] = self.student_row()

        improvement_data = []
        for student in students:
            stud = StudentInTrouble(student=student, areas="Getting started")
            improvement_data.append(stud)

        response = scoreboard_csv(student_rows, levels, improvement_data)

        actual_header, actual_rows = self.actual_data(response.content.decode("utf-8"))

        expected_header = self.expected_header(levels)
        assert actual_header == expected_header

        assert len(actual_rows) == len(student_rows)

        # check first row
        (
            class_name,
            name,
            completed_levels,
            total_time,
            total_scores,
            l1,
            l2,
            improvement,
        ) = actual_rows[0].split(",")
        assert student_rows[0].class_field.name == class_name
        assert student_rows[0].name == name
        assert student_rows[0].level_scores[0]["score"] == int(l1)
        assert student_rows[0].level_scores[1]["score"] == int(l2)
        assert improvement == "Getting started"

        # check last row
        last = len(actual_rows) - 1
        (
            class_name,
            name,
            completed_levels,
            total_time,
            total_scores,
            l1,
            l2,
            improvement,
        ) = actual_rows[last].split(",")
        assert student_rows[last].class_field.name == class_name
        assert student_rows[last].name == name
        assert str(student_rows[last].total_time) == total_time

    def student_row(self, class_name=None):
        email, password = signup_teacher_directly()
        _, class_name, access_code = create_class_directly(email, class_name)
        _, _, student = create_school_student_directly(access_code)

        total_time = timedelta(seconds=30)
        scores = [x for x in range(20)]
        total_score = sum(scores)

        level_scores = {}
        for i in range(2):
            level_scores[i] = {}
            level_scores[i]["score"] = 5
            level_scores[i]["full_score"] = 20
            level_scores[i]["is_low_attempt"] = True

        row = StudentRow(
            student=student,
            class_field=Class(name="MyClass"),
            total_time=total_time,
            total_score=total_score,
            level_scores=level_scores,
            completed=2,
            percentage_complete=45,
        )

        return row, student

    def expected_header(self, levels):
        level_strings = list(map(str, levels))
        all_header_strings = CSVHeaders + level_strings + ["Areas for improvement"]
        joined = ",".join(all_header_strings)
        return joined

    def actual_data(self, content):
        split = content.strip().split("\r\n")
        header = split[0]
        rows = split[1:]
        return header, rows


def create_attempt(student, level, score):
    attempt = Attempt.objects.create(
        finish_time=datetime.fromtimestamp(1435305072),
        level=level,
        student=student,
        score=score,
        is_best_attempt=True,
    )
    attempt.start_time = datetime.fromtimestamp(1435305072)
    attempt.save()


def ids_of_levels_named(names):
    levels = Level.objects.filter(name__in=names)
    return levels


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
