# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def fix_blocks(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    level1 = Level.objects.get(id=1);
    level2 = Level.objects.get(id=2);
    level3 = Level.objects.get(id=3);
    level4 = Level.objects.get(id=4);
    level5 = Level.objects.get(id=5);
    level6 = Level.objects.get(id=6);
    level7 = Level.objects.get(id=7);
    level8 = Level.objects.get(id=8);
    level9 = Level.objects.get(id=9);
    level10 = Level.objects.get(id=10);
    level11 = Level.objects.get(id=11);
    level12 = Level.objects.get(id=12);

    forwards = Block.objects.filter(type__in=["move_forwards"])
    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level1.blocks = forwards
    level2.blocks = forwards
    level3.blocks = Block.objects.filter(type__in=["move_forwards", "turn_right"])
    level4.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left"])
    level5.blocks = blocks
    level6.blocks = blocks
    level7.blocks = blocks
    level8.blocks = blocks
    level9.blocks = blocks
    level10.blocks = blocks
    level11.blocks = blocks
    level12.blocks = blocks

    level1.save()
    level2.save()
    level3.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()

    ##### Shortest path episode

    level13 = Level.objects.get(id=13);
    level14 = Level.objects.get(id=14);
    level15 = Level.objects.get(id=15);
    level16 = Level.objects.get(id=16);
    level17 = Level.objects.get(id=17);
    level18 = Level.objects.get(id=18);

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level13.blocks = blocks
    level14.blocks = blocks
    level15.blocks = blocks
    level16.blocks = blocks
    level17.blocks = blocks
    level18.blocks = blocks

    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()

    ##### Simple repeat

    level19 = Level.objects.get(id=19);
    level20 = Level.objects.get(id=20);
    level21 = Level.objects.get(id=21);
    level22 = Level.objects.get(id=22);
    level23 = Level.objects.get(id=23);
    level24 = Level.objects.get(id=24);
    level25 = Level.objects.get(id=25);
    level26 = Level.objects.get(id=26);
    level27 = Level.objects.get(id=27);
    level28 = Level.objects.get(id=28);

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_repeat"])

    level19.blocks = blocks
    level20.blocks = blocks
    level21.blocks = blocks
    level22.blocks = blocks
    level23.blocks = blocks
    level24.blocks = blocks
    level25.blocks = blocks
    level26.blocks = blocks
    level27.blocks = blocks
    level28.blocks = blocks

    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()

    ##### Until

    level29 = Level.objects.get(id=29);
    level30 = Level.objects.get(id=30);
    level31 = Level.objects.get(id=31);
    level32 = Level.objects.get(id=32);

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                            "controls_whileUntil", "at_destination"])

    level29.blocks = blocks
    level30.blocks = blocks
    level31.blocks = blocks
    level32.blocks = blocks

    level29.save()
    level30.save()
    level31.save()
    level32.save()

    ##### If do

    level33 = Level.objects.get(id=33);
    level34 = Level.objects.get(id=34);
    level35 = Level.objects.get(id=35);
    level36 = Level.objects.get(id=36);
    level37 = Level.objects.get(id=37);
    level38 = Level.objects.get(id=38);
    level39 = Level.objects.get(id=39);
    level40 = Level.objects.get(id=40);
    level41 = Level.objects.get(id=41);
    level42 = Level.objects.get(id=42);
    level43 = Level.objects.get(id=43);

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "controls_if", "logic_negate",
                                            "road_exists", "at_destination"])

    blocks_around = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                   "controls_whileUntil", "controls_if",
                                                   "logic_negate", "road_exists", "at_destination",
                                                   "turn_around", "controls_repeat", "road_exists",
                                                   "dead_end"])

    level33.blocks = blocks
    level34.blocks = blocks
    level35.blocks = blocks
    level36.blocks = blocks
    level37.blocks = blocks
    level38.blocks = blocks
    level39.blocks = blocks
    level40.blocks = blocks_around
    level41.blocks = blocks_around
    level42.blocks = blocks_around
    level43.blocks = blocks_around

    level33.save()
    level34.save()
    level35.save()
    level36.save()
    level37.save()
    level38.save()
    level39.save()
    level40.save()
    level41.save()
    level42.save()
    level43.save()

    ##### Traffic lights

    level44 = Level.objects.get(id=44);
    level45 = Level.objects.get(id=45);
    level46 = Level.objects.get(id=46);
    level47 = Level.objects.get(id=47);
    level48 = Level.objects.get(id=48);
    level49 = Level.objects.get(id=49);
    level50 = Level.objects.get(id=50);

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right", "wait",
                                            "controls_repeat", "controls_whileUntil", "controls_if",
                                            "logic_negate", "road_exists", "at_destination",
                                            "traffic_light"])

    level44.blocks = blocks
    level45.blocks = blocks
    level46.blocks = blocks
    level47.blocks = blocks
    level48.blocks = blocks
    level49.blocks = blocks
    level50.blocks = blocks

    level44.save()
    level45.save()
    level46.save()
    level47.save()
    level48.save()
    level49.save()
    level50.save()

    ##### God knows what episode is this.

    ##### Procedure

    level52 = Level.objects.get(id=52);

    blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                            "controls_whileUntil", "controls_if", "logic_negate",
                                            "road_exists", "at_destination", "turn_around",
                                            "controls_repeat", "road_exists", "dead_end",
                                            "turn_around", "call_proc", "declare_proc", "text"])

    level52.blocks = blocks
    level52.save()


    level53 = Level.objects.get(id=53);
    level53.blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards",
                                                    "turn_around"])
    level53.save()


    ##### Extra fixes from later migrations

    blocks_around = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                   "controls_whileUntil", "controls_if",
                                                   "logic_negate", "road_exists", "at_destination",
                                                   "turn_around", "controls_repeat", "road_exists",
                                                   "dead_end"])

    blocks_traffic = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right", "wait",
                                                    "controls_repeat", "controls_whileUntil", "controls_if",
                                                    "logic_negate", "road_exists", "at_destination",
                                                    "traffic_light", "dead_end", "turn_around"])


    level39 = Level.objects.get(id=39)
    level39.blocks = blocks_around

    level48 = Level.objects.get(id=48)
    level48.blocks = blocks_traffic

    level48.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0047_merge'),
    ]

    operations = [
        migrations.RunPython(fix_blocks),
    ]
