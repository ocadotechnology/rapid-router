# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations



def change_episode_names(apps, schema_editor):
    Episode = apps.get_model('game', 'Episode')

    procEpisode = Episode.objects.get(name="Functions")
    procEpisode.name = "Procedures"

    puzzlesEpisode = Episode.objects.get(name="Hard puzzles!")
    puzzlesEpisode.name = "Puzzles!"

    procEpisode.save()
    puzzlesEpisode.save()



class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_first_puzzle_levels'),
    ]

    operations = [
        migrations.RunPython(change_episode_names),
    ]
