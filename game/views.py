from __future__ import division
import json
import os
import messages
import level_management
import permissions

from cache import cached_all_episodes, cached_level, cached_episode
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from forms import *
from game import random_road
from models import Level, Attempt, Block, Episode, Workspace, LevelDecor, Decor, Theme, Character
from portal.models import Student, Class, Teacher
from portal.templatetags import app_tags
from serializers import WorkspaceSerializer, LevelSerializer


#########
# Level #
#########

def play_level(request, levelID):
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

    if not permissions.can_play_level(request.user, level):
        return renderError(request, messages.noPermissionTitle(), messages.notSharedLevel())

    blocks = level.blocks.order_by('id')
    attempt = None
    lesson = 'description_level' + str(level)
    hint = 'hint_level' + str(level)

    try:
        lessonCall = getattr(messages, lesson)
        hintCall = getattr(messages, hint)
    except AttributeError:
        lesson = 'description_level_default'
        hint = 'hint_level_default'
        lessonCall = getattr(messages, lesson)
        hintCall = getattr(messages, hint)

    lesson = mark_safe(lessonCall())
    hint = mark_safe(hintCall())

    decor = LevelDecor.objects.filter(level=level)
    decorData = parseDecor(level.theme, decor)
    house = getDecorElement('house', level.theme).url
    cfc = getDecorElement('cfc', level.theme).url
    background = getDecorElement('tile1', level.theme).url
    character = level.character

    role = 'unknown'
    if request.user.is_anonymous():
        role = 'anonymous'
    elif hasattr(request.user.userprofile, 'student'):
        role = 'student'
    else:
        role = 'teacher'

    if not request.user.is_anonymous() and hasattr(request.user.userprofile, 'student'):
        student = request.user.userprofile.student
        try:
            attempt = get_object_or_404(Attempt, level=level, student=student)
        except Http404:
            attempt = Attempt(level=level, score=0, student=student)
            attempt.save()

    context = RequestContext(request, {
        'level': level,
        'blocks': blocks,
        'lesson': lesson,
        'decor': decorData,
        'character': character,
        'background': background,
        'house': house,
        'cfc': cfc,
        'hint': hint,
        'attempt': attempt,
        'user_role': role,
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
    """ Processes a request on submission of the program solving the current level.
    """
    if not request.user.is_anonymous() and request.method == 'POST':
        if hasattr(request.user, "userprofile") and hasattr(request.user.userprofile, "student"):
            level = get_object_or_404(Level, id=request.POST.get('level', 1))
            attempt = get_object_or_404(Attempt, level=level,
                                        student=request.user.userprofile.student)
            attempt.score = request.POST.get('score', 0)
            attempt.workspace = request.POST.get('workspace', '')
            attempt.save()
    return HttpResponse('')


def load_list_of_workspaces(request):
    workspaces_owned = Workspace.objects.filter(owner=request.user.userprofile)
    workspaces = []
    for workspace in workspaces_owned:
        workspaces.append({'id': workspace.id, 'name': workspace.name})

    return HttpResponse(json.dumps(workspaces), content_type='application/json')


def load_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_load_workspace(request.user, workspace):
        return HttpResponse(json.dumps({'contents': workspace.contents}), content_type='application/json')

    return HttpResponse(json.dumps(''), content_type='application/json')


def save_workspace(request):
    if permissions.can_create_workspace(request.user):
        name = request.POST.get('name')
        contents = request.POST.get('workspace')
        workspace = Workspace(name=name, contents=contents, owner=request.user.userprofile)
        workspace.save()

    return load_list_of_workspaces(request)


def delete_workspace(request, workspaceID):
    workspace = Workspace.objects.get(id=workspaceID)
    if permissions.can_delete_workspace(request.user, workspace):
        workspace.delete()

    return load_list_of_workspaces(request)


###################
# Level selection #
###################

def levels(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    def get_level_title(i):
        title = 'title_level' + str(i)
        try:
            titleCall = getattr(messages, title)
            return mark_safe(titleCall())
        except AttributeError:
            return ""

    def get_attempt_score(level):
        user = request.user
        if (not user.is_anonymous()) and hasattr(request.user, 'userprofile') and \
                hasattr(request.user.userprofile, 'student'):
            try:
                student = user.userprofile.student
                attempt = get_object_or_404(Attempt, level=level, student=student)
                return attempt.score
            except Http404:
                pass
        return None

    episode_data = []
    episode = Episode.objects.get(name='Getting Started')
    while episode is not None:
        levels = []
        minId = -1
        maxId = -1
        for level in episode.levels:
            if minId == -1 or maxId == -1:
                minId = level.id
                maxId = level.id
            levels.append({
                "id": level.id,
                "title": get_level_title(level.id),
                "score": get_attempt_score(level)})
            if level.id > maxId:
                maxId = level.id
            if level.id < minId:
                minId = level.id

        e = {"id": episode.id,
             "name": episode.name,
             "levels": levels,
             "first_level": minId,
             "last_level": maxId}

        episode_data.append(e)
        episode = episode.next_episode

    owned_level_data = []
    shared_level_data = []

    if hasattr(request.user, 'userprofile'):
        owned_levels, shared_levels = level_management.get_list_of_loadable_levels(request.user)

        for level in owned_levels:
            owned_level_data.append({
                "id": level.id,
                "title": level.name,
                "score": get_attempt_score(level)})

        for level in shared_levels:
            shared_level_data.append({
                "id": level.id,
                "title": level.name,
                "owner": level.owner.user,
                "score": get_attempt_score(level)})

    context = RequestContext(request, {
        'episodeData': episode_data,
        'owned_levels': owned_level_data,
        'shared_levels': shared_level_data,
    })
    return render(request, 'game/level_selection.html', context_instance=context)


def start_episode(request, episode):
    episode = cached_episode(episode)
    return redirect("game.views.play_level", level=episode.first_level.id)


def random_level_for_episode(request, episodeID):
    """ Generates a new random level based on the episodeID

    Redirects to :view:`game.views.play_level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return redirect("game.views.play_level", level=level.id)


def logged_students(request):
    """ Renders the page with information about all the logged in students. Uses

    **Context**

    ``RequestContext``
    ``classes``
        List of :model:`game.Class` available to teacher.
    ``message``
        Message shown at the top of the screen. String from `game.messages`.
    ``thead``
        List of table headers for the table with all logged in students.
    ``studentData``
        List of lists with data about all logged in students to be shown in the table.
    ``currentClass``
        Chosen class to be shown. Instance of :model:`game.Class.`

    **Template:**

    :template:`game/logged_students.html`
    """
    """ Helper method for rendering the student info for a logged-in teacher."""

    user = request.user
    message = messages.chooseClass()
    currentClass = ""
    thead = ["Avatar", "Name", "Surname", "Levels attempted", "Levels completed", "Best level",
             "Best score", "Worst level", "Worst score"]
    students = []
    studentData = []

    if request.method == 'POST':
        cl = get_object_or_404(Class, id=request.POST.getlist('classes')[0])
        students = cl.get_logged_in_students()
        currentClass = cl.name
    try:
        classes = user.userprofile.teacher.class_teacher.all()
    except ObjectDoesNotExist:
        message = messages.noPermission()

    for student in students:
        best = None
        worst = None
        # Exclude your own levels.
        levels = Attempt.objects.filter(student=student,
                                        level__owner__isnull=True).order_by('-score')
        levels_completed = levels.exclude(score=0)
        if len(levels_completed) > 0:
            best = levels_completed[0]
            worst = levels_completed[len(levels_completed) - 1]
        studentData.append([student, len(levels), len(levels_completed), best, worst])

    context = RequestContext(request, {
        'classes': classes,
        'message': message,
        'thead': thead,
        'studentData': studentData,
        'currentClass': currentClass,
    })
    return render(request, 'game/logged_students.html', context)

####################
# Level moderation #
####################

def level_moderation(request):
    """ Renders a page with students' scores.

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
        return renderError(request, messages.noPermissionLevelModerationTitle(), messages.noPermissionLevelModerationPage())

    teacher = request.user.userprofile.teacher
    classes_taught = Class.objects.filter(teacher=teacher)
    students_taught = Student.objects.filter(class_field__in=classes_taught)

    if len(classes_taught) <= 0:
        return renderError(request, messages.noPermissionLevelModerationTitle(), messages.noDataToShowLevelModeration())

    form = LevelModerationForm(request.POST or None, classes=classes_taught)

    studentID = None
    student_dict = None
    level_data = None
    table_headers = None

    if request.method == 'POST':
        if form.is_valid():
            studentID = form.data.get('students', False)
            classID = form.data.get('classes', False)

            if not classID or not studentID:
                raise Http404

            # check user has permission to look at this class!
            cl = get_object_or_404(Class, id=classID)
            if not permissions.can_see_class(request.user, cl):
                return renderError(request,
                                   messages.noPermissionLevelModerationTitle(),
                                   messages.noPermissionLevelModerationClass())

            students = Student.objects.filter(class_field=cl)
            student_dict = {student.id: student.user.user.first_name for student in students}

            # check student is in class
            student = get_object_or_404(Student, id=studentID)
            if student.class_field != cl:
                return renderError(request,
                                   messages.noPermissionLevelModerationTitle(),
                                   messages.noPermissionLevelModerationStudent())

            table_headers = ['Level name', 'Shared with', 'Play', 'Delete']
            level_data = []

            for level in Level.objects.filter(owner=student.user):
                users_shared_with = [user for user in level.shared_with.all()
                                     if permissions.can_share_level_with(user, student.user.user)]

                if len(users_shared_with) == 0:
                    shared_str = "-"
                else:
                    shared_str = ""
                    for user in users_shared_with:
                        if user != student.user.user:
                            shared_str += user.first_name + ", "
                    shared_str = shared_str[:-2]

                level_data.append({'id': level.id,
                                   'name': level.name,
                                   'shared_with': shared_str})

    context = RequestContext(request, {
        'studentID': studentID,
        'students': student_dict,
        'form': form,
        'levelData': level_data,
        'thead': table_headers,
    })
    return render(request, 'game/level_moderation.html', context_instance=context)


def get_students_for_level_moderation(request, class_id):
    class_ = Class.objects.get(id=class_id)
    students = Student.objects.filter(class_field=class_)
    student_dict = {student.id: student.user.user.first_name for student in students}

    return HttpResponse(json.dumps(student_dict), content_type="application/javascript")


##############
# Scoreboard #
##############

def scoreboard(request):
    """ Renders a page with students' scores.

    **Context**

    ``RequestContext``
    ``form``
        Form used to choose a class and level to show. Instance of `forms.ScoreboardForm.`
    ``studentData``
        List of lists containing all the data to be stored in the scoreboard table.
    ``thead``
        List of Strings representing the headers of the scoreboard table.

    **Template:**

    :template:`game/scoreboard.html`
    """
    if not permissions.can_see_scoreboard(request.user):
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())
    
    school = None
    thead = []
    classes = []
    if hasattr(request.user.userprofile, 'teacher'):
        school = request.user.userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        classes = Class.objects.filter(id__in=classes_list)
        if len(classes) <= 0:
            return renderError(request, messages.noPermissionTitle(), messages.noDataToShow())
    elif hasattr(request.user.userprofile, 'student') and \
            request.user.userprofile.student.class_field is not None:
        # user is a school student
        class_ = request.user.userprofile.student.class_field
        classes = Class.objects.filter(id=class_.id)
        school = class_.teacher.school
    else:
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())

    form = ScoreboardForm(request.POST or None, classes=classes)
    studentData = None

    if request.method == 'POST':
        if form.is_valid():
            studentData, thead = renderScoreboard(request, form, school)

    context = RequestContext(request, {
        'form': form,
        'studentData': studentData,
        'thead': thead,
    })
    return render(request, 'game/scoreboard.html', context_instance=context)


def renderScoreboard(request, form, school):
    """ Helper method rendering the scoreboard.
    """
    studentData = None
    levelID = form.data.get('levels', False)
    classID = form.data.get('classes', False)
    thead = ['Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']
    if classID:
        cl = get_object_or_404(Class, id=classID)
        students = cl.students.all()
    # check user has permission to look at this class!
    if hasattr(request.user.userprofile, 'teacher'):
        teachers = Teacher.objects.filter(school=request.user.userprofile.teacher.school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        if classID and not int(classID) in classes_list:
            raise Http404
    elif hasattr(request.user.userprofile, 'student') and not \
            request.user.userprofile.student.class_field is None:
        # user is a school student
        class_ = request.user.userprofile.student.class_field
        if classID and int(classID) != class_.id:
            raise Http404
        students = class_.students.all()
        # remove all students except this student from students if the class config doesn't allow
        # for students to see classmates' data
        if not class_.classmates_data_viewable:
            students = students.filter(id=request.user.userprofile.student.id)
    else:
        raise Http404

    # Get level to filter by
    if levelID:
        level = get_object_or_404(Level, id=levelID)

    # Apply filters using handlers - note handleAllClasses filter must further take responsibility
    # for filtering when school students are in a class where they aren't allowed to see classmates'
    # data or for only showing data from students in their class
    if classID and levelID:
        studentData = handleOneClassOneLevel(students, level)
    elif levelID:
        studentData = handleAllClassesOneLevel(request, level)
    else:
        thead = ['Name', 'Total Score', 'Total Time']
        levels = Level.objects.filter(default=1)
        for level in levels:
            thead.append(str(level))
        if classID:
            studentData = handleOneClassAllLevels(students, levels)
        else:
            # TODO: Decide on how open do we want the scoreboard to be?
            studentData = handleAllClassesAllLevels(request, levels)
    return studentData, thead


def createOneRow(student, level):
    row = []
    row.append(student)
    try:
        attempt = Attempt.objects.get(level=level, student=student)
        row.append(attempt.score)
        row.append(attempt.finish_time - attempt.start_time)
        row.append(attempt.start_time)
        row.append(attempt.finish_time)
    except ObjectDoesNotExist:
        row.append("")
    return row


def createRows(studentData, levels):
    """ Helper method getting overall result for students in studentData in given levels.
    """
    for row in studentData:
        for level in levels:
            try:
                attempt = Attempt.objects.get(level=level, student=row[0])
                row[1] += attempt.score
                row[2].append(attempt.finish_time - attempt.start_time)
                row.append(attempt.score)
                row[3].append(attempt.score)
            except ObjectDoesNotExist:
                row[2].append(timedelta(0))
                row.append("")
                row[3].append("")
    for row in studentData:
        row[2] = sum(row[2], timedelta())
    return studentData


def handleOneClassOneLevel(students, level):
    """ Show scoreboard for a chosen level for students of one class.
    """
    studentData = []
    for student in students:
        row = createOneRow(student, level)
        studentData.append(row)
    return studentData


def handleAllClassesOneLevel(request, level):
    """ Show all the students's (from the same school for now) performance on this level.
    """
    studentData = []
    classes = []
    if hasattr(request.user.userprofile, 'student'):
        # Students can only see at most their classmates
        classes = [request.user.userprofile.student.class_field]
    elif hasattr(request.user.userprofile, 'teacher'):
        # Allow teachers to see school stats
        school = request.user.userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

    for cl in classes:
        students = cl.students.all()
        if hasattr(request.user.userprofile, 'student') and not request.user.userprofile.student.class_field.classmates_data_viewable:
            # Filter out other students' data if not allowed to see classmates
            students = students.filter(id=request.user.userprofile.student.id)
        for student in students:
            row = createOneRow(student, level)
            studentData.append(row)
    return studentData


def handleOneClassAllLevels(students, levels):
    """ Show statisctics for all students in a class across all levels (sum).
    """
    studentData = []
    for student in students:
        studentData.append([student, 0.0, [], []])
    return createRows(studentData, levels)


def handleAllClassesAllLevels(request, levels):
    """ For now restricting it to the same school.
    """
    studentData = []
    if hasattr(request.user.userprofile, 'student'):
        # Students can only see at most their classmates
        classes = [request.user.userprofile.student.class_field]
    elif hasattr(request.user.userprofile, 'teacher'):
        # allow teachers to see school stats
        school = request.user.userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

    for cl in classes:
        students = cl.students.all()
        if hasattr(request.user.userprofile, 'student') and not request.user.userprofile.student.class_field.classmates_data_viewable:
            # Filter out other students' data if not allowed to see classmates
            students = students.filter(id=request.user.userprofile.student.id)
        for student in students:
            studentData.append([student, 0.0, [], []])
    return createRows(studentData, levels)


################
# Level editor #
################


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
        'themes': Theme.objects.all()
    })
    return render(request, 'game/level_editor.html', context_instance=context)


