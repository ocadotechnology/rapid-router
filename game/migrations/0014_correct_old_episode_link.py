# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



def correct_old_episode_link(apps, schema_editor):
    Episode = apps.get_model('game', 'Episode')

    episode6 = Episode.objects.get(id=6, name="Traffic Lights")
    episode6.next_episode = None

    episode6.save()



class Migration(migrations.Migration):

    dependencies = [
        ('game', '0013_delete_orig_limit_level'),
    ]

    operations = [
        migrations.RunPython(correct_old_episode_link),
    ]
