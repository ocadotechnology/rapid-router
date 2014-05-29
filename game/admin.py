from django.contrib import admin
from game.models import Class, Student, Guardian, Teacher, School, UserProfile, Level, Block

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(UserProfile)

admin.site.register(Level)
admin.site.register(Block)
