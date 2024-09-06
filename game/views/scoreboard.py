from __future__ import absolute_import, division

from builtins import map, next, object
from datetime import timedelta

from common.models import Class, Teacher, Student
from django.http import Http404
from django.shortcuts import render

import game.messages as messages
import game.permissions as permissions
from game.forms import ScoreboardForm
from game.level_management import levels_owned_by, levels_shared_with
from game.models import Level, Attempt, sort_levels, Episode
from game.views.scoreboard_csv import scoreboard_csv
from . import level_selection
from .helper import renderError

Headers = ["Class", "Student", "Completed", "Total time"]
SharedHeaders = ["Class", "Student"]
TotalPointsHeader = "Total points"


class StudentRow:
    def __init__(self, *args, **kwargs):
        student = kwargs.get("student")
        self.class_field = student.class_field
        self.name = student.user.user.first_name
        self.id = student.id
        self.total_time = kwargs.get("total_time", timedelta(0))
        self.total_score = kwargs.get("total_score", 0)
        self.level_scores = kwargs.get("level_scores", {})
        self.completed = kwargs.get("completed", 0)
        self.success_rate = kwargs.get("success_rate", 0)


# Returns row of student object with values and scores of each selected level
def student_row(levels_sorted, student, best_attempts):
    threshold = 0.5

    num_all = num_finished = num_attempted = num_started = 0
    total_score = 0
    total_possible_score = 0
    level_scores = {}
    times = []

    for level in levels_sorted:
        level_scores[level.id] = {}
        level_scores[level.id]["score"] = ""

        if (
            level.episode is None
            and student.new_user not in level.shared_with.all()
        ):
            level_scores[level.id]["score"] = "Not shared"

        if level.owner == student.user:
            level_scores[level.id]["score"] = "Owner"

    if best_attempts:
        attempts_dict = {
            best_attempt.level.id: best_attempt
            for best_attempt in best_attempts
        }
        for level in levels_sorted:

            attempt = attempts_dict.get(level.id)

            if attempt:
                max_score = 0

                # Max score logic as follows:
                # - All custom levels have a max score of 10
                # - All official levels have a max score of 20 if both route score and algorithm scores are enabled
                # except for levels 1-12 which have a max score of 20 even though the algorithm score is disabled
                if attempt.level.episode is None:
                    max_score = 10
                else:
                    if not attempt.level.disable_route_score:
                        max_score += 10
                    if not attempt.level.disable_algorithm_score:
                        max_score += 10
                    if int(attempt.level.name) < 13:
                        max_score = 20

                num_all += 1
                if attempt.score:
                    if attempt.score / max_score >= threshold:
                        num_finished += 1
                    else:
                        num_attempted += 1
                else:
                    num_started += 1

                total_score += attempt.score if attempt.score is not None else 0
                total_possible_score += max_score

                elapsed_time = attempt.elapsed_time()
                times.append(chop_milliseconds(elapsed_time))
                # '-' is used to show that the student has started the level but has not submitted any attempts

                level_scores[level.id]["score"] = (
                    int(attempt.score) if attempt.score is not None else "-"
                )
                level_scores[level.id]["full_score"] = (
                    attempt.score == max_score
                )
                level_scores[level.id]["is_low_attempt"] = (
                    attempt.score == 0 or max_score / attempt.score < threshold
                )
            else:
                times.append(timedelta(0))

    total_time = sum(times, timedelta())

    success_rate = (
        total_score / total_possible_score * 100
        if total_possible_score > 0
        else 0
    )

    row = StudentRow(
        student=student,
        total_time=total_time,
        total_score=int(total_score),
        level_scores=level_scores,
        completed=num_finished,
        success_rate=success_rate,
    )
    return row


def to_name(level):
    return f"L{level.name}"


def to_python_name(level):
    return f"L{int(level.name) - 1000}"


def shared_level_to_name(level, user):
    return (
        f"{level.name} (you)"
        if user == level.owner
        else f"{level.name} ({level.owner})"
    )


