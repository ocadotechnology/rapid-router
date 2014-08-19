from __future__ import division
import json
import os
import messages
import re

from cache import cached_all_episodes, cached_level, cached_episode
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from django.forms.models import model_to_dict
from rest_framework import status, permissions, mixins, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from forms import *
from game import random_road
from models import Level, Attempt, Command, Block, Episode, Workspace, LevelDecor, Decor, Theme, Character
from portal.models import Class, Teacher
from serializers import WorkspaceSerializer, LevelSerializer
from permissions import UserIsStudent, WorkspacePermissions


def levels(request):
    """ Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    bgcolour = 'rgba(171, 196, 37, {:f})'

    episodes = Episode.objects.all()
    ratio = 1.0 / (len(episodes) + 1)

    def get_level_title(i):
        title = 'title_level' + str(i)
        try:
            titleCall = getattr(messages, title)
            return mark_safe(titleCall())
        except AttributeError:
            return ""

    def get_attempt_score(lvl):
        user = request.user
        score = "    "
        if (not user.is_anonymous()) and hasattr(request.user, 'userprofile') and \
                hasattr(request.user.userprofile, 'student'):
            try:
                student = user.userprofile.student
                attempt = get_object_or_404(Attempt, level=lvl, student=student)
                score = attempt.score
            except Http404:
                pass
        return score

    episode_data = []
    for episode in episodes:
        levels = []
        for level in episode.levels:
            levels.append({
                "id": level.id,
                "name": level.name,
                "title": get_level_title(level.id),
                "score": get_attempt_score(level)})
        opacity = (len(episode_data) + 1) * ratio
        colour = bgcolour.format(opacity)

        e = {"id": episode.id,
             "name": episode.name,
             "colour": colour,
             "levels": levels,
             "opacity": opacity}

        episode_data.append(e)

    context = RequestContext(request, {
        'episodeData': json.dumps(episode_data),
    })
    return render(request, 'game/level_selection.html', context_instance=context)


def level(request, level):
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
    lvl = cached_level(level)
    blocks = lvl.blocks.order_by('id')
    attempt = None
    lesson = None

    if not lvl.default and lvl.owner is not None and \
            (request.user.is_anonymous() or (request.user != lvl.owner.user and
             not lvl.shared_with.filter(pk=request.user.pk).exists())):
        return renderError(request, messages.noPermissionTitle(), messages.notSharedLevel())

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

    decor = LevelDecor.objects.filter(level=lvl)
    decorData = parseDecor(lvl.theme, decor)
    house = getDecorElement('house', lvl.theme).url
    cfc = getDecorElement('cfc', lvl.theme).url
    background = getDecorElement('tile1', lvl.theme).url
    character = lvl.character

    if not request.user.is_anonymous() and hasattr(request.user, 'userprofile') and \
            hasattr(request.user.userprofile, 'student'):
        student = request.user.userprofile.student
        try:
            attempt = get_object_or_404(Attempt, level=lvl, student=student)
        except Http404:
            attempt = Attempt(level=lvl, score=0, student=student)
            attempt.save()

    context = RequestContext(request, {
        'level': lvl,
        'blocks': blocks,
        'lesson': lesson,
        'decor': decorData,
        'character': character,
        'background': background,
        'house': house,
        'cfc': cfc,
        'hint': hint,
        'attempt': attempt
    })

    return render(request, 'game/game.html', context_instance=context)


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
    return render_student_info(request)


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
    # Not showing this part to outsiders.
    if request.user.is_anonymous() or not hasattr(request.user, "userprofile"):
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


def settings(request):
    """ Renders the settings page. Accessible only to logged-in users.

    **Context**

    ``RequestContext``
    ``avatarPreUploadedForm``
        Form used to choose an avatar from already existing images.
        Instance of `forms.avatarPreUploadedForm`.
    ``avatarUploadForm``
        Form used to upload any image as an avatar. Instance of `forms.avatarUploadForm`.
    ``shareLevelForm``
        Form used to share a level with friends. Instance of `forms.shareLevelForm`.
    ``levels``
        List of :model:`game.Level` created by the user.
    ``user``
        Currently logged in :model:`auth.User`.
    ``levelMessage``
        Message shown on the settings page, level listing part. String from `game.messages`.
    ``modal``

    **Template:**

    :template:`game/settings.html`
    """
    if request.user.is_anonymous() or not hasattr(request.user, "userprofile"):
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionMessage())
    levels = Level.objects.filter(owner=request.user.userprofile.id)
    avatarUploadForm, avatarPreUploadedForm = renderAvatarChoice(request)
    choosePerson, shareLevelClassForm, shareLevelPersonForm, shareLevelChoosePerson, message \
        = renderLevelSharing(request)
    levelMessage = messages.noLevelsToShow() if len(levels) == 0 else messages.levelsMessage()
    sharedLevels = request.user.shared.all()
    sharedMessage = messages.noSharedLevels() if len(sharedLevels) == 0 \
        else messages.sharedLevelsMessage()
    title = messages.shareTitle()

    context = RequestContext(request, {
        'avatarPreUploadedForm': avatarPreUploadedForm,
        'avatarUploadForm': avatarUploadForm,
        'shareLevelPersonForm': shareLevelPersonForm,
        'shareLevelClassForm': shareLevelClassForm,
        'shareLevelChoosePerson': shareLevelChoosePerson,
        'choosePerson': choosePerson,
        'levels': levels,
        'sharedLevels': sharedLevels,
        'user': request.user,
        'levelMessage': levelMessage,
        'sharedLevelMessage': sharedMessage,
        'message': message,
        'title': title
    })
    return render(request, 'game/settings.html', context_instance=context)


def random_level_for_episode(request, episodeID):
    """ Generates a new random level based on the episodeID

    Redirects to :view:`game.views.level` with the id of the newly created :model:`game.Level`.
    """
    episode = cached_episode(episodeID)
    level = random_road.create(episode)
    return redirect("game.views.level", level=level.id)


def start_episode(request, episode):
    episode = cached_episode(episode)
    return redirect("game.views.level", level=episode.first_level.id)


def submit(request):
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


def renderScoreboard(request, form, school):
    """ Helper method rendering the scoreboard.
    """
    studentData = None
    levelID = form.data.get('levels', False)
    classID = form.data.get('classes', False)
    thead = ['avatar', 'name', 'surname', 'score', 'total time', 'start time', 'finish time']
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
        thead = ['avatar', 'name', 'surname', 'total score', 'total time']
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
        if not request.user.userprofile.student.class_field.classmates_data_viewable:
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
        if not request.user.userprofile.student.class_field.classmates_data_viewable:
            # Filter out other students' data if not allowed to see classmates
            students = students.filter(id=request.user.userprofile.student.id)
        for student in students:
            studentData.append([student, 0.0, [], []])
    return createRows(studentData, levels)


def renderLevelSharing(request):
    choosePerson = False
    classes = None
    message = ""
    userProfile = request.user.userprofile
    shareLevelPersonForm = ShareLevelPerson(request.POST or None)

    if hasattr(userProfile, "teacher"):
        school = request.user.userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        classes = Class.objects.filter(id__in=classes_list)
        people = User.objects.filter(userprofile__teacher__school=school) | User.objects.filter(userprofile__student__class_field__in=classes_list)
    elif hasattr(userProfile, "student") and userProfile.student.class_field is not None:
        classesObj = userProfile.student.class_field
        classes = Class.objects.filter(pk=classesObj.id)
        people = User.objects.filter(userprofile__student__class_field=classesObj) | User.objects.filter(userprofile__teacher=classesObj.teacher)
    else:
        return False, None, shareLevelPersonForm, None, None

    shareLevelChoosePerson = ShareLevelChoosePerson(request.POST or None,
                                                    people=people)
    shareLevelClassForm = ShareLevelClass(request.POST or None, classes=classes)

    if request.method == 'POST':
        if "share-level-person" in request.POST and shareLevelPersonForm.is_valid():
            choosePerson, shareLevelChoosePerson, message \
                = handleSharedLevelPerson(request, shareLevelPersonForm)
            people = User.objects.filter(first_name=shareLevelPersonForm.data['name'],
                                         last_name=shareLevelPersonForm.data['surname'])
            shareLevelChoosePerson = ShareLevelChoosePerson(request.POST or None, people=people)
        if "share-level-class" in request.POST and shareLevelClassForm.is_valid():
            message = handleSharedLevelClass(request, shareLevelClassForm)
        if "level-choose-person" in request.POST and shareLevelChoosePerson.is_valid():
            message = handleChoosePerson(request, shareLevelChoosePerson)
    return choosePerson, shareLevelClassForm, shareLevelPersonForm, shareLevelChoosePerson, message


def handleSharedLevelPerson(request, form):
    level = get_object_or_404(Level, id=form.data['level'])
    people = User.objects.filter(first_name=form.data['name'], last_name=form.data['surname'])
    message = None
    choosePerson = False
    peopleLen = len(people)
    shareLevelChoosePerson = ShareLevelChoosePerson(request.POST or None,
                                                    people=User.objects.none())
    if peopleLen == 0:
        message = messages.shareUnsuccessfulPerson(form.data['name'], form.data['surname'])
    elif peopleLen == 1:
        level.shared_with.add(people[0])
        message = messages.shareSuccessfulPerson(form.data['name'], form.data['surname'])
    else:
        shareLevelChoosePerson = ShareLevelChoosePerson(request.POST or None, people=people)
        choosePerson = True
    return choosePerson, shareLevelChoosePerson, message


def handleSharedLevelClass(request, form):
    class_ = get_object_or_404(form.data.get('classes', False))
    level = get_object_or_404(form.data.get('levels', False))
    students = class_.students.all()
    for student in students:
        level.shared_with.add(student.user.user)
    return messages.shareSuccessfulClass(class_.name)


def handleChoosePerson(request, form):
    people = get_object_or_404(User, id=form.data['people'])
    level = get_object_or_404(Level, id=form.data['level'])
    level.shared_with.add(people)
    return messages.shareSuccessfulPerson(people.first_name, people.last_name)


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


def render_student_info(request):
    """ Helper method for rendering the studend info for a logged-in teacher."""
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


def parseInstructions(instructions, attempt, init):
    """ Helper method for inserting user-submitted instructions to the database."""

    if not instructions:
        return
    command = None
    index = init

    for instruction in instructions:
        next = index + 1

        if instruction['command'] == 'Forward':
            command = Command(step=index, attempt=attempt, command='Forward', next=index+1)
        elif instruction['command'] == 'Left':
            command = Command(step=index, attempt=attempt, command='Left', next=index+1)
        elif instruction['command'] == 'Right':
            command = Command(step=index, attempt=attempt, command='Right', next=index+1)
        elif instruction['command'] == 'TurnAround':
            command = Command(step=index, attempt=attempt, command='TurnAround', next=index+1)
        elif instruction['command'] == 'Wait':
            command = Command(step=index, attempt=attempt, command='Wait', next=index+1)

        elif instruction['command'] == 'While':
            condition = instruction['condition']
            parseInstructions(instruction['block'], attempt, next)
            execBlock = range(index + 1, index + len(instruction['block']) + 1)
            command = Command(step=index, attempt=attempt, command='While', condition=condition,
                              next=index+len(execBlock)+1, executedBlock1=execBlock)
            index += len(execBlock)

        elif instruction['command'] == 'If':
            condition = instruction['condition']
            parseInstructions(instruction['ifBlock'], attempt, next)
            next += len(instruction['ifBlock'])
            ifBlock = range(index + 1, next)

            if 'elseBlock' in instruction:
                parseInstructions(instruction['elseBlock'], attempt, next)
                next += len(instruction['elseBlock'])
                elseBlock = range(index + len(ifBlock) + 1, next + 2)
                command = Command(step=index, attempt=attempt, condition=condition, command='If',
                                  executedBlock1=ifBlock, executedBlock2=elseBlock, )
                index += len(elseBlock)
            else:
                command = Command(step=index, attempt=attempt, command='If', condition=condition,
                                  executedBlock1=ifBlock, next=next)
            index += len(ifBlock)

        else:
            command = Command(step=index, attempt=attempt, command='Forward', next=index+1)
        command.save()
        index += 1
    last = Command.objects.get(step=init+len(instructions)- 1, attempt=attempt)
    last.next = None
    last.save()


class WorkspaceViewList(generics.ListCreateAPIView):
    """ Handles requests for the list of workspace objects viewable by the user"""
    permission_classes = (permissions.IsAuthenticated,
                          UserIsStudent,
                          WorkspacePermissions,)

    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        user = self.request.user.userprofile.student
        return Workspace.objects.filter(owner=user)

    def post(self, request, format=None):
        serializer = WorkspaceSerializer(Workspace(owner=request.user.userprofile.student),
                                         data=request.DATA, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkspaceViewDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Handles requests for a specific workspace object"""
    permission_classes = (permissions.IsAuthenticated,
                          UserIsStudent,
                          WorkspacePermissions,)

    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        user = self.request.user.userprofile.student
        return Workspace.objects.filter(owner=user)

    def put(self, request, pk, format=None):
        workspace = self.get_object()
        serializer = WorkspaceSerializer(workspace, data=request.DATA, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


def get_list_of_levels_for_editor(request):
    if request.user.is_anonymous() or not hasattr(request.user, "userprofile"):
        ownedLevels = []
        sharedLevels = []
    else:
        ownedLevels = Level.objects.filter(owner=request.user.userprofile.id)
        sharedLevels = request.user.shared.all()

    owned = [{'name': level.name, 'owner': level.owner.user.first_name, 'id': level.id}
             for level in ownedLevels]
    shared = [{'name': level.name, 'owner': level.owner.user.first_name, 'id': level.id}
              for level in sharedLevels]

    response = {'ownedLevels': owned, 'sharedLevels': shared}
    return HttpResponse(json.dumps(response), content_type='application/javascript')


def get_level_for_editor(request, levelID):
    if request.user.is_anonymous() or not hasattr(request.user, "userprofile"):
        response = ""
    else:
        level = Level.objects.get(id=levelID)
        if(level.owner == request.user.userprofile or request.user.shared.get(id=levelID)):
            response = level
        else:
            response = ''

    return HttpResponse(json.dumps(model_to_dict(response)), content_type='application/javascript')


def delete_level_for_editor(request, levelID):
    if not request.user.is_anonymous() and hasattr(request.user, "userprofile"):
        level = Level.objects.get(id=levelID)
        if(level.owner == request.user.userprofile):
            level.delete()

    return HttpResponse('', content_type='application/javascript')


def save_level_for_editor(request, levelID=None):
    """ Processes a request on creation of the map in the level editor """

    path = request.POST.get('path')
    destinations = request.POST.get('destinations')
    decor = request.POST.get('decor')
    traffic_lights = request.POST.get('traffic_lights')
    max_fuel = request.POST.get('max_fuel')
    theme_id = request.POST.get('themeID')
    character_name = request.POST.get('character_name')
    blockTypes = json.loads(request.POST['block_types'])

    theme = Theme.objects.get(id=theme_id)
    character = Character.objects.get(name=character_name)

    if levelID is not None:
        level = Level.objects.get(id=levelID)

        if request.user.userprofile != level.owner:
            return

    else:
        name = request.POST.get('name')
        level = Level(name=name, default=False)

        if not request.user.is_anonymous():
            level.owner = request.user.userprofile

    level.path = path
    level.destinations = destinations
    level.max_fuel = max_fuel
    level.traffic_lights = traffic_lights
    level.theme = theme
    level.character = character
    level.save()

    setLevelDecor(level, decor)

    level.blocks = Block.objects.filter(type__in=blockTypes)
    level.save()

    return HttpResponse(json.dumps({'id': level.id}), content_type='application/javascript')

def generate_random_map_for_editor(request):
    """Generates a new random path suitable for a random level with the parameters provided"""

    size = int(request.POST['numberOfTiles'])
    branchiness = float(request.POST['branchiness'])
    loopiness = float(request.POST['loopiness'])
    curviness = float(request.POST['curviness'])
    traffic_lights_enabled = request.POST['trafficLightsEnabled']

    data = random_road.generate_random_map_data(size, branchiness, loopiness, curviness,
                                                traffic_lights_enabled)
    return HttpResponse(json.dumps(data), content_type='application/javascript')


def get_sharing_information_for_editor(request, levelID):
    level = Level.objects.get(id=levelID)

    valid_recipients = []
    active_recipients = []

    if level.owner == request.user.userprofile:
        valid_recipients = get_all_valid_recipients(request.user.userprofile)

    data = {'valid_recipients': valid_recipients, 'active_recipients': active_recipients}

    return HttpResponse(json.dumps(data), content_type='application/javascript')

def share_level_for_editor(request, levelID):
    pass


#######################
# Sharing permissions #
#######################

def get_all_valid_recipients(userprofile):

    valid_recipients = []

    if hasattr(userprofile, 'student'):
        student = userprofile.student

        # First get all the student's classmates
        class_ = student.class_field
        classmates = Student.objects.filter(class_field=class_).exclude(id=student.id)
        valid_recipients.extend(classmates)

        # Then add their teacher as well
        teacher = class_.teacher
        valid_recipients.append(teacher)

    elif hasattr(userprofile, 'teacher'):
        teacher = userprofile.teacher

        # First get all the students they teach
        classes_taught = Class.object.filter(teacher=teacher)
        students_taught = Students.object.filter(class_field__in=classes_taught)
        valid_recipients.extend(students_taught)

        # Then add all the teachers at the same organisation
        fellow_teachers = Teacher.object.filter(school=teacher.school)
        valid_recipients.extend(fellow_teachers)


    return [];

def is_valid_recipient():
    return False;


##################
# Helper methods #
##################

def getDecorElement(name, theme):
    """ Helper method to get a decor element corresponding to the theme or a default one."""
    try:
        return Decor.objects.get(name=name, theme=theme)
    except ObjectDoesNotExist:
        return Decor.objects.filter(name=name)[0]


def setLevelDecor(level, decorString):
    """ Helper method creating LevelDecor objects given a string of all decors."""

    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"name": *")([a-zA-Z0-9]+)("}))')
    items = regex.findall(decorString)

    existingDecor = LevelDecor.objects.filter(level=level)
    for levelDecor in existingDecor:
        levelDecor.delete()

    for item in items:
        name = item[6]
        levelDecor = LevelDecor(level=level, x=item[2], y=item[4], decorName=name)
        levelDecor.save()


def parseDecor(theme, levelDecors):
    """ Helper method parsing decor into a format 'sendable' to javascript.
    """
    decorData = []
    for levelDecor in levelDecors:
        decor = Decor.objects.get(name=levelDecor.decorName, theme=theme)
        decorData.append(json.dumps(
            {"coordinate": {"x": levelDecor.x, "y": str(levelDecor.y)}, "url": decor.url,
             "width": decor.width, "height": decor.height}))
    return decorData