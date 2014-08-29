# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def episodes(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Episode = apps.get_model('game', 'Episode')
    Block = apps.get_model('game', 'Block')

    # Episode 9

    level29 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":197,"y":202},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":196,"y":94},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="21",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3,5]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3]},{"coordinate":[3,3],"connectedNodes":[2,6]},{"coordinate":[4,3],"connectedNodes":[5]}]',
            threads = 2)
    level29.save()
    level29.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards", "turn_around"])
    level29.save()
    
    episode9 = Episode(name="Threads", first_level=level29)
    episode9.save()

    episode8 = Episode.objects.get(name="Procedures")
    episode8.next_episode = episode9
    episode8.save();

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0025_level_threads')
    ]

    operations = [
        migrations.RunPython(episodes),
    ]