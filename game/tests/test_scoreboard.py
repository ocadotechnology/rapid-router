import datetime

from django.test import TestCase
from hamcrest import *

from game.models import Level
from game.views.scoreboard import StudentRow, scoreboard_csv, get_levels_headers
from portal.models import Class
from portal.tests.utils.classes import create_class_directly
from portal.tests.utils.student import create_school_student_directly
from portal.tests.utils.teacher import signup_teacher_directly



class ScoreboardTestCase(TestCase):
    def student_row(self):
        # Create one student
        email, password = signup_teacher_directly()
        class_name, access_code = create_class_directly(email)
        _, _, student = create_school_student_directly(access_code)

        start_time = datetime.datetime.now()
        finish_time = datetime.datetime.now()
        total_time = finish_time - start_time
        scores = [x for x in range(20)]
        total_score = sum(scores)
        progress = (0, 0, 0)

        row = StudentRow(student=student,
                         total_time=total_time,
                         total_score=total_score,
                         progress=progress,
                         scores=scores,
                         start_time=start_time,
                         finish_time=finish_time,
                         class_field=Class(name="MyClass"))
        return row

    def test_multiple_levels(self):
        headers = get_levels_headers(['Class', 'Name', 'Total Score', 'Total Time', 'Progress'],
                                     Level.objects.sorted_levels())
        student_row = self.student_row()
        response = scoreboard_csv([student_row], headers)

        actual_header, actual_rows = self.actual_data(response.content)

        print response.content

        assert_that(actual_header, equal_to("Class,Name,Total Score,Total Time,Progress,Level 1,Level 2,Level 3,Level 4,Level 5,Level 6,Level 7,Level 8,Level 9,Level 10,Level 11,Level 12,Level 13,Level 14,Level 15,Level 16,Level 17,Level 18,Level 19,Level 20,Level 21,Level 22,Level 23,Level 24,Level 25,Level 26,Level 27,Level 28,Level 29,Level 30,Level 31,Level 32,Level 33,Level 34,Level 35,Level 36,Level 37,Level 38,Level 39,Level 40,Level 41,Level 42,Level 43,Level 44,Level 45,Level 46,Level 47,Level 48,Level 49,Level 50,Level 51,Level 52,Level 53,Level 54,Level 55,Level 56,Level 57,Level 58,Level 59,Level 60,Level 61,Level 62,Level 63,Level 64,Level 65,Level 66,Level 67,Level 68,Level 69,Level 70,Level 71,Level 72,Level 73,Level 74,Level 75,Level 76,Level 77,Level 78,Level 79,Level 80,Level 81,Level 82,Level 83,Level 84,Level 85,Level 86,Level 87,Level 88,Level 89,Level 90,Level 91,Level 92,Level 93,Level 94,Level 95,Level 96,Level 97,Level 98,Level 99,Level 100,Level 101,Level 102,Level 103,Level 104,Level 105,Level 106,Level 107,Level 108,Level 109"))

        assert_that(actual_rows, equal_to(["Class 1,Student 1,190,%s,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19" % (student_row.total_time), ""]))

    def actual_data(self, content):
        split = content.split("\r\n")
        header = split[0]
        rows = split[1:]
        return header, rows

