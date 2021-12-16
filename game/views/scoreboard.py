from __future__ import absolute_import
from __future__ import division

from builtins import map
from builtins import next
from builtins import object
from datetime import timedelta

from common.models import Class, Teacher, Student
from django.http import Http404
from django.shortcuts import render

import game.messages as messages
import game.permissions as permissions
from game.forms import ScoreboardForm
from game.models import Level, Attempt, sort_levels, Episode
from game.views.scoreboard_csv import scoreboard_csv
from . import level_selection
from .helper import renderError

Headers = ["Class", "Student", "Completed", "Total time"]
TotalPointsHeader = "Total points"


def scoreboard(request):
    """
    Renders a page with students' scores. A teacher can see the visible classes in
    their school. Student's view is restricted to their class if their teacher enabled
    the scoreboard for said class.
    """
    if not permissions.can_see_scoreboard(request.user):
        return render_no_permission_error(request)

    user = User(request.user.userprofile)
    users_classes = classes_for(user)

    class_ids = set(map(int, request.POST.getlist("classes")))
    episode_ids = set(map(int, request.POST.getlist("episodes")))
    levels_sorted = []

    if user.is_independent_student():
        return render_no_permission_error(request)

    if is_teacher_with_no_classes_assigned(user, users_classes):
        return render_no_permission_error(request)

    if not is_valid_request(user, class_ids):
        raise Http404

    form = ScoreboardForm(request.POST or None, classes=users_classes)

    if request.method == "POST" and form.is_valid():
        for episode_id in episode_ids:
            episode = Episode.objects.get(id=episode_id)
            levels_sorted += episode.levels

        student_data, headers, level_headers = scoreboard_data(
            user, levels_sorted, class_ids
        )
    else:
        student_data = []
        headers = []
        level_headers = []

    csv_export = "export" in request.POST

    if csv_export:
        return scoreboard_csv(student_data, levels_sorted)
    else:
        return scoreboard_view(request, form, student_data, headers, level_headers)


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
        if user.teacher.is_admin:
            teachers = Teacher.objects.filter(school=user.teacher.school)
            return Class.objects.filter(teacher__in=teachers)
        else:
            return Class.objects.filter(teacher=user.teacher)

    elif user.is_student():
        class_ = user.student.class_field
        return Class.objects.filter(id=class_.id)


def scoreboard_view(request, form, student_data, headers, level_headers):
    database_episodes = level_selection.fetch_episode_data(False)

    return render(
        request,
        "game/scoreboard.html",
        context={
            "form": form,
            "student_data": student_data,
            "headers": headers,
            "level_headers": level_headers,
            "total_points_header": TotalPointsHeader,
            "episodes": database_episodes,
        },
    )


def scoreboard_data(user, episode_ids, class_ids):
    classes = Class.objects.filter(id__in=class_ids)

    students = students_visible_to_user(user, classes)

    # Show the total score, total time and score of each level
    return data_and_headers_for(students, episode_ids)


def data_and_headers_for(students, levels_sorted):
    level_headers = list(map(to_name, levels_sorted))
    student_data = students_level_data(students, levels_sorted)

    return student_data, Headers, level_headers


def to_name(level):
    return f"L{level.id}"


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
        return class_.students.filter(new_user__is_active=True).select_related(
            "class_field", "user__user"
        )
    else:
        return [student]


def students_visible_to_user(user, classes):
    if user.is_teacher():
        return students_of_classes(classes)
    elif user.is_student():
        student = user.student
        return students_visible_to_student(student)


def students_of_classes(classes):
    return Student.objects.filter(
        class_field__in=classes, new_user__is_active=True
    ).select_related("class_field", "user__user")


def is_valid_request(user, class_ids):
    if len(class_ids) == 0:
        return True
    elif user.is_teacher():
        return are_classes_viewable_by_teacher(class_ids, user)
    elif user.is_student():
        return authorised_student_access(user.student.class_field.id, class_ids)
    else:
        return False


# Return rows of student object with values and scores of each selected level
def students_level_data(students, levels_sorted):
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
        completed=num_finished,
        average=total_score / num_finished if num_finished > 0 else 0,
    )
    return row


def compute_proportions(num_levels, num_started, num_attempted, num_finished):
    return (
        (num_started / num_levels) * 100,
        (num_attempted / num_levels) * 100,
        (num_finished / num_levels) * 100,
    )


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
        self.completed = kwargs.get("completed", 0)
        self.average = kwargs.get("average", 0.0)


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
