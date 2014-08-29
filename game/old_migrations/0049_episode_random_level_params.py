# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def episode_random_level_params(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')

    episode1 = Episode.objects.get(name="Getting Started")
    episode1.r_branchiness = 0.0
    episode1.r_loopiness  = 0.0
    episode1.r_curviness = 0.5
    episode1.r_num_tiles = 10
    episode1.r_blockly_enabled = True
    episode1.r_python_enabled = False
    episode1.save();

    episode2 = Episode.objects.get(name="Shortest Route")
    episode2.r_branchiness = 0.3
    episode2.r_loopiness  = 0.05
    episode2.r_curviness = 0.15
    episode2.r_num_tiles = 20
    episode2.r_blockly_enabled = True
    episode2.r_python_enabled = False
    episode2.save();

    episode3 = Episode.objects.get(name="Loops and Repetitions")
    episode3.r_branchiness = 0.0
    episode3.r_loopiness  = 0.0
    episode3.r_curviness = 0.2
    episode3.r_num_tiles = 15
    episode3.r_blockly_enabled = True
    episode3.r_python_enabled = False
    episode3.save();

    episode4 = Episode.objects.get(name="Traffic Lights")
    episode4.r_branchiness = 0.5
    episode4.r_loopiness  = 0.1
    episode4.r_curviness = 0.2
    episode4.r_num_tiles = 35
    episode4.r_blockly_enabled = True
    episode4.r_python_enabled = False
    episode4.save();

    episode5 = Episode.objects.get(name="Miscellaneous")
    episode5.r_branchiness = 0.3
    episode5.r_loopiness  = 0.1
    episode5.r_curviness = 0.1
    episode5.r_num_tiles = 30
    episode5.r_blockly_enabled = True
    episode5.r_python_enabled = False
    episode5.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0048_fix_level_blocks'),
    ]

    operations = [
        migrations.RunPython(episode_random_level_params),
    ]
