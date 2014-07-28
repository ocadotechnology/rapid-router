from datetime import datetime

from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import models


class UserProfile (models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='static/game/image/avatars/', null=True, blank=True,
                               default='static/game/image/avatars/default-avatar.jpeg')

    def __unicode__(self):
        return self.user.username


class School (models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Teacher (models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return '%s %s' % (self.user.user.first_name, self.user.user.last_name)


class Class (models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, related_name='class_school')
    teacher = models.ForeignKey(Teacher, related_name='class_teacher')

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return '%s %s' % (self.user.user.first_name, self.user.user.last_name)


class Guardian (models.Model):
    name = models.CharField(max_length=200)
    children = models.ManyToManyField(Student)
    user = models.OneToOneField(UserProfile)

    def __unicode__(self):
        return '%s %s' % (self.user.user.first_name, self.user.user.last_name)


class Block (models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type


class Theme(models.Model):
    name = models.CharField(max_length=100)


class Decor(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    width = models.IntegerField()
    height = models.IntegerField()
    theme = models.ForeignKey(Theme, related_name='decor')


class Level (models.Model):
    name = models.CharField(max_length=100)
    path = models.TextField(max_length=10000)
    decor = models.TextField(max_length=10000, default='[]')
    traffic_lights = models.TextField(max_length=10000, default='[]')
    destinations = models.CharField(max_length=50)
    default = models.BooleanField(default=False)
    owner = models.ForeignKey(UserProfile, related_name='levels', blank=True, null=True)
    blocks = models.ManyToManyField(Block, related_name='levels')
    max_fuel = models.IntegerField(default=50)
    direct_drive = models.BooleanField(default=False)
    next_level = models.ForeignKey('self', null=True, default=None)
    shared_with = models.ManyToManyField(User, related_name="shared", blank=True, null=True)
    model_solution = models.IntegerField(blank=True, default=50)
    threads = models.IntegerField(blank=False, default=1)
    blocklyEnabled = models.BooleanField(default=True)
    pythonEnabled = models.BooleanField(default=True)
    theme = models.ForeignKey(Theme, default=1)

    def __unicode__(self):
        return 'Level ' + str(self.id)

    @property
    def episode(self):
        for episode in Episode.objects.all():
            if self in episode.levels:
                return episode
        return None


class LevelDecor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    level = models.ForeignKey(Level)
    decorName = models.CharField(max_length=100, default='tree1')


class Episode (models.Model):
    name = models.CharField(max_length=200)
    first_level = models.ForeignKey(Level)
    next_episode = models.ForeignKey("self", null=True, default=None)

    r_branchiness = models.FloatField(default=0)
    r_loopiness = models.FloatField(default=0)
    r_curviness = models.FloatField(default=0)
    r_num_tiles = models.IntegerField(default=5)
    r_blocks = models.ManyToManyField(Block, related_name='episodes')
    r_blocklyEnabled = models.BooleanField(default=True)
    r_pythonEnabled = models.BooleanField(default=False)

    @property
    def levels(self):
        if self.first_level is not None:
            level = self.first_level
            while level is not None:
                yield level
                level = level.next_level


class Workspace (models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(Student, related_name='workspaces')
    workspace = models.TextField(default="")


class Attempt (models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, related_name='attempts')
    student = models.ForeignKey(Student, related_name='attempts')
    finish_time = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=0)
    workspace = models.TextField(default="")


class Command (models.Model):
    STEP_CHOICES = (
        ('Right', 'right'),
        ('Left', 'left'),
        ('Forward', 'forward'),
        ('TurnAround', 'turn around'),
        ('Wait', 'wait'),
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
