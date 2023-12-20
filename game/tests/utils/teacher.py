import random
import string

from common.models import School, Teacher


def create_school() -> School:
    school = School()
    school.name = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
    school.country = "United Kingdom"
    school.save()

    return school


def add_teacher_to_school(teacher: Teacher, school: School, is_admin=False):
    teacher.user.teacher.school = school
    teacher.is_admin = is_admin
    teacher.user.teacher.save()
