# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def drop_and_add_new(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')

    Episode.objects.all().delete()

    episodes(Episode, Level, Block)


def episodes(Episode, Level, Block):

    level1 = Level.objects.get(id=1)
    level2 = Level.objects.get(id=13)
    level3 = Level.objects.get(id=19)
    level4 = Level.objects.get(id=33)
    level5 = Level.objects.get(id=44)
    level6 = Level.objects.get(id=51)

    episode1 = Episode(name="Getting Started", first_level=level1, r_branchiness=0.0,
                       r_loopiness=0.0, r_curviness=0.5, r_num_tiles=10)
    episode2 = Episode(name="Shortest Route", first_level=level2, r_branchiness=0.4,
                       r_loopiness=0.0, r_curviness=0.3, r_num_tiles=15)
    episode3 = Episode(name="Loops and Repetitions", first_level=level3, r_branchiness=0.0,
                       r_loopiness=0.4, r_curviness=0.3, r_num_tiles=13)
    episode4 = Episode(name="If... Only", first_level=level4, r_branchiness=0.4, r_loopiness=0.4,
                       r_curviness=0.3, r_num_tiles=13)
    episode5 = Episode(name="Traffic Lights", first_level=level5, r_branchiness=0.2,
                       r_loopiness=0.1, r_curviness=0.4, r_num_tiles=13)
    episode6 = Episode(name="Miscellaneous", first_level=level6, r_branchiness=0.4, r_loopiness=0.4,
                       r_curviness=0.4, r_num_tiles=20)

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()

    episode1.next_episode = episode2
    episode2.next_episode = episode3
    episode3.next_episode = episode4
    episode4.next_episode = episode5
    episode5.next_episode = episode6

    episode1.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])
    episode2.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])
    episode3.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                     "controls_whileUntil", "at_destination",
                                                     "controls_repeat"])
    episode4.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                     "controls_whileUntil", "controls_if",
                                                     "logic_negate", "road_exists",
                                                     "at_destination", "turn_around",
                                                     "controls_repeat", "road_exists", "dead_end"])
    episode5.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                     "wait", "controls_repeat", "controls_if",
                                                     "logic_negate", "road_exists", "traffic_light",
                                                     "controls_whileUntil", "at_destination"])
    episode6.blocks = Block.objects.all()

    episode1.save()
    episode2.save()
    episode3.save()
    episode4.save()
    episode5.save()
    episode6.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0029_new_levels'),
    ]

    operations = [
        migrations.RunPython(drop_and_add_new),
    ]
