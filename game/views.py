import os
import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from forms import AvatarUploadForm, AvatarPreUploadedForm
from models import Class, Level, Attempt, Command, Block

def levels(request):
    context = RequestContext(request, {
        'levels': Level.objects.order_by('id'),
    })
    return render(request, 'game/level_selection.html', context)

def level(request, level):
    lvl = get_object_or_404(Level, id=level)
    path = lvl.path
    blocks = lvl.blocks.order_by('id')
    attempt = None

    #FIXME: figure out how to check for all this better
    if not request.user.is_anonymous() and hasattr(request.user, 'userprofile') and hasattr(request.user.userprofile, 'student'):
        student = request.user.userprofile.student
        try:
            attempt = get_object_or_404(Attempt, level=lvl, student=student)
        except Http404:
            attempt = Attempt(level=lvl, score=0, student=student)
            attempt.save()

    context = RequestContext(request, {
        'level': lvl.id,
        'path': path,
        'blocks': blocks,
    })

    return render(request, 'game/game.html', context)

def level_new(request):
    """ Processes a request on creation of the map in the level editor."""
    if 'path' in request.POST:
        path = request.POST.get('path', False)
        passedLevel = Level(name=10, path=path)
        passedLevel.save()

        # Insert all the blockly blocks as available to use.
        for a in range(1, 12):
            passedLevel.blocks.add(get_object_or_404(Block, id=a))

        passedLevel.save()
        response_dict = {}
        response_dict.update({'server_response': passedLevel.id})
        return HttpResponse(json.dumps(response_dict), content_type='application/javascript')

def submit(request):
    """ Processes a request on submission of the program solving the current level."""
    if request.method == 'POST':
        attemptJson = request.POST.get('attemptData', False)
        attemptData = json.loads(attemptJson)
        parseAttempt(attemptData, request)
        return HttpResponse(attemptJson, content_type='application/javascript')

def parseAttempt(attemptData, request):
    level = get_object_or_404(Level, id=attemptData.get('level', 1))
    attempt = get_object_or_404(Attempt, level=level, student=request.user.userprofile.student)

    # Remove all the old commands from previous attempts.
    Command.objects.filter(attempt=attempt).delete()
    parseInstructions(json.loads(attemptData.get('commandStack', "")), attempt, 1)
    attempt.save()


def logged_students(request):
    """ Renders the page with information about all the logged in students."""
    return render_student_info(request, True)

def students_in_class(request):
    """ Renders the page with information about all the students enrolled in a chosen class."""
    return render_student_info(request, False)

def level_editor(request):
    return render(request, 'game/level_editor.html')

def settings(request):
    """ Renders the settings page.  """
    x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(x, 'static/game/image/Avatars/')
    img_list = os.listdir(path)
    avatar = None
    userProfile = request.user.userprofile
    avatarUploadForm = AvatarUploadForm(request.POST or None, request.FILES)
    avatarPreUploadedForm = AvatarPreUploadedForm(request.POST or None, my_choices=img_list)

    if request.method == 'POST':
        if "pre-uploaded" in request.POST:
            if avatarPreUploadedForm.is_valid:
                avatar = avatarPreUploadedForm.data.get('pre-uploaded', False)
        else:
            if avatarUploadForm.is_valid() and "user-uploaded" in request.POST:
                avatar = request.FILES.get('avatar', False)
        userProfile.avatar = avatar
        userProfile.save()

    context = RequestContext(request, {
        'avatarPreUploadedForm': avatarPreUploadedForm,
        'avatarUploadForm': avatarUploadForm,
        'user': request.user,
    })
    return render(request, 'game/settings.html', context)

def render_student_info(request, logged):
    """ Helper method for rendering the studend info for a logged-in teacher."""
    user = request.user
    message = "Choose a class you want to see."
    currentClass = ""
    students = []

    if request.method == 'POST':
        cl = get_object_or_404(Class, id=request.POST.getlist('classes')[0])
        students = cl.get_logged_in_students() if logged else cl.students.all()
        currentClass = cl.name
    try:
        classes = user.userprofile.teacher.class_teacher.all()
    except ObjectDoesNotExist:
        message = "You don't have permissions to see this."

    context = RequestContext(request, {
        'classes': classes,
        'message': message,
        'students': students,
        'currentClass': currentClass,
    })
    return render(request, 'game/logged_students.html', context)

def parseInstructions(instructions, attempt, init):
    """ Helper method for inserting user-submitted instructions to the database."""
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
                command = Command(step=index, attempt=attempt, condition=condition,
                    command='If', executedBlock1=ifBlock, executedBlock2=elseBlock, next=next)
                index += len(elseBlock)
            else:
                command = Command(step=index, attempt=attempt, command='If', condition=condition,
                    executedBlock1=ifBlock, next=next)
            index += len(ifBlock)

        else:
            command = Command(step=index, attempt=attempt, command='Forward', next=index+1)
        command.save()
        index += 1
    last = Command.objects.get(step=init+len(instructions) - 1, attempt=attempt)
    last.next = None
    last.save()
