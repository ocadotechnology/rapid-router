from __future__ import division
import game.messages as messages
import game.permissions as permissions
import csv

from datetime import timedelta
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from helper import renderError
from game.forms import ScoreboardForm
from game.models import Level, Attempt, Episode
from portal.models import Class, Teacher


def scoreboard(request):
    """ Renders a page with students' scores. A teacher can see the the visible classes in their
        school. Student's view is restricted to their class if their teacher enabled the
        scoreboard for said class.

    **Context**

    ``RequestContext``
    ``form``
        Form used to choose a class and level to show. Instance of `forms.ScoreboardForm.`
    ``student_data``
        List of lists containing all the data to be stored in the scoreboard table.
    ``headers``
        List of Strings representing the headers of the scoreboard table.

    **Template:**

    :template:`game/scoreboard.html`
    """
    if not permissions.can_see_scoreboard(request.user):
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())

    form, student_data, headers, error_response = create_scoreboard(request)

    if error_response:
        return error_response

    if 'export' in request.POST:
        return get_scoreboard_csv(student_data, headers)
    else:
        return get_scoreboard_view(request, form, student_data, headers)

def get_scoreboard_view(request, form, student_data, headers):
    context = RequestContext(request, {
        'form': form,
        'student_data': student_data,
        'headers': headers,
    })
    return render(request, 'game/scoreboard.html', context_instance=context)
    
def get_scoreboard_csv(student_data, headers):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'
    
    #remove list element with list of level scores (the following elements hold the same data separately)
    if headers[1] != 'Score':
        for row in student_data:
            del row[3]

    writer = csv.writer(response)
    writer.writerow(headers)
    writer.writerows(student_data)

    return response

def create_scoreboard(request):

    def populate_scoreboard(request, form, school):

        userprofile = request.user.userprofile
        student_data = None
        level_id = form.data.get('levels', False)
        class_id = form.data.get('classes', False)

        if not level_id:
            headers = ['Name', 'Total Score', 'Total Time']
        else:
            headers = ['Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']

        if class_id:
            cl = get_object_or_404(Class, id=class_id)
            students = cl.students.all()

        if level_id:
            level = get_object_or_404(Level, id=level_id)

        if is_teacher(userprofile):
            teachers = Teacher.objects.filter(school=userprofile.teacher.school)
            classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
            if class_id and not int(class_id) in classes_list:
                raise Http404

        elif is_student(userprofile):
            class_ = userprofile.student.class_field
            if class_id and int(class_id) != class_.id:
                raise Http404
            students = class_.students.all()
            if not is_viewable(class_):
                students = class_.students.filter(id=userprofile.student.id)
        else:
            raise Http404

        if class_id and level_id:
            student_data = one_class_one_level(students, level)
        elif not class_id and level_id:
            student_data = all_classes_one_level(request, level)
        elif class_id and not level_id:
            levels, headers = get_levels(userprofile, headers)
            student_data = one_class_all_levels(students, levels)
        elif not class_id and not level_id:
            levels, headers = get_levels(userprofile, headers)
            student_data = all_classes_all_levels(request, levels)
        return student_data, headers

    def one_row(student, level):
        row = [student]

        attempt = Attempt.objects.filter(level=level, student=student).first()
        if attempt:
            row.append(attempt.score if attempt.score is not None else '')
            row.append(chop_miliseconds(attempt.finish_time - attempt.start_time))
            row.append(attempt.start_time)
            row.append(attempt.finish_time)
        else:
            row.append("")
            row.append("")
            row.append("")
            row.append("")

        return row

    def many_rows(student_data, levels):
        for row in student_data:
            for level in levels:
                student = row[0]
                attempt = Attempt.objects.filter(level=level, student=student).first()
                if attempt:
                    row[1] += attempt.score if attempt.score is not None else 0
                    row[2].append(chop_miliseconds(attempt.finish_time - attempt.start_time))
                    row.append(attempt.score if attempt.score is not None else '')
                    row[3].append(attempt.score if attempt.score is not None else '')
                else:
                    row[2].append(timedelta(0))
                    row.append("")
                    row[3].append("")

        for row in student_data:
            row[2] = sum(row[2], timedelta())

        return student_data

    def one_class_one_level(students, level):
        student_data = []
        for student in students:
            row = one_row(student, level)
            student_data.append(row)
        return student_data

    def all_classes_one_level(request, level):
        userprofile = request.user.userprofile
        student_data = []
        classes = []

        if is_student(userprofile):
            classes = [userprofile.student.class_field]
        elif is_teacher(userprofile):
            school = userprofile.teacher.school
            teachers = Teacher.objects.filter(school=school)
            classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

        for cl in classes:
            students = cl.students.all()
            if is_student(userprofile) and not is_viewable(userprofile.student.class_field):
                students = students.filter(id=userprofile.student.id)
            for student in students:
                row = one_row(student, level)
                student_data.append(row)

        return student_data

    def one_class_all_levels(students, levels):
        student_data = []
        for student in students:
            student_data.append([student, 0.0, [], []])
        return many_rows(student_data, levels)

    def all_classes_all_levels(request, levels):
        userprofile = request.user.userprofile
        student_data = []

        if is_student(userprofile):
            classes = [userprofile.student.class_field]
        elif is_teacher(userprofile):
            school = userprofile.teacher.school
            teachers = Teacher.objects.filter(school=school)
            classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

        for cl in classes:
            students = cl.students.all()
            if is_student(userprofile) and not is_viewable(userprofile.student.class_field):
                students = students.filter(id=userprofile.student.id)
            for student in students:
                student_data.append([student, 0.0, [], []])
        return many_rows(student_data, levels)

    def get_levels(userprofile, headers):
        levels = Level.objects.sorted_levels()
        headers += levels

        return levels, headers

    def is_viewable(class_):
        return class_.classmates_data_viewable

    def chop_miliseconds(delta):
        return delta - timedelta(microseconds=delta.microseconds)

    def is_student(userprofile):
        return hasattr(userprofile, 'student') and not userprofile.student.is_independent()

    def is_teacher(userprofile):
        return hasattr(userprofile, 'teacher')

    userprofile = request.user.userprofile
    school = None
    headers = []
    classes = []

    if is_teacher(userprofile):
        teachers = Teacher.objects.filter(school=userprofile.teacher.school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        classes = Class.objects.filter(id__in=classes_list)
        if len(classes) <= 0:
            return None, None, None, renderError(request, messages.noPermissionTitle(), messages.noDataToShow())

    elif is_student(userprofile):
        class_ = userprofile.student.class_field
        classes = Class.objects.filter(id=class_.id)
        school = class_.teacher.school

    else:
        return None, None, None, renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())

    form = ScoreboardForm(request.POST or None, classes=classes)
    student_data = None

    # Update the scoreboard if the class and or level were selected.
    if request.method == 'POST':
        if form.is_valid():
            student_data, headers = populate_scoreboard(request, form, school)

    return form, student_data, headers, None
