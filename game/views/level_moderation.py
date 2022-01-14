from __future__ import absolute_import
from __future__ import division

from common.models import Student, Class
from django.shortcuts import render
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

    classes_taught_ids = [class_.id for class_ in classes_taught]
    form = LevelModerationForm(
        request.POST or None,
        classes=classes_taught,
        initial={"classes": classes_taught_ids},
    )

    if request.method == "POST":
        if form.is_valid():
            class_ids = set(map(int, request.POST.getlist("classes")))

            # check user has permission to look at the classes
            if not all(class_id in classes_taught_ids for class_id in class_ids):
                return renderError(
                    request,
                    messages.noPermissionLevelModerationTitle(),
                    messages.noPermissionLevelModerationClass(),
                )
        else:
            class_ids = []
    else:
        class_ids = [class_id for class_id in classes_taught_ids]

    students = Student.objects.filter(
        class_field_id__in=class_ids, new_user__is_active=True
    )
    owners = [student.user for student in students]

    table_headers = [
        "Student",
        "Level name",
        "Shared with",
        "Actions",
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
                    app_tags.make_into_username(user) for user in users_shared_with
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
            "form": form,
            "levelData": level_data,
            "thead": table_headers,
        },
    )
