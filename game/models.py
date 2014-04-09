from django.db import models
from django.contrib.auth.models import User

class School (models.Model):
	name = models.CharField(max_length = 200)

class Teacher (models.Model):
	name = models.CharField(max_length = 200)
	user = models.OneToOneField(User)

class Class (models.Model):
	school = models.ForeignKey(School, related_name='class')
	teacher = models.ForeignKey(Teacher, related_name='class')

class Student (models.Model):
	name = models.CharField(max_length = 200)
	class_field = models.ForeignKey(Class, related_name='name')
	user = models.OneToOneField(User)

class Guardian (models.Model):
	name = models.CharField(max_length = 200)
	children = models.ManyToManyField(Student)
	user = models.OneToOneField(User)

class Attempt (models.Model):
	time = models.IntegerField()
	student = models.ForeignKey(Student, related_name='attempts')

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

class Level (models.Model):
	name = models.IntegerField()
	attempts = models.ManyToManyField(Attempt)
