from __future__ import division
import game.messages as messages
import game.permissions as permissions
import csv
from sets import Set

from datetime import timedelta
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from helper import renderError
from game.forms import ScoreboardForm
from game.models import Level, Attempt
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
    if headers[2] != 'Score':
        for row in student_data:
            del row[3]

    writer = csv.writer(response)
    writer.writerow(headers)
    writer.writerows(student_data)

    return response

def create_scoreboard(request):

    def are_classes_viewable_by_teacher(class_ids, userprofile):
        teachers = Teacher.objects.filter(school=userprofile.teacher.school)
        classes_in_teachers_school = Class.objects.filter(teacher__in=teachers).values_list('id', flat=True)
        for class_id in class_ids:
            is_authorised = class_id in classes_in_teachers_school
            if not is_authorised:
                return False
        return True

    def authorised_student_access(class_, class_ids):
        return len(class_ids) == 1 and class_ids[0] == class_

    def students_visible_to_student(student, class_):
        if is_viewable(class_):
            return class_.students.all().select_related('class_field', 'user__user')
        else:
            return [student]

    def students_visible_to_user(userprofile, class_ids):
        if is_teacher(userprofile):
            return Student.objects.filter(class_field__id__in = class_ids).select_related('class_field', 'user__user')
        elif is_student(userprofile):
            student = userprofile.student
            class_ = student.class_field
            return students_visible_to_student(student, class_)

    def is_valid_request(userprofile, class_ids):
        if is_teacher(userprofile):
            return are_classes_viewable_by_teacher(class_ids, userprofile)
        elif is_student(userprofile):
            return authorised_student_access(userprofile.student.class_field.id, class_ids)
        else:
            return False
        return True

    def populate_scoreboard(request):

        # Getting data from the request object
        userprofile = request.user.userprofile
        level_ids = Set(map(int, request.POST.getlist('levels')))
        class_ids = map(int, request.POST.getlist('classes'))

        # Get the list of students and levels to be displayed
        # As the list passed by the multiselect is in order, using a for loop will preserve the order and
        # only get the default levels instead of the custom levels as well
        # Django 1.7 does not support sorting queryset by converting strings to int
        # Django 1.8 supports the use of expressios in order_by, should try using that to write cleaner codes
        # https://docs.djangoproject.com/en/1.8/releases/1.8/#query-expressions-conditional-expressions-and-database-functions

        if not is_valid_request(userprofile, class_ids):
            raise Http404

        students = students_visible_to_user(userprofile, class_ids)
        levels = Level.objects.sorted_levels()

        requested_sorted_levels = filter(lambda x : x.id in level_ids, levels)
        sorted_level_ids = map(lambda level: level.id, requested_sorted_levels)

        # If there are more than one level to show, show the total score, total time and score of each level
        # Otherwise, show the details of the level (the score, total time, start time and end time)
        if len(level_ids) > 1:
            # Rows: Students from each class
            # Cols: Total Score, Total Time, Level X, ... , Level Y
            headers = get_levels_headers(['Class', 'Name', 'Total Score', 'Total Time', 'Progress'], requested_sorted_levels)
            student_data = multiple_students_multiple_levels(students, sorted_level_ids)
        else:
            # Rows: Students from each class
            # Cols: Score, Total Time, Start Time, End Time
            headers = ['Class', 'Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']
            student_data = multiple_students_one_level(students, next(iter(level_ids)))
        return student_data, headers

    def one_row(student, level_id):

        attempt = Attempt.objects.filter(level__id=level_id, student=student).first()
        if attempt:
            total_score = attempt.score if attempt.score is not None else ''
            return StudentRow(student=student,
                              total_score=total_score,
                              start_time=attempt.start_time,
                              finish_time=attempt.finish_time,
                              total_time=chop_miliseconds(attempt.finish_time - attempt.start_time))
        else:
            return StudentRow(student=student)

    # Return rows of student object with values for progress bar and scores of each selected level
    def multiple_students_multiple_levels(students, level_ids_sorted):
        result = map(lambda student: student_row(level_ids_sorted, student), students)
        return result

    def student_row(level_ids_sorted, student):
        threshold = 10.0

        num_levels = len(level_ids_sorted)
        num_all = num_finished = num_attempted = num_started = 0
        total_score = 0.0
        scores = []
        times = []
        progress = (0.0, 0.0, 0.0)
        attempts = Attempt.objects.filter(level__id__in=level_ids_sorted, student=student).select_related('level')
        if attempts:
            attempts_dict = {attempt.level.id: attempt for attempt in attempts}
            for level_id in level_ids_sorted:
                attempt = attempts_dict.get(level_id)
                if attempt:
                    num_all += 1;
                    if attempt.score:
                        if attempt.score >= threshold:
                            num_finished += 1
                        else:
                            num_attempted += 1
                    else:
                        num_started += 1

                    total_score += attempt.score if attempt.score is not None else 0

                    times.append(chop_miliseconds(attempt.elapsed_time()))
                    # '-' is used to show that the student has started the level but has not submitted any attempts

                    scores.append(attempt.score if attempt.score is not None else '-')
                else:
                    times.append(timedelta(0))
                    scores.append("")

            progress = compute_proportions(num_levels, num_started, num_attempted, num_finished)
        else:
            scores.extend([''] * num_levels)

        total_time = sum(times, timedelta())

        row = StudentRow(student=student,
                         total_time=total_time,
                         total_score=total_score,
                         progress=progress,
                         scores=scores)
        return row

    def compute_proportions(num_levels, num_started, num_attempted, num_finished):
        return (num_started/num_levels)*100, (num_attempted/num_levels)*100, (num_finished/num_levels)*100

    # Returns rows of student object with score, start time, end time of the level
    def multiple_students_one_level(students, level):
        student_data = []

        for student in students:
            student_data.append(one_row(student, level))

        return student_data

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
            return Class.objects.filter(teacher__in=teachers)
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

class StudentRow:

    def __init__(self, *args, **kwargs):
        student = kwargs.get('student')
        self.class_field = student.class_field
        self.name = student.user.user.first_name
        self.id = student.id
        self.total_time = kwargs.get('total_time', timedelta(0))
        self.total_score = kwargs.get('total_score', 0.0)
        self.progress = kwargs.get('progress', (0.0,0.0,0.0))
        self.scores = kwargs.get('scores', [])
        self.start_time = kwargs.get('start_time', "")
        self.finish_time = kwargs.get('finish_time', "")

