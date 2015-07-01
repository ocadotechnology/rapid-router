import csv

from django.http import HttpResponse

Single_Level_Header = ['Class', 'Name', 'Score', 'Total Time', 'Start Time', 'Finish Time']
Multiple_Levels_Header = ['Class', 'Name', 'Total Score', 'Total Time', 'Started Levels %', 'Attempted levels %', 'Finished levels %']

def scoreboard_csv(student_data, requested_sorted_levels):
    if (len(requested_sorted_levels) > 1):
        return scoreboard_csv_multiple_levels(student_data, requested_sorted_levels)
    else:
        return scoreboard_csv_single_level(student_data)

def scoreboard_csv_multiple_levels(student_rows, levels):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'

    header = header_for(levels)
    rows = map(to_array_multiple_levels, student_rows)

    writer = csv.writer(response)
    writer.writerow(header)
    writer.writerows(rows)

    return response

def scoreboard_csv_single_level(student_rows):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="scoreboard.csv"'

    rows = map(to_array_single_level, student_rows)

    writer = csv.writer(response)
    writer.writerow(Single_Level_Header)
    writer.writerows(rows)

    return response

def header_for(levels):
    level_names = map(str, levels)
    return Multiple_Levels_Header + level_names

def to_array_multiple_levels(student_row):
    started, attempted, finished = student_row.progress
    result = [student_row.class_field.name, student_row.name, student_row.total_score, student_row.total_time,
              started, attempted, finished]

    return result + student_row.scores

def to_array_single_level(student_row):
    result = [student_row.class_field.name, student_row.name, student_row.total_score, student_row.total_time,
              student_row.start_time, student_row.finish_time]

    return result

