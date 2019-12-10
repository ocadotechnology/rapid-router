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
from __future__ import division
from __future__ import absolute_import

from builtins import str
from builtins import object
import json

from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.safestring import mark_safe
from rest_framework import serializers

import game.level_management as level_management
import game.messages as messages
import game.permissions as permissions
from game import app_settings
from game.cache import (
    cached_default_level,
    cached_episode,
    cached_custom_level,
    cached_level_decor,
    cached_level_blocks,
)
from game.decor import get_decor_element
from game.models import Level, Attempt, Workspace
from game.views.level_solutions import solutions
from .helper import renderError


def play_custom_level_from_editor(request, levelId):
    return play_custom_level(request, levelId, from_editor=True)


def play_custom_level(request, levelId, from_editor=False):
    level = cached_custom_level(levelId)
    if level.default:
        raise Http404

    return play_level(request, level, from_editor)


def play_default_level(request, levelName):
    level = cached_default_level(levelName)
    return play_level(request, level)


def _next_level_url(level, night_mode):
    if not level.next_level:
        return ""

    return _level_url(level.next_level, night_mode)


def add_night(url, night_mode):
    if night_mode:
        return url + "?night=1"
    return url


def _level_url(level, night_mode):
    if level.default:
        result = _default_level_url(level)
    else:
        result = _custom_level_url(level)

    return add_night(result, night_mode)


def _default_level_url(level):
    return reverse("play_default_level", args=[level.name])


def _custom_level_url(level):
    return reverse("play_custom_level", args=[level.id])


def play_level(request, level, from_editor=False):
    """ Loads a level for rendering in the game.

    **Context**

    ``RequestContext``
    ``level``
        Level that is about to be played. An instance of :model:`game.Level`.
    ``blocks``
        Blocks that are available during the game. List of :model:`game.Block`.
    ``lesson``
        Instruction shown at the load of the level. String from `game.messages`.
    ``hint``
        Hint shown after a number of failed attempts. String from `game.messages`.

    **Template:**

    :template:`game/game.html`
    """

    night_mode = (
        False if not app_settings.NIGHT_MODE_FEATURE_ENABLED else "night" in request.GET
    )

    if not permissions.can_play_level(
        request.user, level, app_settings.EARLY_ACCESS_FUNCTION(request)
    ):
        return renderError(
            request, messages.noPermissionTitle(), messages.notSharedLevel()
        )

    # Set default level description/hint lookups
    lesson = "description_level_default"
    hint = "hint_level_default"

    # If it's one of our levels, set level description/hint lookups
    # to point to what they should be
    if level.default:
        lesson = "description_level" + str(level.name)
        hint = "hint_level" + str(level.name)

    # Try to get the relevant message, and fall back on defaults
    try:
        lessonCall = getattr(messages, lesson)
        hintCall = getattr(messages, hint)
    except AttributeError:
        lessonCall = messages.description_level_default
        hintCall = messages.hint_level_default

    lesson = mark_safe(lessonCall())
    hint = mark_safe(hintCall())

    house = get_decor_element("house", level.theme).url
    cfc = get_decor_element("cfc", level.theme).url
    background = get_decor_element("tile1", level.theme).url
    character = level.character

    workspace = None
    python_workspace = None
    if not request.user.is_anonymous() and hasattr(request.user.userprofile, "student"):
        student = request.user.userprofile.student
        attempt = (
            Attempt.objects.filter(
                level=level,
                student=student,
                finish_time__isnull=True,
                night_mode=night_mode,
            )
            .order_by("-start_time")
            .first()
        )
        if not attempt:
            attempt = Attempt(
                level=level, student=student, score=None, night_mode=night_mode
            )
            fetch_workspace_from_last_attempt(attempt)
            attempt.save()
        else:
            attempt = close_and_reset(attempt)

        workspace = attempt.workspace
        python_workspace = attempt.python_workspace

    decor_data = cached_level_decor(level)

    character_url = character.top_down
    character_width = character.width
    character_height = character.height
    wreckage_url = "van_wreckage.svg"

    if night_mode:
        block_data = level_management.get_night_blocks(level)
        night_mode_javascript = "true"
        lesson = messages.title_night_mode()
        model_solution = "[]"
    else:
        block_data = cached_level_blocks(level)
        night_mode_javascript = "false"
        model_solution = level.model_solution

    return_view = "level_editor" if from_editor else "levels"

    return render(
        request,
        "game/game.html",
        context={
            "level": level,
            "lesson": lesson,
            "blocks": block_data,
            "decor": decor_data,
            "character": character,
            "background": background,
            "house": house,
            "cfc": cfc,
            "hint": hint,
            "workspace": workspace,
            "python_workspace": python_workspace,
            "return_url": reverse(return_view),
            "character_url": character_url,
            "character_width": character_width,
            "character_height": character_height,
            "wreckage_url": wreckage_url,
            "night_mode": night_mode_javascript,
            "night_mode_feature_enabled": str(
                app_settings.NIGHT_MODE_FEATURE_ENABLED
            ).lower(),
            "model_solution": model_solution,
            "next_level_url": _next_level_url(level, night_mode),
            "flip_night_mode_url": _level_url(level, not night_mode),
        },
    )


