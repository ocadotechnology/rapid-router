# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def levels(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Episode = apps.get_model('game', 'Episode')
    
    # Episode 8

    level28 = Level.objects.get(id="28")
    level28.name = "28"
    level28.save()
    
    episode8 = Episode(name="Procedures", first_level=level28)
    episode8.save()

    episode7 = Episode.objects.get(name="The rest ...")
    episode7.next_episode = episode8
    episode7.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_merge'),
    ]

    operations = [
        migrations.RunPython(levels),
    ]
