import csv
from builtins import map

from django.http import HttpResponse

Headers = [
    "Class",
    "Name",
    "Total Score",
    "Total Time",
    "Started Levels",
    "Attempted levels",
    "Finished levels",
]


def scoreboard_csv(student_data, requested_sorted_levels):
    print(student_data)
    print(requested_sorted_levels)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="scoreboard.csv"'

    header = header_for(requested_sorted_levels)
    rows = list(map(create_to_array_multiple_levels(response), student_data))

    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(rows)

    return response


def header_for(levels):
    level_names = list(map(str, levels))
    return Headers + level_names


def create_to_array_multiple_levels(response):
    def to_array_multiple_levels(student_row):
        started, attempted, finished = student_row.progress
        result = [
            student_row.class_field.name,
            student_row.name,
            student_row.total_score,
            student_row.total_time,
            started,
            attempted,
            finished,
        ]

        return result + student_row.scores

    return to_array_multiple_levels
