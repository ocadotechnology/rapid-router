from __future__ import division
import game.messages as messages
import game.permissions as permissions

from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from helper import renderError
from game.forms import ScoreboardForm
from game.models import Level, Attempt
from portal.models import Class, Teacher


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

    userprofile = request.user.userprofile

    school = None
    thead = []
    classes = []
    if hasattr(userprofile, 'teacher'):
        school = request.user.userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        classes = Class.objects.filter(id__in=classes_list)
        if len(classes) <= 0:
            return renderError(request, messages.noPermissionTitle(), messages.noDataToShow())
    elif hasattr(userprofile, 'student') and not userprofile.student.is_independent():
        # user is a school student
        class_ = userprofile.student.class_field
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
    userprofile = request.user.userprofile

    studentData = None
    levelID = form.data.get('levels', False)
    classID = form.data.get('classes', False)
    thead = ['Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']
    if classID:
        cl = get_object_or_404(Class, id=classID)
        students = cl.students.all()
    # check user has permission to look at this class!
    if hasattr(userprofile, 'teacher'):
        teachers = Teacher.objects.filter(school=userprofile.teacher.school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        if classID and not int(classID) in classes_list:
            raise Http404
    elif hasattr(userprofile, 'student') and not userprofile.student.is_independent():
        # user is a school student
        class_ = userprofile.student.class_field
        if classID and int(classID) != class_.id:
            raise Http404
        students = class_.students.all()
        # remove all students except this student from students if the class config doesn't allow
        # for students to see classmates' data
        if not class_.classmates_data_viewable:
            students = students.filter(id=userprofile.student.id)
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
        row.append(attempt.score if attempt.score is not None else '')
        row.append(chop_miliseconds(attempt.finish_time - attempt.start_time))
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
                row[1] += attempt.score if attempt.score is not None else 0
                row[2].append(chop_miliseconds(attempt.finish_time - attempt.start_time))
                row.append(attempt.score)
                row[3].append(attempt.score if attempt.score is not None else '')
            except ObjectDoesNotExist:
                row[2].append(timedelta(0))
                row.append("")
                row[3].append("")
    for row in studentData:
        row[2] = sum(row[2], timedelta())
    return studentData


def chop_miliseconds(delta):
    delta = delta - timedelta(microseconds=delta.microseconds)
    return delta


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
    userprofile = request.user.userprofile

    studentData = []
    classes = []
    if hasattr(userprofile, 'student'):
        # Students can only see at most their classmates
        classes = [userprofile.student.class_field]
    elif hasattr(userprofile, 'teacher'):
        # Allow teachers to see school stats
        school = userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

    for cl in classes:
        students = cl.students.all()
        if (hasattr(userprofile, 'student') and
                not userprofile.student.class_field.classmates_data_viewable):
            # Filter out other students' data if not allowed to see classmates
            students = students.filter(id=userprofile.student.id)
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
    userprofile = request.user.userprofile

    studentData = []
    if hasattr(userprofile, 'student'):
        # Students can only see at most their classmates
        classes = [userprofile.student.class_field]
    elif hasattr(userprofile, 'teacher'):
        # allow teachers to see school stats
        school = userprofile.teacher.school
        teachers = Teacher.objects.filter(school=school)
        classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

    for cl in classes:
        students = cl.students.all()
        if (hasattr(userprofile, 'student') and
                not userprofile.student.class_field.classmates_data_viewable):
            # Filter out other students' data if not allowed to see classmates
            students = students.filter(id=userprofile.student.id)
        for student in students:
            studentData.append([student, 0.0, [], []])
    return createRows(studentData, levels)
