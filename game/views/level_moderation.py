from __future__ import absolute_import
from __future__ import division

import json

from common.models import Student, Class
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext
from portal.templatetags import app_tags

import game.messages as messages
import game.permissions as permissions
from game.forms import LevelModerationForm
from game.models import Level
from .helper import renderError


def level_moderation(request):
    """Renders a page with students' scores.

    **Context**

    ``RequestContext``
    ``form``
        Form used to choose a class and level to show. Instance of `forms.ScoreboardForm.`
    ``studentData``
        List of lists containing all the data to be stored in the scoreboard table.
    ``thead``
        List of Strings representing the headers of the scoreboard table.

    **Template:**

    :template:`game/level_moderation.html`
    """

    # Not showing this part to outsiders.
    if not permissions.can_see_level_moderation(request.user):
        return renderError(
            request,
            messages.noPermissionLevelModerationTitle(),
            messages.noPermissionLevelModerationPage(),
        )

    teacher = request.user.userprofile.teacher
    classes_taught = Class.objects.filter(teacher=teacher)

    if len(classes_taught) <= 0:
        return renderError(
            request,
            messages.noPermissionLevelModerationTitle(),
            messages.noDataToShowLevelModeration(),
        )

    form = LevelModerationForm(request.POST or None, classes=classes_taught)

    student_id = None
    student_dict = None
    level_data = None
    table_headers = None

    if request.method == "POST":
        if form.is_valid():
            student_id = form.data.get("students")
            class_id = form.data.get("classes")

            if not class_id:
                raise Http404

            # check user has permission to look at this class!
            cl = get_object_or_404(Class, id=class_id)
            if not permissions.can_see_class(request.user, cl):
                return renderError(
                    request,
                    messages.noPermissionLevelModerationTitle(),
                    messages.noPermissionLevelModerationClass(),
                )

            students = Student.objects.filter(class_field=cl)
            student_dict = {
                student.id: student.user.user.first_name for student in students
            }

            if student_id:
                # check student is in class
                student = get_object_or_404(Student, id=student_id)
                if student.class_field != cl:
                    return renderError(
                        request,
                        messages.noPermissionLevelModerationTitle(),
                        messages.noPermissionLevelModerationStudent(),
                    )

                owners = [student.user]

            else:
                owners = [student.user for student in students]

            table_headers = [
                ugettext("Student"),
                ugettext("Level name"),
                ugettext("Shared with"),
                ugettext("Play"),
                ugettext("Delete"),
            ]
            level_data = []

            for owner in owners:
                for level in Level.objects.filter(owner=owner):
                    users_shared_with = [
                        user
                        for user in level.shared_with.all()
                        if permissions.CanShareLevelWith().can_share_level_with(
                            user, owner.user
                        )
                        and user != owner.user
                    ]

                    if not users_shared_with:
                        shared_str = "-"
                    else:
                        shared_str = ", ".join(
                            app_tags.make_into_username(user)
                            for user in users_shared_with
                        )

                    level_data.append(
                        {
                            "student": app_tags.make_into_username(owner.user),
                            "id": level.id,
                            "name": level.name,
                            "shared_with": shared_str,
                        }
                    )
    return render(
        request,
        "game/level_moderation.html",
        context={
            "student_id": student_id,
            "students": student_dict,
            "form": form,
            "levelData": level_data,
            "thead": table_headers,
        },
    )


def get_students_for_level_moderation(request, class_id):
    userprofile = request.user.userprofile
    class_ = Class.objects.get(id=class_id)

    if userprofile.teacher != class_.teacher:
        raise Http404

    students = Student.objects.filter(class_field=class_)
    student_dict = {student.id: student.user.user.first_name for student in students}

    return HttpResponse(json.dumps(student_dict), content_type="application/javascript")
