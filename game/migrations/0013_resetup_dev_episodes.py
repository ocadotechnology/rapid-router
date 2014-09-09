# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def resetup_dev_episodes(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')

    level51 = Level.objects.get(name="51")
    level52 = Level.objects.get(name="52")

    episode7 = Episode(pk=7, name="Functions", first_level=level51, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode7.save()

    episode8 = Episode(pk=8, name="Limited blocks", first_level=level52, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1, in_development=True)
    episode8.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_remove_level_blocks'),
    ]

    operations = [
        migrations.RunPython(resetup_dev_episodes),
    ]
