import csv

from django.http import HttpResponse

Headers = [
    "Class",
    "Name",
    "Completed Levels",
    "Total Time",
    "Total Score",
]


def scoreboard_csv(student_data, requested_sorted_levels, improvement_data):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="scoreboard.csv"'

    improvement_dict = {}
    for student in improvement_data:
        idx = f"{student.class_field.name}_{student.name}"
        improvement_dict[idx] = student.areas

    headers = Headers + requested_sorted_levels + ["Areas for improvement"]

    rows = []
    for student in student_data:
        result = [
            student.class_field.name,
            student.name,
            student.completed,
            student.total_time,
            student.total_score,
        ]

        scores = []
        for level_id, level_score in student.level_scores.items():
            scores.append(level_score["score"])

        row = result + scores

        # add the areas to improve, if there's any
        idx = f"{student.class_field.name}_{student.name}"
        row.append(improvement_dict.get(idx))

        rows.append(row)

    writer = csv.writer(response)
    writer.writerow(headers)
    writer.writerows(rows)

    return response
