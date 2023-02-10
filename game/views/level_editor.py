from __future__ import division

import json
import re
from builtins import map
from builtins import str

from common.models import Student, Teacher
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_POST
from portal.templatetags import app_tags
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView

import game.level_management as level_management
import game.messages as messages
import game.permissions as permissions
from game import app_settings
from game import random_road
from game.cache import cached_level_decor, cached_level_blocks
from game.character import get_all_character
from game.decor import get_all_decor, get_decor_element
from game.models import Level, Block, UserProfile
from game.theme import get_all_themes
from game.views.level import LevelSerializer


def level_editor(request, levelId=None):
    """Renders the level editor page.

    **Context**

    ``RequestContext``
    ``blocks``
        Blocks that can be chosen to be played with later on.
        List of :model:`game.Block`.

    **Template:**

    :template:`game/level_editor.html`
    """

    context = {
        "blocks": [block.type for block in available_blocks()],
        "decor": get_all_decor(),
        "characters": get_all_character(),
        "themes": get_all_themes(),
        "cow_level_enabled": app_settings.COW_FEATURE_ENABLED,
        "night_mode_feature_enabled": str(
            app_settings.NIGHT_MODE_FEATURE_ENABLED
        ).lower(),
    }
    if levelId:
        level = Level.objects.get(id=levelId)
        user_profile = UserProfile.objects.get(id=level.owner_id)

        if request.user.id == user_profile.user_id:
            context["level"] = levelId

    return render(request, "game/level_editor.html", context=context)


def available_blocks():
    if app_settings.COW_FEATURE_ENABLED:
        return Block.objects.all()
    else:
        return Block.objects.all().exclude(type__in=["cow_crossing", "sound_horn"])


def play_anonymous_level(request, levelId, from_level_editor=True, random_level=False):
    night_mode = (
        False if not app_settings.NIGHT_MODE_FEATURE_ENABLED else "night" in request.GET
    )
    level = Level.objects.filter(id=levelId)

    if not level.exists():
        return redirect(reverse("level_editor"), permanent=True)

    level = level[:1].get()

    if not level.anonymous:
        return redirect(reverse("level_editor"), permanent=True)

    lesson = mark_safe(messages.description_level_default())
    hint = mark_safe(messages.hint_level_default())

    attempt = None
    house = get_decor_element("house", level.theme).url
    cfc = get_decor_element("cfc", level.theme).url
    background = get_decor_element("tile1", level.theme).url
    character = level.character

    character_url = character.top_down
    character_width = character.width
    character_height = character.height
    wreckage_url = "van_wreckage.svg"

    decor_data = cached_level_decor(level)

    if night_mode:
        block_data = level_management.get_night_blocks(level)
        night_mode = "true"
        lesson = messages.title_night_mode()
        model_solution = "[]"
    else:
        block_data = cached_level_blocks(level)
        night_mode = "false"
        model_solution = level.model_solution

    return_view_name = "level_editor" if from_level_editor else "levels"

    level.delete()

    return render(
        request,
        "game/game.html",
        context={
            "level": level,
            "decor": decor_data,
            "blocks": block_data,
            "lesson": lesson,
            "character": character,
            "background": background,
            "house": house,
            "cfc": cfc,
            "hint": hint,
            "attempt": attempt,
            "random_level": random_level,
            "return_url": reverse(return_view_name),
            "character_url": character_url,
            "character_width": character_width,
            "character_height": character_height,
            "wreckage_url": wreckage_url,
            "night_mode": night_mode,
            "night_mode_feature_enabled": str(
                app_settings.NIGHT_MODE_FEATURE_ENABLED
            ).lower(),
            "model_solution": model_solution,
        },
    )


def level_data_for(level):
    return {
        "name": level.name,
        "owner": app_tags.make_into_username(level.owner.user),
        "id": level.id,
    }


def levels_shared_with(user):
    shared_levels = level_management.levels_shared_with(user)
    shared_data = list(map(level_data_for, shared_levels))
    return shared_data


def levels_owned_by(user):
    levels_owned_by_user = level_management.levels_owned_by(user)
    owned_data = list(map(level_data_for, levels_owned_by_user))
    return owned_data


def get_list_of_loadable_levels(user):
    owned_data = levels_owned_by(user)
    shared_data = levels_shared_with(user)

    return {"ownedLevels": owned_data, "sharedLevels": shared_data}


def owned_levels(request):
    level_data = levels_owned_by(request.user)
    return HttpResponse(json.dumps(level_data), content_type="application/javascript")


def shared_levels(request):
    level_data = levels_shared_with(request.user)
    return HttpResponse(json.dumps(level_data), content_type="application/javascript")


