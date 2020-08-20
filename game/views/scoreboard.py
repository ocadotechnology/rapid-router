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
from __future__ import absolute_import
from __future__ import division

from builtins import map
from builtins import next
from builtins import object
from builtins import str
from datetime import timedelta

from common.models import Class, Teacher, Student
from django.http import Http404
from django.shortcuts import render
from django.utils.translation import ugettext_lazy

import game.messages as messages
import game.permissions as permissions
from game.forms import ScoreboardForm
from game.models import Level, Attempt, sort_levels
from game.views.scoreboard_csv import scoreboard_csv
from . import level_selection
from .helper import renderError

Single_Level_Header = [
    ugettext_lazy("Class"),
    ugettext_lazy("Name"),
    ugettext_lazy("Score"),
    ugettext_lazy("Total Time"),
    ugettext_lazy("Start Time"),
    ugettext_lazy("Finish Time"),
]
Progress_Header = ugettext_lazy("Progress")
Multiple_Levels_Header = [
    ugettext_lazy("Class"),
    ugettext_lazy("Name"),
    ugettext_lazy("Total Score"),
    ugettext_lazy("Total Time"),
    Progress_Header,
]


def scoreboard(request):
    """ Renders a page with students' scores. A teacher can see the visible classes in their
        school. Student's view is restricted to their class if their teacher enabled the
        scoreboard for said class.
    """
    if not permissions.can_see_scoreboard(request.user):
        return render_no_permission_error(request)

    user = User(request.user.userprofile)
    users_classes = classes_for(user)

    class_ids = set(map(int, request.POST.getlist("classes")))
    level_ids = set(map(int, request.POST.getlist("levels")))

    if user.is_independent_student():
        return render_no_permission_error(request)

    if is_teacher_with_no_classes_assigned(user, users_classes):
        return render_no_permission_error(request)

    if not is_valid_request(user, class_ids):
        raise Http404

    form = ScoreboardForm(request.POST or None, classes=users_classes)

    if request.method == "POST" and form.is_valid():
        student_data, headers = scoreboard_data(user, level_ids, class_ids)
    else:
        student_data = []
        headers = []

    csv_export = "export" in request.POST

    if csv_export:
        return scoreboard_csv(student_data, sorted_levels_by(level_ids))
    else:
        return scoreboard_view(request, form, student_data, headers)


def render_no_permission_error(request):
    return renderError(
        request, messages.noPermissionTitle(), messages.noPermissionScoreboard()
    )


def is_teacher_with_no_classes_assigned(user, users_classes):
    return user.is_teacher() and len(users_classes) == 0


def success_response(form, student_data, headers):
    return form, student_data, headers, None


def classes_for(user):
    if user.is_teacher():
        teachers = Teacher.objects.filter(school=user.teacher.school)
        return Class.objects.filter(teacher__in=teachers)
    elif user.is_student():
        class_ = user.student.class_field
        return Class.objects.filter(id=class_.id)


def scoreboard_view(request, form, student_data, headers):
    database_episodes = level_selection.fetch_episode_data(False)
    context_episodes = {}
    for episode in database_episodes:
        context_episodes[episode["first_level"]] = {
            "name": episode["name"]
            + " -- Levels "
            + str(episode["first_level"])
            + " - "
            + str(episode["last_level"]),
            "first_level": str(episode["first_level"]),
            "last_level": str(episode["last_level"]),
        }

    return render(
        request,
        "game/scoreboard.html",
        context={
            "form": form,
            "student_data": student_data,
            "headers": headers,
            "progress_header": Progress_Header,
            "episodes": context_episodes,
        },
    )


def scoreboard_data(user, level_ids, class_ids):
    classes = Class.objects.filter(id__in=class_ids)

    students = students_visible_to_user(user, classes)

    # If there are more than one level to show, show the total score, total time and score of each level
    # Otherwise, show the details of the level (the score, total time, start time and end time)
    return data_and_headers_for(students, level_ids)


def data_and_headers_for(students, level_ids):
    levels_sorted = sorted_levels_by(level_ids)

    score_for_multiple_levels_is_displayed = len(levels_sorted) > 1

    level_names = list(map(to_name, levels_sorted))

    if score_for_multiple_levels_is_displayed:
        headers = Multiple_Levels_Header + level_names
        student_data = multiple_students_multiple_levels(students, levels_sorted)
    else:
        headers = Single_Level_Header
        student_data = multiple_students_one_level(students, first(levels_sorted))

    return student_data, headers


def to_name(level):
    return level.__str__()


def sorted_levels_by(level_ids):
    return sort_levels(Level.objects.filter(id__in=level_ids))


def first(elements):
    if len(elements) == 0:
        raise ValueError("Collection is empty")
    return next(iter(elements))


def are_classes_viewable_by_teacher(class_ids, user):
    teachers = Teacher.objects.filter(school=user.teacher.school)
    classes_in_teachers_school = Class.objects.filter(teacher__in=teachers).values_list(
        "id", flat=True
    )
    for class_id in class_ids:
        is_authorised = class_id in classes_in_teachers_school
        if not is_authorised:
            return False
    return True


