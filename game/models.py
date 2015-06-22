from django.contrib.auth.models import User
from django.db import models

from portal.models import UserProfile, Student


class Block (models.Model):
    type = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type


class Theme(models.Model):
    name = models.CharField(max_length=100)
    background = models.CharField(max_length=7, default='#eff8ff')
    border = models.CharField(max_length=7, default='#bce369')
    selected = models.CharField(max_length=7, default='#70961f')

    def __unicode__(self):
        return self.name


class Decor(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    width = models.IntegerField()
    height = models.IntegerField()
    theme = models.ForeignKey(Theme, related_name='decor')
    z_index = models.IntegerField()


class Character(models.Model):
    name = models.CharField(max_length=100)
    en_face = models.CharField(max_length=500)
    top_down = models.CharField(max_length=500)
    width = models.IntegerField(default=40)
    height = models.IntegerField(default=20)


class Episode (models.Model):
    '''Variables prefixed with r_ signify they are parameters for random level generation'''

    name = models.CharField(max_length=200)
    next_episode = models.ForeignKey("self", null=True, default=None)
    in_development = models.BooleanField(default=False)

    r_random_levels_enabled = models.BooleanField(default=False)
    r_branchiness = models.FloatField(default=0, null=True)
    r_loopiness = models.FloatField(default=0, null=True)
    r_curviness = models.FloatField(default=0, null=True)
    r_num_tiles = models.IntegerField(default=5, null=True)
    r_blocks = models.ManyToManyField(Block, related_name='episodes')
    r_blocklyEnabled = models.BooleanField(default=True)
    r_pythonEnabled = models.BooleanField(default=False)
    r_trafficLights = models.BooleanField(default=False)
    
    @property
    def first_level(self):
        return self.levels[0]

    @property
    def levels(self):
        '''Sorts the levels by integer conversion of "name" which should equate to the correct play order'''
        
        return sorted(self.level_set.all(), key=lambda level: int(level.name))
    
    def __unicode__(self):
        return 'Episode: ' + self.name

class LevelManager(models.Manager):
    def sorted_levels(self):
        # Sorts all the levels by integer conversion of "name" which should equate to the correct play order
        # Custom levels do not have an episode

        return sorted(self.model.objects.filter(episode__isnull=False), key=lambda level: int(level.name))

class Level (models.Model):
    name = models.CharField(max_length=100)
    episode = models.ForeignKey(Episode, blank=True, null=True, default=None)
    path = models.TextField(max_length=10000)
    traffic_lights = models.TextField(max_length=10000, default='[]')
    origin = models.CharField(max_length=50, default='[]')
    destinations = models.CharField(max_length=50, default='[[]]')
    default = models.BooleanField(default=False)
    owner = models.ForeignKey(UserProfile, related_name='levels', blank=True, null=True)
    fuel_gauge = models.BooleanField(default=True)
    max_fuel = models.IntegerField(default=50)
    direct_drive = models.BooleanField(default=False)
    next_level = models.ForeignKey('self', null=True, default=None)
    shared_with = models.ManyToManyField(User, related_name="shared", blank=True)
    model_solution = models.CharField(blank=True, max_length=20, default='[]')
    disable_route_score = models.BooleanField(default=False)
    threads = models.IntegerField(blank=False, default=1)
    blocklyEnabled = models.BooleanField(default=True)
    pythonEnabled = models.BooleanField(default=True)
    pythonViewEnabled = models.BooleanField(default=False)
    theme = models.ForeignKey(Theme, blank=True, null=True, default=None)
    character = models.ForeignKey(Character, default=1)
    anonymous = models.BooleanField(default=False)
    objects = LevelManager()

    def __unicode__(self):
        return 'Level ' + str(self.name)
    

class LevelBlock(models.Model):
    type = models.ForeignKey(Block)
    level = models.ForeignKey(Level)
    number = models.PositiveIntegerField(default=None, null=True)


class LevelDecor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    level = models.ForeignKey(Level)
    decorName = models.CharField(max_length=100, default='tree1')
    

class Workspace (models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(UserProfile, related_name='workspaces', blank=True, null=True)
    contents = models.TextField(default="")
    python_contents = models.TextField(default="")


class Attempt (models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    level = models.ForeignKey(Level, related_name='attempts')
    student = models.ForeignKey(Student, related_name='attempts', blank=True, null=True)
    finish_time = models.DateTimeField(auto_now=True)
    score = models.FloatField(default=0, null=True)
    workspace = models.TextField(default="")
    python_workspace = models.TextField(default="")

    def elapsed_time(self):
        return self.finish_time - self.start_time
