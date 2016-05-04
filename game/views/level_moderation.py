# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from __future__ import division
import game.messages as messages
import game.permissions as permissions
import json

from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext
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

    student_id = None
    student_dict = None
    level_data = None
    table_headers = None

    if request.method == 'POST':
        if form.is_valid():
            student_id = form.data.get('students')
            class_id = form.data.get('classes')

            if not class_id:
                raise Http404

            # check user has permission to look at this class!
            cl = get_object_or_404(Class, id=class_id)
            if not permissions.can_see_class(request.user, cl):
                return renderError(request,
                                   messages.noPermissionLevelModerationTitle(),
                                   messages.noPermissionLevelModerationClass())

            students = Student.objects.filter(class_field=cl)
            student_dict = {student.id: student.user.user.first_name for student in students}

            if student_id:
                # check student is in class
                student = get_object_or_404(Student, id=student_id)
                if student.class_field != cl:
                    return renderError(request,
                                       messages.noPermissionLevelModerationTitle(),
                                       messages.noPermissionLevelModerationStudent())

                owners = [student.user]

            else:
                owners = [student.user for student in students]

            table_headers = [ugettext('Student'), ugettext('Level name'), ugettext('Shared with'), ugettext('Play'),
                             ugettext('Delete')]
            level_data = []

            for owner in owners:
                for level in Level.objects.filter(owner=owner):
                    users_shared_with = [user for user in level.shared_with.all()
                                         if permissions.can_share_level_with(user, owner.user)
                                         and user != owner.user]

                    if not users_shared_with:
                        shared_str = "-"
                    else:
                        shared_str = ", ".join(app_tags.make_into_username(user) for user in users_shared_with)

                    level_data.append({'student': app_tags.make_into_username(owner.user),
                                       'id': level.id,
                                       'name': level.name,
                                       'shared_with': shared_str})

    context = RequestContext(request, {
        'student_id': student_id,
        'students': student_dict,
        'form': form,
        'levelData': level_data,
        'thead': table_headers,
    })
    return render(request, 'game/level_moderation.html', context_instance=context)


def get_students_for_level_moderation(request, class_id):
    userprofile = request.user.userprofile
    class_ = Class.objects.get(id=class_id)

    if userprofile.teacher != class_.teacher:
        raise Http404

    students = Student.objects.filter(class_field=class_)
    student_dict = {student.id: student.user.user.first_name for student in students}

    return HttpResponse(json.dumps(student_dict), content_type="application/javascript")