def scoreboard_data(episode_ids, attempts_per_students, language):
    # Show the total score, total time and score of each level
    levels_sorted = []
    for episode_id in episode_ids:
        episode = Episode.objects.get(id=episode_id)
        levels_sorted += episode.levels

    to_name_function = to_name if language == "blockly" else to_python_name

    level_headers = list(map(to_name_function, levels_sorted))
    student_data = [
        student_row(levels_sorted, student, best_attempts)
        for student, best_attempts in attempts_per_students.items()
    ]

    return student_data, Headers, level_headers, levels_sorted


def shared_levels_data(user, shared_levels, attempts_per_students):
    shared_level_headers = list(
        shared_level_to_name(level, user) for level in shared_levels
    )
    shared_student_data = [
        student_row(shared_levels, student, best_attempts)
        for student, best_attempts in attempts_per_students.items()
    ]

    return SharedHeaders, shared_level_headers, shared_student_data


class StudentInTrouble:
    def __init__(self, *args, **kwargs):
        student = kwargs.get("student")
        self.class_field = student.class_field
        self.name = student.user.user.first_name
        self.areas = kwargs.get("areas")


def _check_attempts(best_attempts):
    threshold = 0.5

    # episode ids with low attempts (below 50%)
    low_episode_ids = set()

    for episode_id in range(1, 12):
        total_score = 0
        total_possible_score = 0
        # Get the best attempts for the specific Episode
        attempts = [
            best_attempt
            for best_attempt in best_attempts
            if best_attempt.level.episode.id == episode_id
        ]
        for attempt in attempts:
            max_score = 10 if attempt.level.disable_route_score else 20

            total_score += attempt.score if attempt.score is not None else 0
            total_possible_score += max_score

            is_low_attempt = (
                attempt.score == 0 or max_score / attempt.score < threshold
            )
            if is_low_attempt:
                low_episode_ids.add(episode_id)

    return low_episode_ids


# Returns students that need improvement
def get_improvement_data(attempts_per_student):
    the_students = []  # that need improvement
    for student, best_attempts in attempts_per_student.items():
        episodes_of_concern = _check_attempts(best_attempts)
        if episodes_of_concern:
            areas = [
                messages.get_episode_title(ep_id)
                for ep_id in episodes_of_concern
            ]
            areas_summary = ", ".join(areas)
            the_students.append(
                StudentInTrouble(student=student, areas=areas_summary)
            )
    return the_students


def scoreboard_view(
    request,
    form,
    student_data,
    headers,
    level_headers,
    improvement_data,
    shared_headers,
    shared_level_headers,
    shared_student_data,
    language,
):
    database_episodes = level_selection.fetch_episode_data(False)

    return render(
        request,
        "game/scoreboard.html",
        context={
            "anchor": request.POST,  # Scroll to top of scoreboard section only if request is POST
            "form": form,
            "student_data": student_data,
            "headers": headers,
            "level_headers": level_headers,
            "total_points_header": TotalPointsHeader,
            "episodes": database_episodes,
            "improvement_data": improvement_data,
            "shared_headers": shared_headers,
            "shared_level_headers": shared_level_headers,
            "shared_student_data": shared_student_data,
            "language": language,
        },
    )


def blockly_scoreboard(request):
    return scoreboard(request, "blockly")


def python_scoreboard(request):
    return scoreboard(request, "python")


