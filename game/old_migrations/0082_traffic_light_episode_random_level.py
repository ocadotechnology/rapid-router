# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def episode_random_level_tls(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')

    episode4 = Episode.objects.get(name="Traffic Lights")
    episode4.r_trafficLights = True
    episode4.save()

    episode5 = Episode.objects.get(name="Miscellaneous")
    episode5.r_trafficLights = True
    episode5.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0081_episode_r_trafficlights'),
    ]

    operations = [
        migrations.RunPython(episode_random_level_tls),
    ]
