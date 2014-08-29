# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def apply_changes(apps, schema_editor):

    Block = apps.get_model('game', 'Block')
    Episode = apps.get_model('game', 'Episode')
    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')

    seutp_blocks_in_db(Block, Level)
    levels_49_50_city(Level, Theme)
    levels_while_until(Level, Block)
    episode_repeat_until(Level, Episode, Block)


def seutp_blocks_in_db(Block, Level):

    while_block = Block(type='controls_repeat_while')
    until_block = Block(type='controls_repeat_until')

    while_block.save()
    until_block.save()


def episode_repeat_until(Level, Episode, Block):

    level29 = Level.objects.get(pk=29)
    if_only = Episode.objects.get(name='If... Only')
    traffic_lights = Episode.objects.get(name='Traffic Lights')
    loops_and_repetitions = Episode.objects.get(name='Loops and Repetitions')

    # Reorder the next episodes to make room

    episode = Episode(name='Loops with Conditions', first_level=level29, next_episode=if_only)
    episode.save()

    episode.r_branchiness = 0.0
    episode.r_loopiness = 0.0
    episode.r_curviness = 0.2
    episode.r_num_tiles = 15

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination"])
    episode.blocks = blocks

    episode.save()

    loops_and_repetitions.next_episode = episode
    loops_and_repetitions.save()

    traffic_lights.next_episode = None
    traffic_lights.save()

    levels = Level.objects.filter(pk__in=range(29, 33))

    for level in levels:
        level.blocks = blocks
        level.save()


def levels_49_50_city(Level, Theme):

    city = Theme.objects.get(name='city')

    level49 = Level.objects.get(pk=49)
    level50 = Level.objects.get(pk=50)

    level49.theme = city
    level50.theme = city

    level49.save()
    level50.save()


def levels_while_until(Level, Block):

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "at_destination"])

    for i in range(33, 39):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "at_destination",
                                            "controls_repeat", "dead_end"])

    for i in range(39, 44):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat_until", "at_destination",
                                            "controls_if", "road_exists", "at_destination",
                                            "controls_repeat", "dead_end", "controls_repeat_while",
                                            "wait", "traffic_light"])

    for i in range(44, 51):
        level = Level.objects.get(pk=i)
        level.blocks = blocks
        level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0088_merge'),
    ]

    operations = [
        migrations.RunPython(apply_changes)
    ]