def scoreboard(request, language):
    """
    Renders a page with students' scores. A teacher can see the visible classes in
    their school. Student's view is restricted to their class if their teacher enabled
    the scoreboard for said class.
    """
    if not permissions.can_see_scoreboard(request.user):
        return render_no_permission_error(request)

    user = User(request.user.userprofile)
    users_classes = classes_for(user)

    episodes_range = range(1, 10) if language == "blockly" else range(12, 16)

    all_episode_ids = [
        episode.id for episode in Episode.objects.filter(pk__in=episodes_range)
    ]

    if user.is_independent_student():
        return render_no_permission_error(request)

    if request.POST:
        class_ids = set(map(int, request.POST.getlist("classes")))
        # Show all levels if the teacher doesn't select any
        episode_ids = (
            set(all_episode_ids)
            if "episodes" not in request.POST
            else set(map(int, request.POST.getlist("episodes")))
        )
    else:
        # Show no data on page load by default (if teacher)
        class_ids = ()
        episode_ids = ()

        # If user is a student, show data for their class and all episodes
        if user.is_student():
            class_ids = {user.student.class_field.id}
            episode_ids = set(all_episode_ids)

    if is_teacher_with_no_classes_assigned(user, users_classes):
        return render_no_permission_error(request)

    if not is_valid_request(user, class_ids):
        raise Http404

    form = ScoreboardForm(
        request.POST or None,
        classes=users_classes,
        language=language,
        initial={
            "classes": class_ids,
            "episodes": episode_ids,
        },  # Check selected checkboxes of each dropdown to cater for POST page load
    )

    classes = Class.objects.filter(id__in=class_ids)
    students = students_visible_to_user(user, classes)

    all_levels = []
    shared_levels = []

    for episode_id in all_episode_ids:
        episode = Episode.objects.get(id=episode_id)
        all_levels += episode.levels

    attempts_per_student = {}

    for student in students:
        best_attempts = Attempt.objects.filter(
            level__in=all_levels, student=student, is_best_attempt=True
        ).select_related("level")
        attempts_per_student[student] = best_attempts

    (student_data, headers, level_headers, levels_sorted) = scoreboard_data(
        episode_ids, attempts_per_student, language
    )
    improvement_data = get_improvement_data(attempts_per_student)

    shared_headers = shared_level_headers = shared_student_data = []

    if language == "blockly":
        attempts_per_student_shared_levels = {}

        if user.is_teacher():
            if user.teacher.is_admin:
                # Get all custom levels owned by non-admin teachers
                standard_teachers = Teacher.objects.filter(
                    school=user.teacher.school, is_admin=False
                )
                for standard_teacher in standard_teachers:
                    shared_levels += levels_owned_by(standard_teacher.new_user)
            else:
                # Get logged in teacher's custom levels
                shared_levels += levels_owned_by(request.user)

            # In all cases, get all admins' custom levels
            school_admins = Teacher.objects.filter(
                school=user.teacher.school, is_admin=True
            )
            for school_admin in school_admins:
                shared_levels += levels_owned_by(school_admin.new_user)

        elif user.is_student():
            shared_levels += levels_shared_with(request.user)

        for student in students:
            shared_levels += levels_owned_by(student.new_user)
            best_attempts_shared_levels = Attempt.objects.filter(
                level__in=shared_levels, student=student, is_best_attempt=True
            ).select_related("level")
            attempts_per_student_shared_levels[
                student
            ] = best_attempts_shared_levels

        (
            shared_headers,
            shared_level_headers,
            shared_student_data,
        ) = shared_levels_data(
            request.user.userprofile,
            shared_levels,
            attempts_per_student_shared_levels,
        )

    csv_export = "export" in request.POST

    if csv_export:
        return scoreboard_csv(
            student_data,
            levels_sorted,
            improvement_data,
            shared_level_headers,
            shared_student_data,
        )
    else:
        return scoreboard_view(
            request,
            form,
            student_data,
            headers,
            level_headers,
            improvement_data,
            shared_headers,
            shared_level_headers,
            shared_student_data,
            language,
        )


def render_no_permission_error(request):
    return renderError(
        request,
        messages.no_permission_title(),
        messages.no_permission_scoreboard(),
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


def sorted_levels_by(level_ids):
    return sort_levels(Level.objects.filter(id__in=level_ids))


def are_classes_viewable_by_teacher(class_ids, user):
    teachers = Teacher.objects.filter(school=user.teacher.school)
    classes_in_teachers_school = Class.objects.filter(
        teacher__in=teachers
    ).values_list("id", flat=True)
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


def is_viewable(class_):
    return class_.classmates_data_viewable


def chop_milliseconds(delta):
    return delta - timedelta(microseconds=delta.microseconds)


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
        return (
            hasattr(self.profile, "student")
            and self.profile.student.is_independent()
        )
