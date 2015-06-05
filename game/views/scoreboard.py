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
from portal.models import Class, Teacher, Student


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

    def are_classes_viewable_by_teacher(class_ids, userprofile):
        teachers = Teacher.objects.filter(school=userprofile.teacher.school)
        classes_list = Class.objects.filter(teacher__in=teachers).values_list('id', flat=True)
        for class_id in class_ids:
            if class_id and not class_id in classes_list:
                return False
        return True

    def populate_scoreboard(request):

        # Getting data from the request object
        userprofile = request.user.userprofile
        level_ids = map(int, request.POST.getlist('levels'))
        class_ids = map(int, request.POST.getlist('classes'))

        # Get the list of students and levels to be displayed
        # As the list passed by the multiselect is in order, using a for loop will preserve the order and
        # only get the default levels instead of the custom levels as well
        # Django 1.7 does not support sorting queryset by converting strings to int
        # Django 1.8 supports the use of expressios in order_by, should try using that to write cleaner codes
        # https://docs.djangoproject.com/en/1.8/releases/1.8/#query-expressions-conditional-expressions-and-database-functions

        students = Student.objects.filter(class_field__id__in = class_ids)

        levels = Level.objects.filter(id__in=level_ids)

        # Check that all the classes selected are valid
        if is_teacher(userprofile):
            if not are_classes_viewable_by_teacher(class_ids, userprofile):
                raise Http404

        # Retrieve the class that the student is in, check that the class selected in drop down menu is the same
        # Each student can only be in one class at a time, so there will be only be one element in the list
        elif is_student(userprofile):
            class_ = userprofile.student.class_field
            if class_ids[0] and int(class_ids[0]) != class_.id:
                raise Http404
            students = class_.students.all()
            # If student is not permitted to look at other students' score, it will only show the student's own data
            if not is_viewable(class_):
                students = class_.students.filter(id=userprofile.student.id)
        else:
            raise Http404
        # If there are more than one level to show, show the total score, total time and score of each level
        # Otherwise, show the details of the level (the score, total time, start time and end time)
        if len(level_ids) > 1:
            # Rows: Students from each class
            # Cols: Total Score, Total Time, Level X, ... , Level Y
            headers = get_levels_headers(['Name', 'Total Score', 'Total Time', 'Progress'], levels)
            student_data = multiple_students_multiple_levels(students, level_ids)
        else:
            # Rows: Students from each class
            # Cols: Score, Total Time, Start Time, End Time
            headers = ['Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']
            student_data = multiple_students_one_level(students, level_ids[0])
        return student_data, headers

    def one_row(student, level_id):
        row = [student]

        attempt = Attempt.objects.filter(level__id=level_id, student=student).first()
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

    # many_rows return the
    def many_rows(student_data, level_ids):
        threshold = 10.0

        num_levels = len(level_ids)
        for row in student_data:
            student = row[0]
            num_all = num_finished = num_attempted = num_started = 0

            if Attempt.objects.filter(student=student).exists():
                attempts = Attempt.objects.filter(level__id__in=level_ids, student=student)

                attempts_dict = {attempt.level.id : attempt for attempt in attempts}
                for level in level_ids:
                    attempt = attempts_dict.get(level)
                    if attempt:
                        num_all += 1;
                        if attempt.score:
                            if attempt.score >= threshold:
                                num_finished += 1
                            else:
                                num_attempted += 1
                        else:
                            num_started += 1

                        row[1] += attempt.score if attempt.score is not None else 0
                        row[2].append(chop_miliseconds(attempt.finish_time - attempt.start_time))
                        # '-' is used to show that the student has started the level but has not submitted any attempts
                        row.append(attempt.score if attempt.score is not None else '-')
                        row[3].append(attempt.score if attempt.score is not None else '-')
                    else:
                        row[2].append(timedelta(0))
                        row.append("")
                        row[3].append("")

                row[4] = compute_proportions(num_levels, num_started, num_attempted, num_finished)
            else:
                row[3].extend([''] * num_levels)
        for row in student_data:
            row[2] = sum(row[2], timedelta())

        return student_data

    def compute_proportions(num_levels, num_started, num_attempted, num_finished):
        return (num_started/num_levels)*100, (num_attempted/num_levels)*100, (num_finished/num_levels)*100

    # Returns rows of student object with score, start time, end time of the level
    def multiple_students_one_level(students, level):
        student_data = []

        for student in students:
            student_data.append(one_row(student, level))

        return student_data

    # Return rows of student object with values for progress bar and scores of each selected level
    def multiple_students_multiple_levels(students, level_ids):
        student_data = []

        for student in students:
            student_data.append([student, 0.0, [], [], (0.0, 0.0, 0.0)])

        return many_rows(student_data, level_ids)


    def get_levels_headers(headers, levels):
        headers += levels
        return headers

    def is_viewable(class_):
        return class_.classmates_data_viewable

    def chop_miliseconds(delta):
        return delta - timedelta(microseconds=delta.microseconds)

    def is_student(userprofile):
        return hasattr(userprofile, 'student') and not userprofile.student.is_independent()

    def is_teacher(userprofile):
        return hasattr(userprofile, 'teacher')

    def is_independent_student(userprofile):
        return hasattr(userprofile, 'student') and userprofile.student.is_independent()

    def classes_for(userprofile):
        if is_teacher(userprofile):
            teachers = Teacher.objects.filter(school=userprofile.teacher.school)
            classes_list = [c.id for c in Class.objects.all() if (c.teacher in teachers)]
            return Class.objects.filter(id__in=classes_list)
        elif is_student(userprofile):
            class_ = userprofile.student.class_field
            return Class.objects.filter(id=class_.id)

    def error_response(message):
        return None, None, None, renderError(request, messages.noPermissionTitle(), message)

    userprofile = request.user.userprofile
    headers = []
    classes = classes_for(userprofile)

    if is_independent_student(userprofile):
        return error_response(messages.noPermissionScoreboard())

    if is_teacher(userprofile) and len(classes) == 0:
        return error_response(messages.noDataToShow())

    form = ScoreboardForm(request.POST or None, classes=classes)
    student_data = None

    # Update the scoreboard if the class and or level were selected.
    if request.method == 'POST':
        if form.is_valid():
            student_data, headers = populate_scoreboard(request)

    return form, student_data, headers, None
