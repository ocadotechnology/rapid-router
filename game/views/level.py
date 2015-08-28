# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Limited
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
import game.messages as messages
import game.level_management as level_management
import game.permissions as permissions
import json

from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.utils.safestring import mark_safe
from helper import renderError, getDecorElement
from game.cache import cached_level, cached_episode
from game.models import Level, Attempt, Workspace
from portal import beta


def play_custom_level(request, levelID):
    level = cached_level(levelID)
    if level.default:
        raise Http404
    return play_level(request, levelID)

def play_night_level(request, levelName):
    level = get_object_or_404(Level, name=levelName, default=True)
    return play_level(request, level.id, True)

def play_default_level(request, levelName):
    level = get_object_or_404(Level, name=levelName, default=True)
    return play_level(request, level.id, False)


def play_level(request, levelID, night_mode):
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
    level = cached_level(levelID)

    if not permissions.can_play_level(request.user, level, beta.has_beta_access(request)):
        return renderError(request, messages.noPermissionTitle(), messages.notSharedLevel())

    # Set default level description/hint lookups
    lesson = 'description_level_default'
    hint = 'hint_level_default'

    # If it's one of our levels, set level description/hint lookups
    # to point to what they should be
    if level.default:
        lesson = 'description_level' + str(level.name)
        hint = 'hint_level' + str(level.name)

    # Try to get the relevant message, and fall back on defaults
    try:
        lessonCall = getattr(messages, lesson)
        hintCall = getattr(messages, hint)
    except AttributeError:
        lessonCall = messages.description_level_default
        hintCall = messages.hint_level_default

    lesson = mark_safe(lessonCall())
    hint = mark_safe(hintCall())

    house = getDecorElement('house', level.theme).url
    cfc = getDecorElement('cfc', level.theme).url
    background = getDecorElement('tile1', level.theme).url
    character = level.character

    workspace = None
    python_workspace = None
    if not request.user.is_anonymous() and hasattr(request.user.userprofile, 'student'):
        student = request.user.userprofile.student
        if (night_mode):
            attempt = Attempt.objects.filter(level=level, student=student, night_mode=True).first()
        else:
            attempt = Attempt.objects.filter(level=level, student=student, night_mode=False).first()
        if not attempt:
            attempt = Attempt(level=level, student=student, score=None)
            attempt.save()

        workspace = attempt.workspace
        python_workspace = attempt.python_workspace

    decorData = level_management.get_decor(level)

    if (night_mode):
        blockData = level_management.get_night_blocks(level)
        character_url = 'characters/top_view/NightModeVan.svg'
        character_width = 4240
        character_height = 3440
        wreckage_url = 'NightModeVan_wreckage.svg'
        night_mode = "true"
        lesson = 'Can you find your way in the dark?'
        model_solution = 0
    else:
        blockData = level_management.get_blocks(level)
        character_url = character.top_down
        character_width = character.width
        character_height = character.height
        wreckage_url = 'van_wreckage.svg'
        night_mode = "false"
        model_solution = level.model_solution

    context = RequestContext(request, {
        'level': level,
        'lesson': lesson,
        'blocks': blockData,
        'decor': decorData,
        'character': character,
        'background': background,
        'house': house,
        'cfc': cfc,
        'hint': hint,
        'workspace': workspace,
        'python_workspace': python_workspace,
        'return_url': '/rapidrouter/',
        'character_url': character_url,
        'character_width': character_width,
        'character_height': character_height,
        'wreckage_url': wreckage_url,
        'night_mode': night_mode,
        'model_solution': model_solution,
    })

    return render(request, 'game/game.html', context_instance=context)


def delete_level(request, levelID):
    success = False
    level = Level.objects.get(id=levelID)
    if permissions.can_delete_level(request.user, level):
        level_management.delete_level(level)
        success = True

    return HttpResponse(json.dumps({'success': success}), content_type='application/javascript')


def submit_attempt(request):
    """ Processes a request on submission of the program solving the current level. """
    if (not request.user.is_anonymous() and request.method == 'POST' and
            hasattr(request.user.userprofile, "student")):
        level = get_object_or_404(Level, id=request.POST.get('level', 1))
        student = request.user.userprofile.student
        attempt = Attempt.objects.filter(level=level, student=student).first()
        if attempt:
            attempt.score = request.POST.get('score')
            attempt.workspace = request.POST.get('workspace')
            attempt.python_workspace = request.POST.get('python_workspace')
            attempt.save()

    return HttpResponse('[]', content_type='application/json')


def load_list_of_workspaces(request):
    workspaces_owned = []
    if permissions.can_create_workspace(request.user):
        workspaces_owned = Workspace.objects.filter(owner=request.user.userprofile)

    workspaces = [{'id': workspace.id, 'name': workspace.name} for workspace in workspaces_owned]
    return HttpResponse(json.dumps(workspaces), content_type='application/json')


def load_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_load_workspace(request.user, workspace):
        return HttpResponse(json.dumps({'contents': workspace.contents,
                                        'python_contents': workspace.python_contents}),
                            content_type='application/json')

    return HttpResponse(json.dumps(''), content_type='application/json')


def save_workspace(request, workspaceID=None):
    name = request.POST.get('name')
    contents = request.POST.get('contents')
    python_contents = request.POST.get('python_contents')

    workspace = None
    if workspaceID:
        workspace = Workspace.objects.get(id=workspaceID)
    elif permissions.can_create_workspace(request.user):
        workspace = Workspace(owner=request.user.userprofile)

    if workspace and permissions.can_save_workspace(request.user, workspace):
        workspace.name = name
        workspace.contents = contents
        workspace.python_contents = python_contents
        workspace.save()

    return load_list_of_workspaces(request)


def start_episode(request, episode):
    episode = cached_episode(episode)
    return play_level(request, episode.first_level.id)


def delete_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_delete_workspace(request.user, workspace):
        workspace.delete()

    return load_list_of_workspaces(request)
