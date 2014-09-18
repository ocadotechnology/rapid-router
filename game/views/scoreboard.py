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
from game.models import Level, Attempt, Episode
from portal.models import Class, Teacher


def scoreboard(request):
    """ Renders a page with students' scores.

    **Context**

    ``RequestContext``
    ``form``
        Form used to choose a class and level to show. Instance of `forms.ScoreboardForm.`
    ``student_data``
        List of lists containing all the data to be stored in the scoreboard table.
    ``thead``
        List of Strings representing the headers of the scoreboard table.

    **Template:**

    :template:`game/scoreboard.html`
    """
    if not permissions.can_see_scoreboard(request.user):
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())

    form, student_data, thead = create_scoreboard(request)

    context = RequestContext(request, {
        'form': form,
        'student_data': student_data,
        'thead': thead,
    })
    return render(request, 'game/scoreboard.html', context_instance=context)


def create_scoreboard(request):

    def render_scoreboard(request, form, school):
        """ Helper method rendering the scoreboard.
        """
        userprofile = request.user.userprofile
        student_data = None
        level_id = form.data.get('levels', False)
        class_id = form.data.get('classes', False)

        # Adjust the table headers to the chosen parameters.
        if not level_id:
            thead = ['Name', 'Total Score', 'Total Time']
        else:
            thead = ['Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']

        if class_id:
            cl = get_object_or_404(Class, id=class_id)
            students = cl.students.all()

        if level_id:
            level = get_object_or_404(Level, id=level_id)

        if hasattr(userprofile, 'teacher'):
            teachers = Teacher.objects.filter(school=userprofile.teacher.school)
            classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
            if class_id and not int(class_id) in classes_list:
                raise Http404

        elif hasattr(userprofile, 'student') and not userprofile.student.is_independent():
            class_ = userprofile.student.class_field
            if class_id and int(class_id) != class_.id:
                raise Http404
            # If student is allowed to see other pupils' data
            if class_.classmates_data_viewable:
                students = class_.students.all()
            else:

                class_.students.filter(id=userprofile.student.id)
        else:
            raise Http404

        if class_id and level_id:
            student_data = one_class_one_level(students, level)
        elif level_id:
            student_data = all_classes_one_level(request, level)
        else:
            if userprofile.developer:
                episodes = Episode.objects.all()
            else:
                episodes = Episode.objects.filter(in_development=False)
            levels = []
            for episode in episodes:
                levels += episode.levels
            for level in levels:
                thead.append(str(level))
            if class_id:
                student_data = one_class_all_levels(students, levels)
            else:
                # TODO: Decide on how open do we want the scoreboard to be?
                student_data = all_classes_all_levels(request, levels)
        return student_data, thead

    def one_row(student, level):
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

    def many_rows(student_data, levels):
        """ Helper method getting overall result for students in student_data in given levels.
        """
        for row in student_data:
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
        for row in student_data:
            row[2] = sum(row[2], timedelta())
        return student_data

    def chop_miliseconds(delta):
        return delta - timedelta(microseconds=delta.microseconds)

    def one_class_one_level(students, level):
        """ Show scoreboard for a chosen level for students of one class.
        """
        student_data = []
        for student in students:
            row = one_row(student, level)
            student_data.append(row)
        return student_data

    def all_classes_one_level(request, level):
        """ Show all the students's (from the same school for now) performance on this level.
        """
        userprofile = request.user.userprofile

        student_data = []
        classes = []
        if is_student(userprofile):
            # Students can only see at most their classmates
            classes = [userprofile.student.class_field]
        elif is_teacher(userprofile):
            # Allow teachers to see school stats
            school = userprofile.teacher.school
            teachers = Teacher.objects.filter(school=school)
            classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

        for cl in classes:
            students = cl.students.all()
            if (is_student(userprofile) and
                    not userprofile.student.class_field.classmates_data_viewable):
                # Filter out other students' data if not allowed to see classmates
                students = students.filter(id=userprofile.student.id)
            for student in students:
                row = one_row(student, level)
                student_data.append(row)
        return student_data

    def one_class_all_levels(students, levels):
        """ Show statisctics for all students in a class across all levels (sum).
        """
        student_data = []
        for student in students:
            student_data.append([student, 0.0, [], []])
        return many_rows(student_data, levels)

    def all_classes_all_levels(request, levels):
        """ For now restricting it to the same school.
        """
        userprofile = request.user.userprofile

        student_data = []
        if is_student(userprofile):
            # Students can only see at most their classmates
            classes = [userprofile.student.class_field]
        elif is_teacher(userprofile):
            # allow teachers to see school stats
            school = userprofile.teacher.school
            teachers = Teacher.objects.filter(school=school)
            classes = [c for c in Class.objects.all() if (c.teacher in teachers)]

        for cl in classes:
            students = cl.students.all()
            if (is_student(userprofile) and
                    not userprofile.student.class_field.classmates_data_viewable):
                # Filter out other students' data if not allowed to see classmates
                students = students.filter(id=userprofile.student.id)
            for student in students:
                student_data.append([student, 0.0, [], []])
        return many_rows(student_data, levels)

    def is_student(userprofile):
        return hasattr(userprofile, 'student') and not userprofile.student.is_independent()

    def is_teacher(userprofile):
        return hasattr(userprofile, 'teacher')

    userprofile = request.user.userprofile
    school = None
    thead = []
    classes = []

    if is_teacher(userprofile):
        teachers = Teacher.objects.filter(school=userprofile.teacher.school)
        classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
        classes = Class.objects.filter(id__in=classes_list)
        if len(classes) <= 0:
            return renderError(request, messages.noPermissionTitle(), messages.noDataToShow())

    elif is_student(userprofile):
        class_ = userprofile.student.class_field
        classes = Class.objects.filter(id=class_.id)
        school = class_.teacher.school
    else:
        return renderError(request, messages.noPermissionTitle(), messages.noPermissionScoreboard())

    form = ScoreboardForm(request.POST or None, classes=classes)
    student_data = None

    # Update the scoreboard if the class and or level were selected.
    if request.method == 'POST':
        if form.is_valid():
            student_data, thead = render_scoreboard(request, form, school)

    return form, student_data, thead
