# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_blocks_to_episode(apps, schema_editor):

    Block = apps.get_model('game', 'Block')
    Episode = apps.get_model('game', 'Episode')

    episodes(Episode, Block)


def episodes(Episode, Block):

    episode1 = Episode.objects.get(name="Getting Started")
    episode2 = Episode.objects.get(name="Shortest Route")
    episode3 = Episode.objects.get(name="Loops and Repetitions")
    episode4 = Episode.objects.get(name="If... Only")
    episode5 = Episode.objects.get(name="Traffic Lights")
    episode6 = Episode.objects.get(name="Miscellaneous")

    episode1.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])
    episode2.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])
    episode3.r_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "controls_whileUntil", "at_destination",
                                                     "controls_repeat"])
    episode4.r_blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                     "controls_whileUntil", "controls_if",
                                                     "logic_negate", "road_exists",
                                                     "at_destination", "turn_around",
                                                     "controls_repeat", "road_exists", "dead_end"])
    episode5.r_blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                     "wait", "controls_repeat", "controls_if",
                                                     "logic_negate", "road_exists", "traffic_light",
                                                     "controls_whileUntil", "at_destination"])
    episode6.r_blocks = Block.objects.all()

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0031_levels_move_decor'),
    ]

    operations = [
        migrations.RunPython(add_blocks_to_episode),
    ]
