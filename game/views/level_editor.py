# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
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
import json
import re

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict

import game.messages as messages
import game.level_management as level_management
import game.permissions as permissions
from game import random_road
from game.decor import get_all_decor, get_decor_element
from game.models import Level, Block
from portal.models import Student, Class, Teacher
from portal.templatetags import app_tags
from game import app_settings
from game.cache import cached_level_decor, cached_level_blocks
from game.theme import get_all_themes
from game.character import get_all_character


def level_editor(request):
    """ Renders the level editor page.

    **Context**

    ``RequestContext``
    ``blocks``
        Blocks that can be chosen to be played with later on. List of :model:`game.Block`.

    **Template:**

    :template:`game/level_editor.html`
    """

    context = RequestContext(request, {
        'blocks': available_blocks(),
        'decor': get_all_decor(),
        'characters': get_all_character(),
        'themes': get_all_themes(),
        'cow_level_enabled': app_settings.COW_FEATURE_ENABLED,
        'night_mode_feature_enabled': str(app_settings.NIGHT_MODE_FEATURE_ENABLED).lower(),
    })
    return render(request, 'game/level_editor.html', context_instance=context)


def available_blocks():
    if app_settings.COW_FEATURE_ENABLED:
        return Block.objects.all()
    else:
        return Block.objects.all().exclude(type__in=['declare_event', 'puff_up', 'sound_horn'])


def play_anonymous_level(request, levelId, from_level_editor=True, random_level=False):
    night_mode = False if not app_settings.NIGHT_MODE_FEATURE_ENABLED else 'night' in request.GET
    level = Level.objects.filter(id=levelId)

    if not level.exists():
        return redirect(reverse('level_editor'), permanent=True)

    level = level[:1].get()

    if not level.anonymous:
        return redirect(reverse('level_editor'), permanent=True)

    lesson = mark_safe(messages.description_level_default())
    hint = mark_safe(messages.hint_level_default())

    attempt = None
    house = get_decor_element('house', level.theme).url
    cfc = get_decor_element('cfc', level.theme).url
    background = get_decor_element('tile1', level.theme).url
    character = level.character

    character_url = character.top_down
    character_width = character.width
    character_height = character.height
    wreckage_url = 'van_wreckage.svg'

    decor_data = cached_level_decor(level)

    if night_mode:
        block_data = level_management.get_night_blocks(level)
        night_mode = "true"
        lesson = messages.title_night_mode()
        model_solution = '[]'
    else:
        block_data = cached_level_blocks(level)
        night_mode = "false"
        model_solution = level.model_solution

    return_view_name = 'level_editor' if from_level_editor else 'levels'

    context = RequestContext(request, {
        'level': level,
        'decor': decor_data,
        'blocks': block_data,
        'lesson': lesson,
        'character': character,
        'background': background,
        'house': house,
        'cfc': cfc,
        'hint': hint,
        'attempt': attempt,
        'random_level': random_level,
        'return_url': reverse(return_view_name),
        'character_url': character_url,
        'character_width': character_width,
        'character_height': character_height,
        'wreckage_url': wreckage_url,
        'night_mode': night_mode,
        'night_mode_feature_enabled': str(app_settings.NIGHT_MODE_FEATURE_ENABLED).lower(),
        'model_solution': model_solution,
    })

    level.delete()

    return render(request, 'game/game.html', context_instance=context)


def level_data_for(level):
    return {'name': level.name,
            'owner': app_tags.make_into_username(level.owner.user),
            'id': level.id}


def levels_shared_with(user):
    shared_levels = level_management.levels_shared_with(user)
    shared_data = map(level_data_for, shared_levels)
    return shared_data


def levels_owned_by(user):
    levels_owned_by_user = level_management.levels_owned_by(user)
    owned_data = map(level_data_for, levels_owned_by_user)
    return owned_data


def get_list_of_loadable_levels(user):
    owned_data = levels_owned_by(user)
    shared_data = levels_shared_with(user)

    return {'ownedLevels': owned_data, 'sharedLevels': shared_data}


def owned_levels(request):
    level_data = levels_owned_by(request.user)
    return HttpResponse(json.dumps(level_data), content_type='application/javascript')


def shared_levels(request):
    level_data = levels_shared_with(request.user)
    return HttpResponse(json.dumps(level_data), content_type='application/javascript')


def get_loadable_levels_for_editor(request):
    response = get_list_of_loadable_levels(request.user)
    return HttpResponse(json.dumps(response), content_type='application/javascript')


def load_level_for_editor(request, levelID):
    level = get_object_or_404(Level, id=levelID)

    if not permissions.can_load_level(request.user, level):
        return HttpResponseUnauthorized()

    level_dict = model_to_dict(level)
    level_dict['theme'] = level.theme.id
    level_dict['decor'] = cached_level_decor(level)
    level_dict['blocks'] = cached_level_blocks(level)

    response = {'owned': level.owner == request.user.userprofile, 'level': level_dict}

    return HttpResponse(json.dumps(response), content_type='application/javascript')


