from __future__ import division
import game.messages as messages
import game.level_management as level_management
import game.permissions as permissions
import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from game import random_road
from helper import getDecorElement
from game.models import Level, Block, Decor, Theme, Character
from portal.models import Student, Class, Teacher
from portal.templatetags import app_tags


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
        'blocks': Block.objects.all(),
        'decor': Decor.objects.all(),
        'characters': Character.objects.all(),
        'themes': Theme.objects.all(),
    })
    return render(request, 'game/level_editor.html', context_instance=context)


def play_anonymous_level(request, levelID, from_level_editor=True):
    level = Level.objects.filter(id=levelID)

    if not level.exists():
        return redirect("/rapidrouter/level_editor", permanent=True)

    level = level[:1].get()

    if not level.anonymous:
        return redirect("/rapidrouter/level_editor", permanent=True)

    lesson = 'description_level_default'
    hint = 'hint_level_default'
    lessonCall = getattr(messages, lesson)
    hintCall = getattr(messages, hint)
    lesson = mark_safe(lessonCall())
    hint = mark_safe(hintCall())

    attempt = None
    house = getDecorElement('house', level.theme).url
    cfc = getDecorElement('cfc', level.theme).url
    background = getDecorElement('tile1', level.theme).url
    character = level.character

    decor_data = level_management.get_decor(level)
    block_data = level_management.get_blocks(level)

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
        'return_url': '/rapidrouter/' + ('level_editor' if from_level_editor else ''),
    })

    level.delete()

    return render(request, 'game/game.html', context_instance=context)


def get_list_of_loadable_levels(user):
    owned_levels, shared_levels = level_management.get_loadable_levels(user)

    owned_data = []
    shared_data = []
    for level in owned_levels:
        owned_data.append({'name': level.name,
                           'owner': app_tags.make_into_username(level.owner.user),
                           'id': level.id})
    for level in shared_levels:
        shared_data.append({'name': level.name,
                            'owner': app_tags.make_into_username(level.owner.user),
                            'id': level.id})

    return {'ownedLevels': owned_data, 'sharedLevels': shared_data}


def get_loadable_levels_for_editor(request):
    response = get_list_of_loadable_levels(request.user)
    return HttpResponse(json.dumps(response), content_type='application/javascript')


def load_level_for_editor(request, levelID):
    level = Level.objects.get(id=levelID)

    response = ''
    if permissions.can_load_level(request.user, level):
        levelDict = model_to_dict(level)
        levelDict['decor'] = level_management.get_decor(level)
        levelDict['blocks'] = level_management.get_blocks(level)

        response = {'owned': level.owner == request.user.userprofile, 'level': levelDict}

    return HttpResponse(json.dumps(response), content_type='application/javascript')


def save_level_for_editor(request, levelID=None):
    """ Processes a request on creation of the map in the level editor """

    data = json.loads(request.POST['data'])

    if levelID is not None:
        level = Level.objects.get(id=levelID)
    else:
        level = Level(default=False, anonymous=data['anonymous'])

        if permissions.can_create_level(request.user):
            level.owner = request.user.userprofile

    if permissions.can_save_level(request.user, level):
        level_management.save_level(level, data)

        # Add the teacher automatically if it is a new level and the student is not independent
        if ((levelID is None) and hasattr(level.owner, 'student') and
                not level.owner.student.is_independent()):
            level.shared_with.add(level.owner.student.class_field.teacher.user.user)
            level.save()

        response = get_list_of_loadable_levels(request.user)
        response['levelID'] = level.id
    else:
        response = {}

    return HttpResponse(json.dumps(response), content_type='application/javascript')


def delete_level_for_editor(request, levelID):
    level = Level.objects.get(id=levelID)
    if permissions.can_delete_level(request.user, level):
        level_management.delete_level(level)

    response = get_list_of_loadable_levels(request.user)

    return HttpResponse(json.dumps(response), content_type='application/javascript')


def generate_random_map_for_editor(request):
    """Generates a new random path suitable for a random level with the parameters provided"""

    size = int(request.GET['numberOfTiles'])
    branchiness = float(request.GET['branchiness'])
    loopiness = float(request.GET['loopiness'])
    curviness = float(request.GET['curviness'])
    traffic_lights = request.GET['trafficLights'] == 'true'
    scenery = request.GET['scenery'] == 'true'

    data = random_road.generate_random_map_data(size, branchiness, loopiness, curviness,
                                                traffic_lights, scenery)

    return HttpResponse(json.dumps(data), content_type='application/javascript')


def get_sharing_information_for_editor(request, levelID):
    """ Returns a information about who the level can be and is shared with """
    level = Level.objects.get(id=levelID)
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

            # Then add all the teachers at the same organisation
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

    level = Level.objects.get(id=levelID)
    recipients = User.objects.filter(id__in=recipientIDs)

    for recipient in recipients:
        if permissions.can_share_level_with(recipient, level.owner.user):
            if action == 'share':
                level_management.share_level(level, recipient.userprofile.user)
            elif action == 'unshare':
                level_management.unshare_level(level, recipient.userprofile.user)

    return get_sharing_information_for_editor(request, levelID)
