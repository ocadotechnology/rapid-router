import json
import os
import messages

from cache import cached_all_episodes, cached_level, cached_episode
from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.safestring import mark_safe
from forms import *
from game import random_road
from models import Class, Level, Attempt, Command, Block


def levels(request):
    """Loads a page with all levels listed.

    **Context**

    ``RequestContext``
    ``episodes``

    **Template:**

    :template:`game/level_selection.html`
    """
    context = RequestContext(request, {
        'episodes': cached_all_episodes()
    })
    return render(request, 'game/level_selection.html', context)


def level(request, level):
    """Loads a level for rendering in the game.

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
    if lvl.default:
        lesson = 'description_level' + str(level)
        hint = 'hint_level' + str(level)
    else:
        lesson = 'description_level_default'
        hint = 'hint_level_default'
    messageCall = getattr(messages, lesson)
    lesson = mark_safe(messageCall())
    messageCall = getattr(messages, hint)
    hint = mark_safe(messageCall())

    #FIXME: figure out how to check for all this better
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
        'hint': hint,
    })

    return render(request, 'game/game.html', context)


def level_editor(request):
    """Renders the level editor page.

    **Context**

    ``RequestContext``
    ``blocks``
        Blocks that can be chosen to be played with later on. List of :model:`game.Block`.

    **Template:**

    :template:`game/level_editor.html`
    """
    context = RequestContext(request, {
        'blocks': Block.objects.all()
    })
    return render(request, 'game/level_editor.html', context)


def renderError(request, title, message):
    """Renders an error page with passed title and message.

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
    return render(request, 'game/error.html', context)


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
        classes = request.user.userprofile.teacher.class_teacher.all()
        school = classes[0].school
    elif hasattr(request.user.userprofile, 'student'):
        class_ = request.user.userprofile.student.class_field
        school = class_.school
        classes = Class.objects.filter(id=class_.id)
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
    return render(request, 'game/scoreboard.html', context)


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
    message = "None"
    levels = Level.objects.filter(owner=request.user.userprofile.id)
    avatarUploadForm, avatarPreUploadedForm = renderAvatarChoice(request)
    shareLevelClassForm, shareLevelPersonForm, message = renderLevelSharing(request)
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
        'levels': levels,
        'sharedLevels': sharedLevels,
        'user': request.user,
        'levelMessage': levelMessage,
        'sharedLevelMessage': sharedMessage,
        'message': message,
        'title': title
    })
    return render(request, 'game/settings.html', context)


def level_random(request):
    """Generates a new random level

    Redirects to :view:`game.views.level` with the id of the newly created :model:`game.Level`.
    """
    level = random_road.create()
    return redirect("game.views.level", level=level.id)


def start_episode(request, episode):
    episode = cached_episode(episode)
    return redirect("game.views.level", level=episode.first_level.id)


def submit(request):
    """ Processes a request on submission of the program solving the current level.
    """
    if not request.user.is_anonymous() and request.method == 'POST' \
            and 'attemptData' in request.POST:
        attemptJson = request.POST['attemptData']
        attemptData = json.loads(attemptJson)
        parseAttempt(attemptData, request)
        return HttpResponse(attemptJson, content_type='application/javascript')
    return HttpResponse('')


def level_new(request):
    """Processes a request on creation of the map in the level editor.
    """
    if 'nodes' in request.POST:
        path = request.POST['nodes']
        destination = request.POST['destination']
        decor = request.POST['decor']
        max_fuel = request.POST['maxFuel']
        name = request.POST.get('name')
        passedLevel = None
        passedLevel = Level(name=name, path=path, default=False, destination=destination,
                            decor=decor, max_fuel=max_fuel)

        if not request.user.is_anonymous() and hasattr(request.user, 'userprofile'):
            passedLevel.owner = request.user.userprofile
        passedLevel.save()

        if 'blockTypes' in request.POST:
            blockTypes = json.loads(request.POST['blockTypes'])
            blocks = Block.objects.filter(type__in=blockTypes)
        else:
            blocks = Block.objects.all()

        passedLevel.blocks = blocks
        passedLevel.save()

        response_dict = {}
        response_dict.update({'server_response': passedLevel.id})
        return HttpResponse(json.dumps(response_dict), content_type='application/javascript')


#
# Helper methods for rendering views in the game.
#


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
    if levelID:
        level = get_object_or_404(Level, id=levelID)

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
        pass
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
                pass
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
        school = request.user.userprofile.student.class_field.school
        classes = school.class_school.all()
    elif hasattr(request.user.userprofile, 'teacher'):
        classes = request.user.userprofile.teacher.class_teacher.all()

    for cl in classes:
        students = cl.students.all()
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
        school = request.user.userprofile.student.class_field.school
        classes = school.class_school.all()
    elif hasattr(request.user.userprofile, 'teacher'):
        classes = request.user.userprofile.teacher.class_teacher.all()

    for cl in classes:
        students = cl.students.all()
        for student in students:
            studentData.append([student, 0.0, [], []])
    return createRows(studentData, levels)


def handleSharedLevelPerson(request, form):
    level = get_object_or_404(Level, id=form.data['level'])
    people = User.objects.filter(first_name=form.data['name'], last_name=form.data['surname'])
    message = None
    peopleLen = len(people)
    if peopleLen == 0:
        message = messages.shareUnsuccessfulPerson(form.name, form.surname)
    elif peopleLen == 1:
        level.shared_with.add(people[0])
        message = messages.shareSuccessfulPerson(form.data['name'], form.data['surname'])
    else:
        message = "Say whaaaaat"
    return message


def handleSharedLevelClass(request, form):
    classID = form.data.get('classes', False)
    levelID = form.data.get('levels', False)
    cl = get_object_or_404(Class, id=classID)
    level = get_object_or_404(Level, id=levelID)
    students = cl.students.all()
    for student in students:
        level.shared_with.add(student.user.user)
    return messages.shareSuccessfulClass(cl.name)


def renderLevelSharing(request):
    classes = None
    message = ""
    userProfile = request.user.userprofile
    shareLevelPersonForm = ShareLevelPerson(request.POST or None)
    if hasattr(userProfile, "teacher"):
        classes = userProfile.teacher.class_teacher.all()
    elif hasattr(userProfile, "student"):
        classesObj = userProfile.student.class_field
        classes = Class.objects.filter(pk=classesObj.id)
    else:
        return None, shareLevelPersonForm
    shareLevelClassForm = ShareLevelClass(request.POST or None, classes=classes)
    if request.method == 'POST':
        if "share-level-person" in request.POST and shareLevelPersonForm.is_valid():
            message = handleSharedLevelPerson(request, shareLevelPersonForm)
        if "share-level-class" in request.POST and shareLevelClassForm.is_valid():
            message = handleSharedLevelClass(request, shareLevelClassForm)
    return shareLevelClassForm, shareLevelPersonForm, message


def parseAttempt(attemptData, request):
    level = get_object_or_404(Level, id=attemptData.get('level', 1))
    attempt = get_object_or_404(Attempt, level=level, student=request.user.userprofile.student)
    attempt.score = request.POST.get('score', 0)

    # Remove all the old commands from previous attempts.
    Command.objects.filter(attempt=attempt).delete()
    commands = attemptData.get('commandStack', None)
    parseInstructions(json.loads(commands), attempt, 1)
    attempt.save()


def renderAvatarChoice(request):
    """ Helper method for settings view. Generates and processes the avatar changing forms.
    """
    x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(x, 'static/game/image/Avatars')
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
