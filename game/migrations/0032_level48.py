# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def decor_and_length(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    level = Level.objects.get(id=48)
    level.traffic_lights = '[{"node":3,"sourceNode":2,"redDuration":4,"greenDuration":2,"startTime":0,"startingState":"RED"}, {"node":3,"sourceNode":4,"redDuration":2,"greenDuration":4,"startTime":0,"startingState":"GREEN"}, {"node":3,"sourceNode":5,"redDuration":2,"greenDuration":4,"startTime":0,"startingState":"GREEN"}, {"node":3,"sourceNode":6,"redDuration":4,"greenDuration":2,"startTime":0,"startingState":"RED"}]'
    level.save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0031_levels_move_decor'),
    ]

    operations = [
        migrations.RunPython(decor_and_length),
    ]
