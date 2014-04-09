from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime

class School (models.Model):
  name = models.CharField(max_length = 200)

class Teacher (models.Model):
  name = models.CharField(max_length = 200)
  user = models.OneToOneField(User)

class Class (models.Model):
  name = models.CharField(max_length = 200)
  school = models.ForeignKey(School, related_name='class')
  teacher = models.ForeignKey(Teacher, related_name='class')

  def get_logged_in_students(self):
    """This gets all the students who are logged in."""
    sessions = Session.objects.filter(expire_date__gte=datetime.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return Student.objects.filter(class_field=self).filter(user__id__in=uid_list)

class Student (models.Model):
  name = models.CharField(max_length = 200)
  class_field = models.ForeignKey(Class, related_name='students')
  user = models.OneToOneField(User)

class Guardian (models.Model):
  name = models.CharField(max_length = 200)
  children = models.ManyToManyField(Student)
  user = models.OneToOneField(User)

class Level (models.Model):
  name = models.IntegerField()

class Attempt (models.Model):
  start_time = models.IntegerField()
  level = models.ForeignKey(Level, related_name='attempts')
  student = models.ForeignKey(Student, related_name='attempts')
  finish_time = models.IntegerField()

class Command (models.Model):
  STEP_CHOICES = (
    ('R', 'right'),
    ('L', 'left'),
    ('F', 'forward'),
    ('B', 'backwards'),
  )
  step = models.IntegerField()
  attempt = models.ForeignKey(Attempt, related_name='commands')
  command = models.CharField(max_length = 10, choices=STEP_CHOICES, default='F')