def get_loadable_levels_for_editor(request):
    response = get_list_of_loadable_levels(request.user)
    return HttpResponse(json.dumps(response), content_type="application/javascript")


def load_level_for_editor(request, levelID):
    level = get_object_or_404(Level, id=levelID)

    if not permissions.can_load_level(request.user, level):
        return HttpResponseUnauthorized()

    level_dict = LevelSerializer(level).data
    level_dict["theme"] = level.theme.id
    level_dict["decor"] = level_management.get_decor(level)
    level_dict["blocks"] = cached_level_blocks(level)

    response = {"owned": level.owner == request.user.userprofile, "level": level_dict}

    return HttpResponse(json.dumps(response), content_type="application/javascript")


@transaction.atomic
@require_POST
def save_level_for_editor(request, levelId=None):
    """Processes a request on creation of the map in the level editor"""
    data = json.loads(request.POST["data"])
    if ("character" not in data) or (not data["character"]):
        # Set a default, to deal with issue #1158 "Cannot save custom level"
        data["character"] = 1
    if levelId is not None:
        level = get_object_or_404(Level, id=levelId)
    else:
        level = Level(default=False, anonymous=data["anonymous"])
        if permissions.can_create_level(request.user):
            level.owner = request.user.userprofile
    if not permissions.can_save_level(request.user, level):
        return HttpResponseUnauthorized()

    pattern = re.compile("^(\w?[ ]?)*$")

    if pattern.match(data["name"]):
        level_management.save_level(level, data)

        if levelId is None:
            teacher = None

            is_user_school_student = (
                hasattr(level.owner, "student")
                and not level.owner.student.is_independent()
            )
            is_user_independent = (
                hasattr(level.owner, "student") and level.owner.student.is_independent()
            )
            is_user_teacher = hasattr(level.owner, "teacher")

            # if level owner is a school student, share with teacher automatically if they aren't an admin
            if is_user_school_student:
                teacher = level.owner.student.class_field.teacher
                if not teacher.is_admin:
                    level.shared_with.add(teacher.new_user)

                if not data["anonymous"]:
                    level_management.email_new_custom_level(
                        level.owner.student.class_field.teacher.new_user.email,
                        request.build_absolute_uri(reverse("level_moderation")),
                        request.build_absolute_uri(
                            reverse("play_custom_level", kwargs={"levelId": level.id})
                        ),
                        request.build_absolute_uri(reverse("home")),
                        str(level.owner.student),
                        level.owner.student.class_field.name,
                    )
            elif is_user_teacher:
                teacher = level.owner.teacher

            # share with all admins of the school if user is in a school
            if not is_user_independent:
                school_admins = teacher.school.admins()

                [
                    level.shared_with.add(school_admin.new_user)
                    for school_admin in school_admins
                    if school_admin.new_user != request.user
                ]

            level.save()
        response = {"id": level.id}
        return HttpResponse(json.dumps(response), content_type="application/javascript")
    else:
        return HttpResponseUnauthorized()


@transaction.atomic
def delete_level_for_editor(request, levelId):
    level = get_object_or_404(Level, id=levelId)

    if not permissions.can_delete_level(request.user, level):
        return HttpResponseUnauthorized()

    level_management.delete_level(level)

    return HttpResponse(json.dumps({}), content_type="application/javascript")


@require_POST
def generate_random_map_for_editor(request):
    """
    Generates a new random path suitable for a random level with the parameters provided
    """
    data = dict(request.POST)

    size = int(data["numberOfTiles"][0])
    branchiness = float(data["branchiness"][0])
    loopiness = float(data["loopiness"][0])
    curviness = float(data["curviness"][0])
    traffic_lights = data["trafficLights"][0] == "true"
    scenery = data["scenery"][0] == "true"

    data = random_road.generate_random_map_data(
        size, branchiness, loopiness, curviness, traffic_lights, scenery, False
    )

    return HttpResponse(json.dumps(data), content_type="application/javascript")