@transaction.atomic
def save_level_for_editor(request, levelId=None):
    """ Processes a request on creation of the map in the level editor """
    data = json.loads(request.POST['data'])
    if levelId is not None:
        level = get_object_or_404(Level, id=levelId)
    else:
        level = Level(default=False, anonymous=data['anonymous'])
        if permissions.can_create_level(request.user):
            level.owner = request.user.userprofile
    if not permissions.can_save_level(request.user, level):
        return HttpResponseUnauthorized()

    pattern = re.compile("^(\w?[ ]?)*$")
    if pattern.match(data['name']):
        level_management.save_level(level, data)
        # Add the teacher automatically if it is a new level and the student is not independent
        if ((levelId is None) and hasattr(level.owner, 'student') and
                not level.owner.student.is_independent()):
            level.shared_with.add(level.owner.student.class_field.teacher.user.user)
            level.save()
            level_management.email_new_custom_level(level.owner.student.class_field.teacher.new_user.email,
                                                    request.build_absolute_uri(reverse('level_moderation')),
                                                    request.build_absolute_uri(reverse('play_custom_level',
                                                                                       kwargs={'levelId': level.id})),
                                                    request.build_absolute_uri(reverse('home')),
                                                    str(level.owner.student), level.owner.student.class_field.name)
        response = {'id': level.id}
        return HttpResponse(json.dumps(response), content_type='application/javascript')
    else:
        return HttpResponseUnauthorized()


@transaction.atomic
def delete_level_for_editor(request, levelId):
    level = get_object_or_404(Level, id=levelId)

    if not permissions.can_delete_level(request.user, level):
        return HttpResponseUnauthorized()

    level_management.delete_level(level)

    return HttpResponse(json.dumps({}), content_type='application/javascript')


def generate_random_map_for_editor(request):
    """Generates a new random path suitable for a random level with the parameters provided"""
    data = dict(request.POST)

    size = int(data['numberOfTiles'][0])
    branchiness = float(data['branchiness'][0])
    loopiness = float(data['loopiness'][0])
    curviness = float(data['curviness'][0])
    traffic_lights = data['trafficLights'][0] == 'true'
    scenery = data['scenery'][0] == 'true'

    data = random_road.generate_random_map_data(size, branchiness, loopiness, curviness,
                                                traffic_lights, scenery, False)

    return HttpResponse(json.dumps(data), content_type='application/javascript')


def get_sharing_information_for_editor(request, levelID):
    """ Returns a information about who the level can be and is shared with """
    level = get_object_or_404(Level, id=levelID)
    valid_recipients = {}

    if permissions.can_share_level(request.user, level):
        userprofile = request.user.userprofile
        valid_recipients = {}

        # Note: independent users can't share levels so no need to check
        if hasattr(userprofile, 'student'):
            student = userprofile.student

            # First get all the student's classmates
            class_ = student.class_field
            classmates = Student.objects.filter(class_field=class_).exclude(id=student.id)
            valid_recipients['classmates'] = [
                {'id': classmate.user.user.id,
                 'name': app_tags.make_into_username(classmate.user.user),
                 'shared': level.shared_with.filter(id=classmate.user.user.id).exists()}
                for classmate in classmates]

            # Then add their teacher as well
            teacher = class_.teacher
            valid_recipients['teacher'] = {
                'id': teacher.user.user.id,
                'name': app_tags.make_into_username(teacher.user.user),
                'shared': level.shared_with.filter(id=teacher.user.user.id).exists()}

        elif hasattr(userprofile, 'teacher'):
            teacher = userprofile.teacher

            # First get all the students they teach
            valid_recipients['classes'] = []
            classes_taught = Class.objects.filter(teacher=teacher)
            for class_ in classes_taught:
                students = Student.objects.filter(class_field=class_)
                valid_recipients['classes'].append({
                    'name': class_.name, 'id': class_.id,
                    'students': [{
                        'id': student.user.user.id,
                        'name': app_tags.make_into_username(student.user.user),
                        'shared': level.shared_with.filter(id=student.user.user.id).exists()}
                        for student in students]})

            if not teacher.school:
                valid_recipients['teachers'] = []
            else:
                fellow_teachers = Teacher.objects.filter(school=teacher.school)
                valid_recipients['teachers'] = [{
                    'id': fellow_teacher.user.user.id,
                    'name': app_tags.make_into_username(fellow_teacher.user.user),
                    'shared': level.shared_with.filter(id=fellow_teacher.user.user.id).exists()}
                    for fellow_teacher in fellow_teachers if teacher != fellow_teacher]

    return HttpResponse(json.dumps(valid_recipients), content_type='application/javascript')


def share_level_for_editor(request, levelID):
    """ Shares a level with the provided list of recipients """
    recipientIDs = request.POST.getlist('recipientIDs[]')
    action = request.POST.get('action')

    level = get_object_or_404(Level, id=levelID)
    recipients = User.objects.filter(id__in=recipientIDs)

    def can_share_level_with(r):
        return permissions.can_share_level_with(r, level.owner.user)

    users = [recipient.userprofile.user for recipient in recipients if can_share_level_with(recipient)]

    if action == 'share':
        level_management.share_level(level, *users)
    elif action == 'unshare':
        level_management.unshare_level(level, *users)

    return get_sharing_information_for_editor(request, levelID)


class HttpResponseUnauthorized(HttpResponse):
    def __init__(self):
        super(HttpResponseUnauthorized, self).__init__(content='Unauthorized', status=401)
