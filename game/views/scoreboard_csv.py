# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
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
import csv

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy

Single_Level_Header = [ugettext_lazy('Class'), ugettext_lazy('Name'), ugettext_lazy('Score'),
                       ugettext_lazy('Total Time'), ugettext_lazy('Start Time'), ugettext_lazy('Finish Time')]
Multiple_Levels_Header = [ugettext_lazy('Class'), ugettext_lazy('Name'), ugettext_lazy('Total Score'),
                          ugettext_lazy('Total Time'), ugettext_lazy('Started Levels %'),
                          ugettext_lazy('Attempted levels %'), ugettext_lazy('Finished levels %')]


def scoreboard_csv(student_data, requested_sorted_levels):
    if len(requested_sorted_levels) > 1:
        return scoreboard_csv_multiple_levels(student_data, requested_sorted_levels)
    else:
        return scoreboard_csv_single_level(student_data)


def scoreboard_csv_multiple_levels(student_rows, levels):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'

    header = header_for(levels)
    rows = map(create_to_array_multiple_levels(response), student_rows)

    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(rows)

    return response


def scoreboard_csv_single_level(student_rows):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'

    rows = map(create_to_array_single_level(response), student_rows)

    writer = csv.writer(response)
    writer.writerow(Single_Level_Header)
    writer.writerows(rows)

    return response


def header_for(levels):
    level_names = map(str, levels)
    return Multiple_Levels_Header + level_names


def create_to_array_multiple_levels(response):
    def to_array_multiple_levels(student_row):
        started, attempted, finished = student_row.progress
        result = [student_row.class_field.name.encode(response.charset), student_row.name, student_row.total_score,
                  student_row.total_time, started, attempted, finished]

        return result + student_row.scores
    return to_array_multiple_levels


def create_to_array_single_level(response):
    def to_array_single_level(student_row):
        result = [student_row.class_field.name.encode(response.charset), student_row.name, student_row.total_score,
                  student_row.total_time, student_row.start_time, student_row.finish_time]

        return result
    return to_array_single_level

