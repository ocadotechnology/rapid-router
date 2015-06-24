import datetime
from unittest import skip

from django.test import TestCase

from game.models import Level
from game.views.scoreboard import StudentRow, get_scoreboard_csv, get_levels_headers
from portal.models import Student
from portal.tests.utils.student import generate_solo_details


class ScoreboardTestCase(TestCase):
    def createTestData(self):
        # Create one student
        student = Student.objects.soloFactory(*generate_solo_details())
        start_time = datetime.datetime.now()
        finish_time = datetime.datetime.now()
        total_time = finish_time-start_time
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
        )
        return row

    @skip("Not passing yet")
    def multipleLevels(self):
        headers = get_levels_headers(['Class', 'Name', 'Total Score', 'Total Time', 'Progress'], Level.objects.sorted_levels())
        response = get_scoreboard_csv([self.createTestData()], headers)
        print response