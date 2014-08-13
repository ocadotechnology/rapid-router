from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime

class ClassTestCase(TestCase):
  def test_that_tests_still_work(self):
    self.assertTrue(True)
