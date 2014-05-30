from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models

import random

class UserProfile (models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='static/game/image/avatars/', null=True, blank=True,
                               default='/static/game/image/avatars/default-avatar.jpeg')

class School (models.Model):
    name = models.CharField(max_length=200)

class Teacher (models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(UserProfile)

class Class (models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, related_name='class_school')
    teacher = models.ForeignKey(Teacher, related_name='class_teacher')

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

    class Meta:
        verbose_name_plural = "classes"

class Student (models.Model):
    name = models.CharField(max_length=200)
    class_field = models.ForeignKey(Class, related_name='students')
    user = models.OneToOneField(UserProfile)

class Guardian (models.Model):
    name = models.CharField(max_length=200)
    children = models.ManyToManyField(Student)
    user = models.OneToOneField(UserProfile)

class Block (models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type


class Level (models.Model):
    name = models.IntegerField()
    path = models.CharField(max_length=10000)
    default = models.BooleanField(default=False)
    owner = models.ForeignKey(UserProfile, related_name='levels', blank=True, null=True)
    blockLimit = models.IntegerField(blank=True, null=True)
    blocks = models.ManyToManyField(Block, related_name='+')

    @classmethod
    def random_road(cls):
        generated_path = Level.generate_random_path()
        level = cls(name=3000, path=generated_path)
        level.save()
        level.blocks = Block.objects.all()
        level.save()
        return level

    @staticmethod
    def generate_random_path():
        road_tiles = set()
        road_tiles.add((1,3))

        for _ in xrange(20):
            new_tile = Level.pick_adjacent_tile(road_tiles)
            if new_tile is not None:
                road_tiles.add(new_tile)

        print(road_tiles)
        return "[[0,3],[1,3],[1,4],[1,5],[1,6],[2,6],[2,5],[3,5],[3,4],[3,3],[3,2],[4,2],[4,3],[5,3]]"

    @staticmethod
    def pick_adjacent_tile(tiles):
        for attempts in xrange(5):
            origin = random.sample(tiles, 1)[0]
            possibles = set()
            if (origin[0] - 1, origin[1]) not in tiles:
                possibles.add((origin[0] - 1, origin[1]))
            if (origin[0] + 1, origin[1]) not in tiles:
                possibles.add((origin[0] + 1, origin[1]))
            if (origin[0], origin[1] - 1) not in tiles:
                possibles.add((origin[0], origin[1] - 1))
            if (origin[0], origin[1] + 1) not in tiles:
                possibles.add((origin[0], origin[1] + 1))

            if possibles:
                return random.sample(possibles, 1)[0]

        return None

    def __unicode__(self):
        return 'Level ' + str(self.id)


class Attempt (models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, related_name='attempts')
    student = models.ForeignKey(Student, related_name='attempts')
    finish_time = models.DateTimeField(auto_now=True)
    score = models.FloatField()

class Command (models.Model):
    STEP_CHOICES = (
        ('Right', 'right'),
        ('Left', 'left'),
        ('Forward', 'forward'),
        ('TurnAround', 'turn around'),
        ('While', 'while'),
        ('If', 'if'),
    )

    step = models.IntegerField()
    attempt = models.ForeignKey(Attempt, related_name='commands')
    command = models.CharField(max_length=15, choices=STEP_CHOICES, default='Forward')
    next = models.IntegerField(blank=True, null=True)

    # Condition in While or If statements. Optional.
    condition = models.CharField(max_length=400, blank=True)
    # 'While' or 'If' block. Optional.
    executedBlock1 = models.CommaSeparatedIntegerField(blank=True, max_length=100)
    # 'Else' block. Optional.
    executedBlock2 = models.CommaSeparatedIntegerField(blank=True, max_length=100)
