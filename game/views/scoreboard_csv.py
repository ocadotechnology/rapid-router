from builtins import map
import csv

from django.http import HttpResponse
from django.utils.translation import ugettext_lazy

Single_Level_Header = [
    ugettext_lazy("Class"),
    ugettext_lazy("Name"),
    ugettext_lazy("Score"),
    ugettext_lazy("Total Time"),
    ugettext_lazy("Start Time"),
    ugettext_lazy("Finish Time"),
]
Multiple_Levels_Header = [
    ugettext_lazy("Class"),
    ugettext_lazy("Name"),
    ugettext_lazy("Total Score"),
    ugettext_lazy("Total Time"),
    ugettext_lazy("Started Levels %"),
    ugettext_lazy("Attempted levels %"),
    ugettext_lazy("Finished levels %"),
]


def scoreboard_csv(student_data, requested_sorted_levels):
    if len(requested_sorted_levels) > 1:
        return scoreboard_csv_multiple_levels(student_data, requested_sorted_levels)
    else:
        return scoreboard_csv_single_level(student_data)


def scoreboard_csv_multiple_levels(student_rows, levels):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="scoreboard.csv"'

    header = header_for(levels)
    rows = list(map(create_to_array_multiple_levels(response), student_rows))

    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(rows)

    return response


def scoreboard_csv_single_level(student_rows):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="scoreboard.csv"'

    rows = list(map(create_to_array_single_level(response), student_rows))

    writer = csv.writer(response)
    writer.writerow(Single_Level_Header)
    writer.writerows(rows)

    return response


def header_for(levels):
    level_names = list(map(str, levels))
    return Multiple_Levels_Header + level_names


def create_to_array_multiple_levels(response):
    def to_array_multiple_levels(student_row):
        started, attempted, finished = student_row.progress
        result = [
            student_row.class_field.name.encode(response.charset),
            student_row.name.encode(response.charset),
            student_row.total_score,
            student_row.total_time,
            started,
            attempted,
            finished,
        ]

        return result + student_row.scores

    return to_array_multiple_levels


def create_to_array_single_level(response):
    def to_array_single_level(student_row):
        result = [
            student_row.class_field.name.encode(response.charset),
            student_row.name.encode(response.charset),
            student_row.total_score,
            student_row.total_time,
            student_row.start_time,
            student_row.finish_time,
        ]

        return result

    return to_array_single_level
