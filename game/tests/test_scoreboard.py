from datetime import timedelta, datetime

from django.test import TestCase

from hamcrest import *

from game.models import Level
from game.views.scoreboard import StudentRow, scoreboard_csv_multiple_levels, scoreboard_csv_single_level
from portal.models import Class
from portal.tests.utils.classes import create_class_directly
from portal.tests.utils.student import create_school_student_directly
from portal.tests.utils.teacher import signup_teacher_directly

Headers = ['Class', 'Name', 'Total Score', 'Total Time', 'Started Levels %', 'Attempted levels %', 'Finished levels %']

class ScoreboardTestCase(TestCase):

    def test_multiple_levels(self):
        levels = Level.objects.sorted_levels()
        student_rows = [(self.student_row()), (self.student_row())]

        response = scoreboard_csv_multiple_levels(student_rows, levels)

        actual_header, actual_rows = self.actual_data(response.content)

        expected_header = self.expected_header(levels)
        expected_rows = self.expected_rows_multiple_levels(student_rows)

        assert_that(actual_header, equal_to(expected_header))

        assert_that(actual_rows, equal_to(expected_rows))

    def test_single_level(self):
        student_rows = [(self.student_row()), (self.student_row())]
        response = scoreboard_csv_single_level(student_rows)

        actual_header, actual_rows = self.actual_data(response.content)

        expected_header = 'Class,Name,Score,Total Time,Start Time,Finish Time'
        expected_rows = self.expected_rows_single_level(student_rows)

        assert_that(actual_header, equal_to(expected_header))

        assert_that(actual_rows, equal_to(expected_rows))

    def expected_rows_single_level(self, student_rows):
        return map(self.expected_row_single_level, student_rows) + [""]

    def expected_rows_multiple_levels(self, student_rows):
        return map(self.expected_row_multiple_levels, student_rows) + [""]

    def student_row(self):
        # Create one student
        email, password = signup_teacher_directly()
        class_name, access_code = create_class_directly(email)
        _, _, student = create_school_student_directly(access_code)

        total_time = timedelta(0, 30)
        scores = [x for x in range(20)]
        total_score = sum(scores)
        progress = (0, 0, 0)

        all_scores = scores + [""] * 89

        row = StudentRow(student=student,
                         total_time=total_time,
                         total_score=total_score,
                         start_time=datetime.fromtimestamp(1435305072),
                         finish_time=datetime.fromtimestamp(1438305072),
                         progress=progress,
                         scores=all_scores,
                         class_field=Class(name="MyClass"))
        return row

    def expected_row_multiple_levels(self, student_row):
        beginning = "%s,%s,190,0:00:30,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19," \
                    % (student_row.class_field.name, student_row.name)
        padding = ','.join([""] * 89)
        return beginning + padding

    def expected_row_single_level(self, student_row):
        return "%s,%s,190,0:00:30,2015-06-26 08:51:12,2015-07-31 02:11:12" % (student_row.class_field.name, student_row.name)

    def expected_header(self, levels):
        level_strings = map(str, levels)
        all_header_strings = Headers + level_strings
        joined = ','.join(all_header_strings)
        return joined

    def actual_data(self, content):
        split = content.split("\r\n")
        header = split[0]
        rows = split[1:]
        return header, rows

