from __future__ import division
import game.messages as messages
import game.permissions as permissions
import json

from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from helper import renderError
from game.forms import LevelModerationForm
from game.models import Level
from portal.models import Student, Class
from portal.templatetags import app_tags


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
        return renderError(request, messages.noPermissionLevelModerationTitle(),
                           messages.noPermissionLevelModerationPage())

    teacher = request.user.userprofile.teacher
    classes_taught = Class.objects.filter(teacher=teacher)

    if len(classes_taught) <= 0:
        return renderError(request, messages.noPermissionLevelModerationTitle(),
                           messages.noDataToShowLevelModeration())

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
                            shared_str += app_tags.make_into_username(user) + ", "
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
