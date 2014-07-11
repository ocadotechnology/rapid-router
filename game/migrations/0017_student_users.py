from django.db import models, migrations
from django.contrib.auth.hashers import make_password

def insert_user(apps, name, password):
    User = apps.get_model('auth', 'User')
    user = User.objects.create(username=name, email=name+'@ocado.com', is_superuser=False, is_staff=False, password=make_password(password))
    user.save()
    return user

def insert_user_profile(apps, user):
    UserProfile = apps.get_model('game', 'UserProfile')
    userProfile = UserProfile.objects.create(user=user)
    userProfile.save()
    return userProfile

def insert_school(apps, name):
    School = apps.get_model('game', 'School')
    school = School.objects.create(name=name)
    school.save()
    return school

def insert_teacher(apps, name, user):
    Teacher = apps.get_model('game', 'Teacher')
    teacher = Teacher.objects.create(name=name, user=user)
    teacher.save()
    return teacher

def insert_class(apps, name, teacher, school):
    Class = apps.get_model('game', 'Class')
    klass = Class.objects.create(name=name, teacher=teacher, school=school)
    klass.save()
    return klass

def insert_student(apps, name, klass, user):
    Student = apps.get_model('game', 'Student')
    student = Student.objects.create(name=name, class_field=klass, user=user)
    student.save()
    return student

def insert_students(apps, schema_editor):
    teacher_user = insert_user(apps, 'teacher', 'abc123')
    teacher_user_profile = insert_user_profile(apps, teacher_user)
    teacher = insert_teacher(apps, 'teacher', teacher_user_profile)

    school = insert_school(apps, 'school')
    klass = insert_class(apps, 'class', teacher, school)

    student1_user = insert_user(apps, 'student1', 'abc123')
    student1_user_profile = insert_user_profile(apps, student1_user)
    student1 = insert_student(apps, 'student1', klass, student1_user_profile) 

    student2_user = insert_user(apps, 'student2', 'abc123')
    student2_user_profile = insert_user_profile(apps, student2_user)
    student2 = insert_student(apps, 'student2', klass, student2_user_profile)

class Migration(migrations.Migration):
    dependencies = [
            ('game', '0016_merge')
    ]

    operations = [
            migrations.RunPython(insert_students),
    ]
    