def get_list_of_loadable_levels(user):
    owned_levels, shared_levels = level_management.get_list_of_loadable_levels(user)

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
        response = {'owned': level.owner == request.user.userprofile, 'level': model_to_dict(level)}

    return HttpResponse(json.dumps(response), content_type='application/javascript')


def save_level_for_editor(request, levelID=None):
    """ Processes a request on creation of the map in the level editor """

    if levelID is not None:
        level = Level.objects.get(id=levelID)
    else:
        level = Level(default=False)

        if permissions.can_create_level(request.user):
            level.owner = request.user.userprofile

            if hasattr(level.owner, 'student') and level.owner.student.class_field is not None:
                level.save()
                level.shared_with.add(level.owner.student.class_field.teacher.user.user)

    if permissions.can_save_level(request.user, level):
        data = {'name': request.POST.get('name'),
                'path': request.POST.get('path'),
                'destinations': request.POST.get('destinations'),
                'origin': request.POST.get('origin'),
                'decor': request.POST.get('decor'),
                'traffic_lights': request.POST.get('traffic_lights'),
                'max_fuel': request.POST.get('max_fuel'),
                'theme_id': request.POST.get('themeID'),
                'character_name': request.POST.get('character_name'),
                'blockTypes': json.loads(request.POST['block_types'])}

        level_management.save_level(level, data)

        response = get_list_of_loadable_levels(request.user)
        response['levelID'] = level.id
    else:
        response = ''

    return HttpResponse(json.dumps(response), content_type='application/javascript')