def fetch_workspace_from_last_attempt(attempt):
    latest_attempt = (
        Attempt.objects.filter(
            level=attempt.level, student=attempt.student, night_mode=attempt.night_mode
        )
        .order_by("-start_time")
        .first()
    )
    if latest_attempt:
        attempt.workspace = latest_attempt.workspace
        attempt.python_workspace = latest_attempt.python_workspace


def delete_level(request, levelID):
    success = False
    level = Level.objects.get(id=levelID)
    if permissions.can_delete_level(request.user, level):
        level_management.delete_level(level)
        success = True

    return HttpResponse(
        json.dumps({"success": success}), content_type="application/javascript"
    )


def submit_attempt(request):
    """ Processes a request on submission of the program solving the current level. """
    if (
        not request.user.is_anonymous()
        and request.method == "POST"
        and hasattr(request.user.userprofile, "student")
    ):
        level = get_object_or_404(Level, id=request.POST.get("level", 1))
        student = request.user.userprofile.student
        attempt = Attempt.objects.filter(
            level=level, student=student, finish_time__isnull=True
        ).first()
        if attempt:
            attempt.score = float(request.POST.get("score"))
            attempt.workspace = request.POST.get("workspace")
            attempt.workspace = request.POST.get("workspace")
            attempt.python_workspace = request.POST.get("python_workspace")

            record_best_attempt(attempt)
            close_and_reset(attempt)

    return HttpResponse("[]", content_type="application/json")


def record_best_attempt(attempt):
    best_attempt = Attempt.objects.filter(
        level=attempt.level,
        student=attempt.student,
        night_mode=attempt.night_mode,
        is_best_attempt=True,
    ).first()
    if best_attempt and (best_attempt.score <= attempt.score):
        best_attempt.is_best_attempt = False
        best_attempt.save()
        attempt.is_best_attempt = True
    elif not best_attempt:
        attempt.is_best_attempt = True


def close_and_reset(attempt):
    attempt.finish_time = timezone.now()
    attempt.save()
    new_attempt = Attempt(
        level=attempt.level,
        student=attempt.student,
        score=None,
        night_mode=attempt.night_mode,
        workspace=attempt.workspace,
        python_workspace=attempt.python_workspace,
    )
    new_attempt.save()
    return new_attempt


def load_list_of_workspaces(request):
    workspaces_owned = []
    if permissions.can_create_workspace(request.user):
        workspaces_owned = Workspace.objects.filter(owner=request.user.userprofile)

    workspaces = [
        {
            "id": workspace.id,
            "name": workspace.name,
            "blockly_enabled": workspace.blockly_enabled,
            "python_enabled": workspace.python_enabled,
        }
        for workspace in workspaces_owned
    ]

    return HttpResponse(json.dumps(workspaces), content_type="application/json")


def load_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_load_workspace(request.user, workspace):
        return HttpResponse(
            json.dumps(
                {
                    "contents": workspace.contents,
                    "python_contents": workspace.python_contents,
                }
            ),
            content_type="application/json",
        )

    return HttpResponse(json.dumps(""), content_type="application/json")


def save_workspace(request, workspaceID=None):
    name = request.POST.get("name")
    contents = request.POST.get("contents")
    python_contents = request.POST.get("python_contents")
    blockly_enabled = json.loads(request.POST.get("blockly_enabled"))
    python_enabled = json.loads(request.POST.get("python_enabled"))

    workspace = None
    if workspaceID:
        workspace = Workspace.objects.get(id=workspaceID)
    elif permissions.can_create_workspace(request.user):
        workspace = Workspace(owner=request.user.userprofile)

    if workspace and permissions.can_save_workspace(request.user, workspace):
        workspace.name = name
        workspace.contents = contents
        workspace.python_contents = python_contents
        workspace.blockly_enabled = blockly_enabled
        workspace.python_enabled = python_enabled
        workspace.save()

    return load_list_of_workspaces(request)


def load_workspace_solution(request, levelName):

    if levelName in solutions:
        workspace = Workspace(owner=request.user.userprofile)
        workspace.id = levelName
        workspace.name = levelName
        workspace.contents = solutions["blockly_default"]
        workspace.python_contents = solutions["python_default"]

        if int(levelName) <= 91:
            workspace.contents = solutions[levelName]
            workspace.blockly_enabled = True
            workspace.python_enabled = False
        else:
            workspace.python_contents = solutions[levelName]
            workspace.blockly_enabled = False
            workspace.python_enabled = True

        return HttpResponse(
            json.dumps(
                {
                    "contents": workspace.contents,
                    "python_contents": workspace.python_contents,
                }
            ),
            content_type="application/json",
        )

    raise Http404


def start_episode(request, episodeId):
    episode = cached_episode(episodeId)
    return play_level(request, episode.first_level, False)


def delete_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_delete_workspace(request.user, workspace):
        workspace.delete()

    return load_list_of_workspaces(request)


class LevelSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Level
        fields = "__all__"