def authorised_student_access(class_, class_ids):
    return len(class_ids) == 1 and next(iter(class_ids)) == class_


def students_visible_to_student(student):
    class_ = student.class_field
    if is_viewable(class_):
        return class_.students.all().select_related("class_field", "user__user")
    else:
        return [student]


def students_visible_to_user(user, classes):
    if user.is_teacher():
        return students_of_classes(classes)
    elif user.is_student():
        student = user.student
        return students_visible_to_student(student)


def students_of_classes(classes):
    return Student.objects.filter(class_field__in=classes).select_related(
        "class_field", "user__user"
    )


def is_valid_request(user, class_ids):
    if len(class_ids) == 0:
        return True
    elif user.is_teacher():
        return are_classes_viewable_by_teacher(class_ids, user)
    elif user.is_student():
        return authorised_student_access(user.student.class_field.id, class_ids)
    else:
        return False
    return True


def one_row(student, level):
    best_attempt = Attempt.objects.filter(
        level=level, student=student, is_best_attempt=True
    ).first()
    if best_attempt:
        total_score = best_attempt.score if best_attempt.score is not None else ""
        return StudentRow(
            student=student,
            total_score=total_score,
            start_time=best_attempt.start_time,
            finish_time=best_attempt.finish_time,
            total_time=chop_miliseconds(
                best_attempt.finish_time - best_attempt.start_time
            ),
        )
    else:
        return StudentRow(student=student)


# Return rows of student object with values for progress bar and scores of each selected level
def multiple_students_multiple_levels(students, levels_sorted):
    result = [student_row(levels_sorted, student) for student in students]
    return result


def student_row(levels_sorted, student):
    threshold = 0.5

    num_levels = len(levels_sorted)
    num_all = num_finished = num_attempted = num_started = 0
    total_score = 0.0
    scores = []
    times = []
    progress = (0.0, 0.0, 0.0)
    best_attempts = Attempt.objects.filter(
        level__in=levels_sorted, student=student, is_best_attempt=True
    ).select_related("level")
    if best_attempts:
        attempts_dict = {
            best_attempt.level.id: best_attempt for best_attempt in best_attempts
        }
        for level in levels_sorted:
            attempt = attempts_dict.get(level.id)
            if attempt:
                num_all += 1
                max_score = 10 if attempt.level.disable_route_score else 20
                if attempt.score:
                    if attempt.score / max_score >= threshold:
                        num_finished += 1
                    else:
                        num_attempted += 1
                else:
                    num_started += 1

                total_score += attempt.score if attempt.score is not None else 0

                elapsed_time = attempt.elapsed_time()
                times.append(chop_miliseconds(elapsed_time))
                # '-' is used to show that the student has started the level but has not submitted any attempts

                scores.append(attempt.score if attempt.score is not None else "-")
            else:
                times.append(timedelta(0))
                scores.append("")

        progress = compute_proportions(
            num_levels, num_started, num_attempted, num_finished
        )
    else:
        scores.extend([""] * num_levels)

    total_time = sum(times, timedelta())

    row = StudentRow(
        student=student,
        total_time=total_time,
        total_score=total_score,
        progress=progress,
        scores=scores,
    )
    return row


def compute_proportions(num_levels, num_started, num_attempted, num_finished):
    return (
        (num_started / num_levels) * 100,
        (num_attempted / num_levels) * 100,
        (num_finished / num_levels) * 100,
    )


# Returns rows of student object with score, start time, end time of the level
def multiple_students_one_level(students, level):
    student_data = []

    for student in students:
        student_data.append(one_row(student, level))

    return student_data


def is_viewable(class_):
    return class_.classmates_data_viewable


def chop_miliseconds(delta):
    return delta - timedelta(microseconds=delta.microseconds)


class StudentRow(object):
    def __init__(self, *args, **kwargs):
        student = kwargs.get("student")
        self.class_field = student.class_field
        self.name = student.user.user.first_name
        self.id = student.id
        self.total_time = kwargs.get("total_time", timedelta(0))
        self.total_score = kwargs.get("total_score", 0.0)
        self.progress = kwargs.get("progress", (0.0, 0.0, 0.0))
        self.scores = kwargs.get("scores", [])
        self.start_time = kwargs.get("start_time", "")
        self.finish_time = kwargs.get("finish_time", "")


class User(object):
    def __init__(self, profile):
        self.profile = profile
        if self.is_teacher():
            self.teacher = profile.teacher

        if self.is_student():
            self.student = profile.student

    def is_student(self):
        return (
            hasattr(self.profile, "student")
            and not self.profile.student.is_independent()
        )

    def is_teacher(self):
        return hasattr(self.profile, "teacher")

    def is_independent_student(self):
        return hasattr(self.profile, "student") and self.student.is_independent()