def generate_random_map_for_editor(request):
    """Generates a new random path suitable for a random level with the parameters provided"""

    size = int(request.GET['numberOfTiles'])
    branchiness = float(request.GET['branchiness'])
    loopiness = float(request.GET['loopiness'])
    curviness = float(request.GET['curviness'])
    traffic_lights_enabled = request.GET['trafficLightsEnabled'] == 'true'

    data = random_road.generate_random_map_data(size, branchiness, loopiness, curviness,
                                                traffic_lights_enabled)
    return HttpResponse(json.dumps(data), content_type='application/javascript')


def get_sharing_information_for_editor(request, levelID):
    """ Returns a information about who the level can be and is shared with """
    level = Level.objects.get(id=levelID)
    valid_recipients = []
    role = 'anonymous'
        
    if permissions.can_share_level(request.user, level):
        userprofile = request.user.userprofile
        valid_recipients = {}

        if hasattr(userprofile, 'student'):
            student = userprofile.student
            role = 'student'

            # First get all the student's classmates
            class_ = student.class_field
            classmates = Student.objects.filter(class_field=class_).exclude(id=student.id)
            valid_recipients['classmates'] = [{'id': classmate.user.user.id,
                                               'name': classmate.user.user.first_name,
                                               'shared': level.shared_with.filter(id=classmate.user.user.id).exists()}
                                              for classmate in classmates]

            # Then add their teacher as well
            teacher = class_.teacher
            valid_recipients['teacher'] = {'id': teacher.user.user.id,
                                           'name': teacher.title + " " + teacher.user.user.last_name,
                                           'shared': level.shared_with.filter(id=teacher.user.user.id).exists()}

        elif hasattr(userprofile, 'teacher'):
            teacher = userprofile.teacher
            role = 'teacher'

            # First get all the students they teach
            valid_recipients['classes'] = []
            classes_taught = Class.objects.filter(teacher=teacher)
            for class_ in classes_taught:
                students = Student.objects.filter(class_field=class_)
                valid_recipients['classes'].append({'name': class_.name,
                                                    'id': class_.id,
                                                    'students': [{'id': student.user.user.id,
                                                                  'name': student.user.user.first_name,
                                                                  'shared': level.shared_with.filter(id=student.user.user.id).exists()}
                                                                 for student in students]})

            # Then add all the teachers at the same organisation
            fellow_teachers = Teacher.objects.filter(school=teacher.school)
            valid_recipients['teachers'] = [{'id': fellow_teacher.user.user.id,
                                             'name': fellow_teacher.user.user.first_name + " " + fellow_teacher.user.user.last_name,
                                             'shared': level.shared_with.filter(id=fellow_teacher.user.user.id).exists()}
                                            for fellow_teacher in fellow_teachers if teacher != fellow_teacher]

    data = {'validRecipients': valid_recipients, 'role': role}

    return HttpResponse(json.dumps(data), content_type='application/javascript')


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