class SharingInformationForEditor(APIView):
    """Returns information about who the level can be and is shared with. This uses
    the CanShareLevel permission."""

    authentication_classes = (SessionAuthentication,)
    permission_classes = (permissions.CanShareLevel,)

    def get(self, request, **kwargs):
        """
        Gets a level's information of who it is and can be shared with. How it works:
        - if the requester is a student, get all their classmates and their teacher.
        - if the requester is a teacher, get all their students and their colleagues.
        :param request: GET request made by user.
        :param kwargs: In this case, houses the level ID.
        :return: A HttpResponse with the data in JSON format.
        """
        levelID = kwargs["levelID"]
        level = get_object_or_404(Level, id=levelID)

        self.check_object_permissions(request, level)

        userprofile = request.user.userprofile
        valid_recipients = {}

        # Note: independent users can't share levels so no need to check
        if hasattr(userprofile, "student"):
            student = userprofile.student

            # First get all the student's classmates
            class_ = student.class_field
            classmates = Student.objects.filter(
                class_field=class_, new_user__is_active=True
            ).exclude(id=student.id)
            valid_recipients["classmates"] = [
                {
                    "id": classmate.new_user.id,
                    "name": app_tags.make_into_username(classmate.new_user),
                    "shared": level.owner == classmate.user
                    or level.shared_with.filter(id=classmate.new_user.id).exists(),
                }
                for classmate in classmates
            ]

            # Then add their teacher as well
            teacher = class_.teacher
            valid_recipients["teacher"] = {
                "id": teacher.new_user.id,
                "name": app_tags.make_into_username(teacher.new_user),
                "shared": level.owner == teacher.user
                or level.shared_with.filter(id=teacher.new_user.id).exists(),
            }

        elif hasattr(userprofile, "teacher"):
            teacher = userprofile.teacher

            # First get all the students they teach
            valid_recipients["classes"] = []
            if teacher.is_admin:
                classes_taught = teacher.school.classes()
            else:
                classes_taught = teacher.class_teacher.all()
            for class_ in classes_taught:
                students = Student.objects.filter(
                    class_field=class_, new_user__is_active=True
                )
                valid_recipients["classes"].append(
                    {
                        "name": f"{class_.name} ({app_tags.make_into_username(class_.teacher.new_user)})"
                        if teacher.is_admin
                        else class_.name,
                        "id": class_.id,
                        "students": [
                            {
                                "id": student.new_user.id,
                                "name": app_tags.make_into_username(student.new_user),
                                "shared": level.owner == student.user
                                or level.shared_with.filter(
                                    id=student.new_user.id
                                ).exists(),
                            }
                            for student in students
                        ],
                    }
                )

            if not teacher.school:
                valid_recipients["teachers"] = []
            else:
                fellow_teachers = Teacher.objects.filter(school=teacher.school)
                valid_recipients["teachers"] = [
                    {
                        "id": fellow_teacher.new_user.id,
                        "name": app_tags.make_into_username(fellow_teacher.new_user),
                        "admin": fellow_teacher.is_admin,
                        "shared": level.owner == fellow_teacher.user
                        or level.shared_with.filter(
                            id=fellow_teacher.new_user.id
                        ).exists(),
                    }
                    for fellow_teacher in fellow_teachers
                    if teacher != fellow_teacher
                ]

        return HttpResponse(
            json.dumps(valid_recipients), content_type="application/javascript"
        )


class ShareLevelView(APIView):
    """Handles the sharing request of a level."""

    authentication_classes = (SessionAuthentication,)
    permission_classes = [permissions.CanShareLevel, permissions.CanShareLevelWith]

    def post(self, request, **kwargs):
        """
        Gets the level id and recipient ids from the request, and shares or
        unshares the level according to the action from the request.
        :param request: the post request sent to the view.
        :return a call to the SharingInformationForEditor class to return the new
        sharing information of the level.
        """
        levelID = kwargs["levelID"]
        recipientIDs = request.POST.getlist("recipientIDs[]")
        action = request.POST.get("action")

        level = get_object_or_404(Level, id=levelID)

        recipients = User.objects.filter(id__in=recipientIDs)
        users = self._get_users_to_share_level_with(recipients)

        if action == "share":
            level_management.share_level(level, *users)
        elif action == "unshare":
            level_management.unshare_level(level, *users)

        return SharingInformationForEditor().get(request, levelID=levelID)

    def _get_users_to_share_level_with(self, recipients):
        """
        Gets a list of users that the level can be shared with - this is done by
        checking the list of requested users against the sharing permission.
        :param recipients: List of recipients the user wants to share the level with.
        :return: A list of users which the requester is authorised to share the level
        with.
        """
        return [
            recipient.userprofile.user
            for recipient in recipients
            if self._can_share_level_with(recipient)
        ]

    def _can_share_level_with(self, recipient):
        """
        Checks whether the requester can share a level with a specific user. Calls the
        CanShareLevelWith permission.
        :param recipient: User that the requester wants to share a level with.
        :return: A boolean of whether the requester has permission.
        """
        return permissions.CanShareLevelWith().has_object_permission(
            self.request, self, recipient
        )


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        super(HttpResponseUnauthorized, self).__init__(
            content="Unauthorized", status=401
        )
