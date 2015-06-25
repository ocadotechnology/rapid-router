from datetime import timedelta

from django.test import TestCase
from hamcrest import *

from game.models import Level
from game.views.scoreboard import StudentRow, scoreboard_csv, get_levels_headers
from portal.models import Class
from portal.tests.utils.classes import create_class_directly
from portal.tests.utils.student import create_school_student_directly
from portal.tests.utils.teacher import signup_teacher_directly

HEADERS = ['Class', 'Name', 'Total Score', 'Total Time', 'Started Levels %', 'Attempted levels %', 'Finished levels %']

class ScoreboardTestCase(TestCase):

    def test_multiple_levels(self):
        levels = Level.objects.sorted_levels()
        headers = get_levels_headers(HEADERS, levels)
        student_row = self.student_row()
        student_row2 = self.student_row()

        response = scoreboard_csv([student_row, student_row2], headers)

        actual_header, actual_rows = self.actual_data(response.content)

        expected_header = self.expected_header(levels)
        expected_rows = self.expected_rows(student_row, student_row2)

        assert_that(actual_header, equal_to(expected_header))

        assert_that(actual_rows, equal_to(expected_rows))

    def expected_rows(self, *student_rows):
        return map(self.expected_row, student_rows) + [""]

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
                         progress=progress,
                         scores=all_scores,
                         class_field=Class(name="MyClass"))
        return row

    def expected_row(self, student_row):
        beginning = "%s,%s,190,0:00:30,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19," \
                    % (student_row.class_field.name, student_row.name)
        padding = ','.join([""] * 89)
        return beginning + padding

    def expected_header(self, levels):
        level_strings = map(str, levels)
        all_header_strings = HEADERS + level_strings
        joined = ','.join(all_header_strings)
        return joined

    def actual_data(self, content):
        split = content.split("\r\n")
        header = split[0]
        rows = split[1:]
        return header, rows