##################
# Error handling #
##################

def renderError(request, title, message):
    """ Renders an error page with passed title and message.

    **Context**

    ``RequestContext``
    ``title``
        Title that is to be used as a title and header of the page. String.
    ``message``
        Message that will be shown on the error page. String.

    **Template:**

    :template:`game/error.html`
    """
    context = RequestContext(request, {
        'title': title,
        'message': message
    })
    return render(request, 'game/error.html', context_instance=context)


##################
# Helper methods #
##################

def getDecorElement(name, theme):
    """ Helper method to get a decor element corresponding to the theme or a default one."""
    try:
        return Decor.objects.get(name=name, theme=theme)
    except ObjectDoesNotExist:
        return Decor.objects.filter(name=name)[0]


def parseDecor(theme, levelDecors):
    """ Helper method parsing decor into a format 'sendable' to javascript. """
    decorData = []
    for levelDecor in levelDecors:
        decor = Decor.objects.get(name=levelDecor.decorName, theme=theme)
        decorData.append(json.dumps(
            {"coordinate": {"x": levelDecor.x, "y": str(levelDecor.y)}, "url": decor.url,
             "width": decor.width, "height": decor.height}))
    return decorData


def renderAvatarChoice(request):
    """ Helper method for settings view. Generates and processes the avatar changing forms.
    """
    x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(x, 'portal/static/portal/img/avatars')
    img_list = os.listdir(path)
    userProfile = request.user.userprofile
    avatar = userProfile.avatar
    avatarUploadForm = AvatarUploadForm(request.POST or None, request.FILES)
    avatarPreUploadedForm = AvatarPreUploadedForm(request.POST or None, my_choices=img_list)
    if request.method == 'POST':
        if "pre-uploaded" in request.POST and avatarPreUploadedForm.is_valid:
            avatar = avatarPreUploadedForm.data.get('pre-uploaded', False)
        elif "user-uploaded" in request.POST and avatarUploadForm.is_valid():
            avatar = request.FILES.get('avatar', False)
        userProfile.avatar = avatar
        userProfile.save()
    return avatarUploadForm, avatarPreUploadedForm
