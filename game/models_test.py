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
    geography = Class.objects.create(name="Geography", teacher=teacher, school=school)
    geography.save()
    student_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    student_user.save()
    student = Student.objects.create(name="Student", class_field=geography, user=student_user)
    student.save()
    home_economics = Class.objects.create(name="Home Economics", teacher=teacher, school=school)
    home_economics.save()
    other_user = User.objects.create_user('paul', 'mccartney@thebeatles.com', 'paulpassword')
    other_user.save()
    other = Student.objects.create(name="Bob", class_field=home_economics, user=other_user)
    other.save()

  def test_get_logged_in_students(self):
    class_obj = Class.objects.get(name="Geography")
    self.client.login(username='john', password='johnpassword')
    logged_in_students = class_obj.get_logged_in_students()
    self.assertEqual(len(logged_in_students), 1)
    self.assertEqual(logged_in_students[0].name, "Student")
    self.client.login(username='paul', password='paulpassword')
    logged_in_students = class_obj.get_logged_in_students()
    self.assertEqual(len(logged_in_students), 0)
