# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def insert_model_scores(apps, schema_editor):
    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    level = Level.objects.get(id=1)
    level.model_solution = 1
    level.save()

    level = Level.objects.get(id=2)
    level.model_solution = 3
    level.save()

    level = Level.objects.get(id=3)
    level.model_solution = 2
    level.save()

    level = Level.objects.get(id=4)
    level.model_solution = 6
    level.save()

    level = Level.objects.get(id=5)
    level.model_solution = 12
    level.save()

    level = Level.objects.get(id=6)
    level.model_solution = 4
    level.save()

    level = Level.objects.get(id=7)
    level.model_solution = 13
    level.save()

    level = Level.objects.get(id=8)
    level.model_solution = 29
    level.save()

    level = Level.objects.get(id=9)
    level.model_solution = 34
    level.save()

    level = Level.objects.get(id=10)
    level.model_solution = 57
    level.save()

    level = Level.objects.get(id=11)
    level.model_solution = 2
    level.save()

    level = Level.objects.get(id=12)
    level.model_solution = 3
    level.save()

    level = Level.objects.get(id=13)
    level.model_solution = 3
    level.save()

    level = Level.objects.get(id=14)
    level.model_solution = 4
    level.save()

    level = Level.objects.get(id=15)
    level.model_solution = 4
    level.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                  "controls_whileUntil", "at_destination", 
                                                  "logic_negate"])
    level.save()

    level = Level.objects.get(id=16)
    level.model_solution = 5
    level.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right",
                                                  "controls_whileUntil", "at_destination", 
                                                  "logic_negate"])
    level.save()

    level = Level.objects.get(id=17)
    level.model_solution = 6
    level.save()

    level = Level.objects.get(id=18)
    level.model_solution = 7
    level.save()

    level = Level.objects.get(id=19)
    level.model_solution = 9
    level.save()

    level = Level.objects.get(id=20)
    level.model_solution = 9
    level.save()

    level = Level.objects.get(id=21)
    level.model_solution = 2
    level.save()

    level = Level.objects.get(id=22)
    level.model_solution = 2
    level.save()

    level = Level.objects.get(id=23)
    level.model_solution = 6
    level.save()

    level = Level.objects.get(id=24)
    level.model_solution = 12
    level.save()

    level = Level.objects.get(id=25)
    level.model_solution = 4
    level.save()

    level = Level.objects.get(id=26)
    level.model_solution = 10
    level.save()

    level = Level.objects.get(id=27)
    level.model_solution = 17
    level.save()

    level = Level.objects.get(id=28)
    level.model_solution = 8
    level.save()



class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_merge'),
    ]

    operations = [
        migrations.RunPython(insert_model_scores),
    ]
