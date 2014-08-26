# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def run_operations(apps, schema_editor):

    Episode = apps.get_model('game', 'Episode')
    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    Episode.objects.all().delete()

    recreate_episodes(Episode, Level, Block)


def recreate_episodes(Episode, Level, Block):

    level1 = Level.objects.get(pk=1)

    episode1 = Episode(pk=1, name="Getting Started", first_level=level1, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=10, r_curviness=0.5, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode1.save()

    level13 = Level.objects.get(pk=13)

    episode2 = Episode(pk=2, name="Shortest Route", first_level=level13, r_branchiness=0.3,
                       r_loopiness=0.05, r_num_tiles=20, r_curviness=0.15, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode2.save()

    level19 = Level.objects.get(pk=19)

    episode3 = Episode(pk=3, name="Loops and Repetitions", first_level=level19, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode3.save()

    level29 = Level.objects.get(pk=29)

    episode4 = Episode(pk=4, name="Loops with Conditions", first_level=level29, r_branchiness=0,
                       r_loopiness=0, r_num_tiles=15, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode4.save()

    level33 = Level.objects.get(pk=33)

    episode5 = Episode(pk=5, name="If... Only", first_level=level33, r_branchiness=0.4,
                       r_loopiness=0.4, r_num_tiles=13, r_curviness=0.3, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=0)
    episode5.save()

    level44 = Level.objects.get(pk=44)

    episode6 = Episode(pk=6, name="Traffic Lights", first_level=level44, r_branchiness=0.5,
                       r_loopiness=0.1, r_num_tiles=35, r_curviness=0.2, r_pythonEnabled=0,
                       r_blocklyEnabled=1, r_trafficLights=1)
    episode6.save()

    episode1.next_episode = episode2
    episode2.next_episode = episode3
    episode3.next_episode = episode4
    episode4.next_episode = episode5
    episode5.next_episode = episode6

    episode1.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    episode2.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "deliver"])

    episode3.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "controls_repeat"])

    episode4.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "controls_repeat_until", "at_destination",
                                                     "controls_repeat"])
    
    episode5.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "controls_repeat_until", "at_destination",
                                                     "controls_if", "road_exists", "dead_end",
                                                     "controls_repeat", "turn_around"])

    episode6.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
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
        ('game', '0097_add_turnaround'),
    ]

    operations = [
        migrations.RunPython(run_operations)
    ]
