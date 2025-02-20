from __future__ import unicode_literals

from builtins import map, range
from datetime import datetime, timedelta

from common.models import Class, Teacher, Student
from common.tests.utils.classes import create_class_directly
from common.tests.utils.organisation import create_organisation_directly, join_teacher_to_organisation
from common.tests.utils.student import (
    create_school_student_directly,
    create_independent_student_directly,
)
from common.tests.utils.teacher import signup_teacher_directly
from django.test import Client, TestCase
from django.urls import reverse

from game.models import Attempt, Level, Episode
from game.tests.utils.level import create_save_level
from game.views.scoreboard import (
    StudentRow,
    scoreboard_data,
    Headers,
    StudentInTrouble,
    shared_level_to_name,
    shared_levels_data,
    SharedHeaders,
)
from game.views.scoreboard_csv import (
    scoreboard_csv,
    Headers as CSVHeaders,
    SharedHeaders as CSVSharedHeaders,
)


class ScoreboardTestCase(TestCase):
    def test_teacher_multiple_students_multiple_levels(self):
        # Setup official levels data
        episode_ids = [1, 2]
        episode1 = Episode.objects.get(id=1)
        episode2 = Episode.objects.get(id=2)
        level_ids = [
            f"{x}"
            for x in range(1, len(episode1.levels) + len(episode2.levels) + 1)
        ]
        level1 = Level.objects.get(name="1")
        level13 = Level.objects.get(name="13")

        clas, student, student2 = set_up_data()

        create_attempt(student, level1, 20)
        create_attempt(student2, level1, 2)
        create_attempt(student2, level13, 16)

        # Setup custom levels data
        shared_level = create_save_level(
            student, "custom_level1", shared_with=[student2.new_user]
        )

        create_attempt(student2, shared_level, 10)

        all_levels = [level1, level13]
        all_shared_levels = [shared_level]

        attempts_per_student = {
            student: Attempt.objects.filter(
                level__in=all_levels, student=student, is_best_attempt=True
            ).select_related("level"),
            student2: Attempt.objects.filter(
                level__in=all_levels, student=student2, is_best_attempt=True
            ).select_related("level"),
        }

        shared_attempts_per_student = {
            student2: Attempt.objects.filter(
                level__in=all_shared_levels,
                student=student2,
                is_best_attempt=True,
            ).select_related("level"),
        }

        # Generate results
        student_data, headers, level_headers, levels_sorted = scoreboard_data(
            episode_ids, attempts_per_student, "blockly"
        )
        (
            shared_headers,
            shared_level_headers,
            shared_student_data,
        ) = shared_levels_data(
            student.new_user, all_shared_levels, shared_attempts_per_student
        )

        # Check data for official levels matches
        assert headers == Headers
        assert level_headers == [f"L{id}" for id in level_ids]

        assert len(student_data) == 2

        student_row = student_data[0]
        assert student_row.class_field.name == clas.name
        assert student_row.name == student.user.user.first_name
        assert student_row.total_score == 20
        assert student_row.total_time == timedelta(0)
        assert student_row.level_scores[all_levels[0].id]["score"] == 20
        assert student_row.completed == 1
        assert student_row.success_rate == 100.0

        student_row = student_data[1]
        assert student_row.class_field.name == clas.name
        assert student_row.name == student2.user.user.first_name
        assert student_row.total_score == 18
        assert student_row.total_time == timedelta(0)
        assert student_row.level_scores[all_levels[0].id]["score"] == 2
        assert student_row.level_scores[all_levels[1].id]["score"] == 16
        assert student_row.completed == 1
        assert (
            student_row.success_rate == 45.0
        )  ## the scores, (2 + 16 = 18), divided by the total possible, (2 * 20 = 40), 18/40 = 45%

        # Check data for custom levels matches
        assert shared_headers == SharedHeaders
        assert shared_level_headers == [
            f"{shared_level.name} ({shared_level.owner})"
        ]

        assert len(shared_student_data) == 1

        student_row = shared_student_data[0]
        assert student_row.class_field.name == clas.name
        assert student_row.name == student2.user.user.first_name
        assert student_row.total_score == 10
        assert student_row.total_time == timedelta(0)
        assert student_row.level_scores[shared_level.id]["score"] == 10
        assert student_row.completed == 1
        assert student_row.success_rate == 100.0

    def test_scoreboard_loads(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        klass, name, access_code = create_class_directly(email)
        create_school_student_directly(access_code)

        url = reverse("scoreboard")
        c = Client()
        c.login(username=email, password=password)

        # test scoreboard page loads properly
        response = c.get(url)
        assert response.status_code == 200

        # test scoreboard shows all episodes if no episodes are manually selected
        data = {"classes": [klass.id], "view": [""]}

        response = c.post(url, data)

        active_levels = Level.objects.filter(episode__pk__in=range(1, 10))

        assert response.status_code == 200
        assert len(response.context["level_headers"]) == active_levels.count()

    def test_python_scoreboard_loads(self):
        email, password = signup_teacher_directly()
        create_organisation_directly(email)
        klass, name, access_code = create_class_directly(email)
        create_school_student_directly(access_code)

        url = reverse("python_scoreboard")
        c = Client()
        c.login(username=email, password=password)

        # test scoreboard page loads properly
        response = c.get(url)
        assert response.status_code == 200

        # test scoreboard shows all episodes if no episodes are manually selected
        data = {"classes": [klass.id], "view": [""]}

        response = c.post(url, data)

        active_levels = Level.objects.filter(episode__pk__in=range(12, 16))

        assert response.status_code == 200
        assert len(response.context["level_headers"]) == active_levels.count()

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
        teacher_email = "normal@school.edu"
        admin_email = "admin@school.edu"

        normal_teacher = Teacher.objects.factory(
            "Normal", "Teacher", teacher_email, "secretpa$sword"
        )
        admin_teacher = Teacher.objects.factory(
            "Admin", "Admin", admin_email, "secretpa$sword2"
        )

        school = create_organisation_directly(admin_email)
        join_teacher_to_organisation(teacher_email, school.name)

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
        c.login(
            username=admin_teacher.user.user.email, password="secretpa$sword2"
        )

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

        assert (
            "Scoreboard is only visible to school students and teachers"
            in str(response.content)
        )


class ScoreboardCsvTestCase(TestCase):
    def test_scoreboard_csv(self):
        # Take the first two levels of the main game
        levels = Level.objects.sorted_levels()[0:2]

        # Create 2 students along with their main scoreboard data
        student_rows = [None, None]
        students = [None, None]
        student_rows[0], students[0] = self.student_row("secrète")
        student_rows[1], students[1] = self.student_row()

        # Create 2 custom levels and create the associated student data
        shared_level_rows = [None, None]
        shared_level1 = create_save_level(
            students[0], "level1", shared_with=[students[1].new_user]
        )
        shared_level2 = create_save_level(students[1], "level2")
        shared_levels = [shared_level1, shared_level2]

        shared_levels_headers = list(
            [
                shared_level_to_name(level, level.owner)
                for level in shared_levels
            ]
        )

        shared_level_rows[0] = self.shared_student_row(
            students[0], shared_levels
        )
        shared_level_rows[1] = self.shared_student_row(
            students[1], shared_levels
        )

        # Create students' improvement table data
        improvement_data = []
        for student in students:
            stud = StudentInTrouble(student=student, areas="Getting started")
            improvement_data.append(stud)

        # Generate the CSV
        response = scoreboard_csv(
            student_rows,
            levels,
            improvement_data,
            shared_levels_headers,
            shared_level_rows,
        )

        # Gather the data from the CSV
        (
            actual_scoreboard_header,
            actual_scoreboard_rows,
            actual_shared_levels_header,
            actual_shared_levels_rows,
        ) = self.actual_data(response.content.decode("utf-8"), len(students))

        # Check the headers and the number or rows match expectations
        assert actual_scoreboard_header == self.expected_scoreboard_header(
            levels
        )
        assert len(actual_scoreboard_rows) == len(student_rows)
        assert (
            actual_shared_levels_header
            == self.expected_shared_levels_header(shared_levels)
        )
        assert len(actual_shared_levels_rows) == len(shared_level_rows)

        # check first scoreboard row
        (
            class_name,
            name,
            completed_levels,
            total_time,
            total_scores,
            l1,
            l2,
            improvement,
        ) = actual_scoreboard_rows[0].split(",")
        assert student_rows[0].class_field.name == class_name
        assert student_rows[0].name == name
        assert student_rows[0].level_scores[0]["score"] == int(l1)
        assert student_rows[0].level_scores[1]["score"] == int(l2)
        assert improvement == "Getting started"

        # check last scoreboard row
        last = len(actual_scoreboard_rows) - 1
        (
            class_name,
            name,
            completed_levels,
            total_time,
            total_scores,
            l1,
            l2,
            improvement,
        ) = actual_scoreboard_rows[last].split(",")
        assert student_rows[last].class_field.name == class_name
        assert student_rows[last].name == name
        assert str(student_rows[last].total_time) == total_time

        # check first shared level row
        (class_name, name, l1, l2) = actual_shared_levels_rows[0].split(",")
        assert shared_level_rows[0].class_field.name == class_name
        assert shared_level_rows[0].name == name
        assert shared_level_rows[0].level_scores[0]["score"] == l1
        assert shared_level_rows[0].level_scores[1]["score"] == l2

        # check last shared level row
        last = len(actual_shared_levels_rows) - 1
        (class_name, name, l1, l2) = actual_shared_levels_rows[last].split(",")
        assert shared_level_rows[last].class_field.name == class_name
        assert shared_level_rows[last].name == name
        assert shared_level_rows[last].level_scores[0]["score"] == int(l1)
        assert shared_level_rows[last].level_scores[1]["score"] == l2

    def student_row(self, class_name=None):
        """
        Create data for a student row in the main scoreboard table
        """
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
            success_rate=45,
        )

        return row, student

    def shared_student_row(self, student, shared_levels):
        """
        Create data for a student row in the custom levels table
        """
        level_scores = {}
        for i in range(len(shared_levels)):
            level_scores[i] = {}

            level_scores[i]["score"] = 5

            if student.new_user not in shared_levels[i].shared_with.all():
                level_scores[i]["score"] = "Not shared"

            if shared_levels[i].owner == student.user:
                level_scores[i]["score"] = "Owner"

            level_scores[i]["full_score"] = 10
            level_scores[i]["is_low_attempt"] = True

        row = StudentRow(
            student=student,
            class_field=Class(name="MyClass"),
            total_time=0,
            total_score=0,
            level_scores=level_scores,
            completed=0,
            success_rate=0,
        )

        return row

    def expected_scoreboard_header(self, levels):
        level_strings = list(map(str, levels))
        all_header_strings = (
            CSVHeaders + level_strings + ["Areas for improvement"]
        )
        joined = ",".join(all_header_strings)
        return joined

    def expected_shared_levels_header(self, shared_levels):
        level_strings = list(
            [
                shared_level_to_name(level, level.owner)
                for level in shared_levels
            ]
        )
        all_header_strings = CSVSharedHeaders + level_strings
        joined = ",".join(all_header_strings)
        return joined

    def actual_data(self, content, number_of_students):
        """
        Gets the data from the CSV taking into account the number of students in the request. The CSV should contain
        two tables, each with a one-row header and x number of rows where x = number of students.
        """
        scoreboard_header_row = 0
        scoreboard_rows_start = scoreboard_header_row + 1
        scoreboard_rows_end = scoreboard_rows_start + number_of_students
        shared_levels_header_row = scoreboard_rows_end + 1
        shared_levels_rows_start = shared_levels_header_row + 1
        shared_levels_rows_end = shared_levels_rows_start + number_of_students

        split = content.strip().split("\r\n")
        scoreboard_header = split[scoreboard_header_row]
        scoreboard_rows = split[scoreboard_rows_start:scoreboard_rows_end]
        shared_levels_header = split[shared_levels_header_row]
        shared_levels_rows = split[
            shared_levels_rows_start:shared_levels_rows_end
        ]

        return (
            scoreboard_header,
            scoreboard_rows,
            shared_levels_header,
            shared_levels_rows,
        )


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
