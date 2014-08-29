# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def recreate_episodes(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')

    episode1 = Episode.objects.get(pk=1)
    episode2 = Episode.objects.get(pk=2)
    episode3 = Episode.objects.get(pk=3)
    episode4 = Episode.objects.get(pk=4)
    episode5 = Episode.objects.get(pk=5)
    episode6 = Episode.objects.get(pk=6)
   
    episode1.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    episode2.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "deliver"])

    episode3.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat"])

    episode4.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_repeat"])
    
    episode5.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "at_destination",
                                                       "controls_if", "road_exists", "dead_end",
                                                       "controls_repeat", "turn_around"])

    episode6.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                       "controls_repeat_until", "controls_if",
                                                       "road_exists", "at_destination", "wait",
                                                       "controls_repeat", "dead_end", "turn_around",
                                                       "controls_repeat_while", "traffic_light"])

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0106_amend_decor'),
    ]

    operations = [
        migrations.RunPython(recreate_episodes)
    ]
