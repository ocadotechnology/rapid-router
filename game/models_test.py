from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from models import School, Teacher, Student, Class
from datetime import datetime

class ClassTestCase(TestCase):
	def setUp(self):
		school = School.objects.create(name="My School")
		school.save()
		teacher_user = User.objects.create_user('ringo', 'starr@thebeatles.com', 'ringopassword')
		teacher_user.save()
		teacher = Teacher.objects.create(name="My Teacher", user=teacher_user)
		teacher.save()
		class_obj = Class.objects.create(name="Geography", teacher=teacher, school=school)
		class_obj.save()
		student_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
		student_user.save()
		student = Student.objects.create(name="Student", class_field=class_obj, user=student_user)
		self.client.login(username='john', password='johnpassword')

	def test_get_logged_in_students(self):
		class_obj = Class.objects.get(name="Geography")
		logged_in_students = class_obj.get_logged_in_students()
		self.assertEqual(len(logged_in_students), 1)
		self.assertEqual(logged_in_students[0].name, "Student")
