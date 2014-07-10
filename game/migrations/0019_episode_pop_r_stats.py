# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def episodes(apps, schema_editor):
    Episode = apps.get_model('game', 'Episode')

    episode1 = Episode.objects.get(id=1)
    episode1.r_branchiness = 0.0
    episode1.loopiness = 0.0
    episode1.r_num_tiles = 5
    episode1.save();

    episode2 = Episode.objects.get(id=2)
    episode2.r_branchiness = 0.0
    episode2.loopiness = 0.0
    episode2.r_num_tiles = 5
    episode2.save();

    episode3 = Episode.objects.get(id=3)
    episode3.r_branchiness = 0.0
    episode3.loopiness = 0.0
    episode3.r_num_tiles = 5
    episode3.save();

    episode4 = Episode.objects.get(id=4)
    episode4.r_branchiness = 0.0
    episode4.loopiness = 0.0
    episode4.r_num_tiles = 5
    episode4.save();

    episode5 = Episode.objects.get(id=5)
    episode5.r_branchiness = 0.0
    episode5.loopiness = 0.0
    episode5.r_num_tiles = 5
    episode5.save();

    episode6 = Episode.objects.get(id=6)
    episode6.r_branchiness = 0.2
    episode6.loopiness = 0.5
    episode6.r_num_tiles = 12
    episode6.save();

    episode7 = Episode.objects.get(id=7)
    episode7.r_branchiness = 0.2
    episode7.loopiness = 0.5
    episode7.r_num_tiles = 20
    episode7.save();

    episode8 = Episode.objects.get(id=8)
    episode8.r_branchiness = 0.0
    episode8.loopiness = 0.0
    episode8.r_num_tiles = 10
    episode8.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_auto_20140710_1636')
    ]

    operations = [
        migrations.RunPython(episodes),
    ]