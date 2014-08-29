
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def populate_destinations(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    level = Level.objects.get(pk=1)
    level.destinations = [[2, 3]]
    level.save()

    level = Level.objects.get(pk=2)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=3)
    level.destinations = [[2, 2]]
    level.save()

    level = Level.objects.get(pk=4)
    level.destinations = [[4, 5]]
    level.save()

    level = Level.objects.get(pk=5)
    level.destinations = [[4, 6]]
    level.save()

    level = Level.objects.get(pk=6)
    level.destinations = [[6, 1]]
    level.save()

    level = Level.objects.get(pk=7)
    level.destinations = [[5, 3]]
    level.save()

    level = Level.objects.get(pk=8)
    level.destinations = [[4, 1]]
    level.save()

    level = Level.objects.get(pk=9)
    level.destinations = [[8, 1]]
    level.save()

    level = Level.objects.get(pk=10)
    level.destinations = [[3, 3]]
    level.save()

    level = Level.objects.get(pk=11)
    level.destinations = [[1, 3]]
    level.save()

    level = Level.objects.get(pk=12)
    level.destinations = [[1, 3]]
    level.save()

    level = Level.objects.get(pk=13)
    level.destinations = [[0, 1]]
    level.save()

    level = Level.objects.get(pk=14)
    level.destinations = [[2, 5]]
    level.save()

    level = Level.objects.get(pk=15)
    level.destinations = [[7, 2]]
    level.save()

    level = Level.objects.get(pk=16)
    level.destinations = [[7, 0]]
    level.save()

    level = Level.objects.get(pk=17)
    level.destinations = [[4, 1]]
    level.save()

    level = Level.objects.get(pk=18)
    level.destinations = [[2, 7]]
    level.save()

    level = Level.objects.get(pk=19)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=20)
    level.destinations = [[4, 6]]
    level.save()

    level = Level.objects.get(pk=21)
    level.destinations = [[3, 7]]
    level.save()

    level = Level.objects.get(pk=22)
    level.destinations = [[7, 5]]
    level.save()

    level = Level.objects.get(pk=23)
    level.destinations = [[7, 2]]
    level.save()

    level = Level.objects.get(pk=24)
    level.destinations = [[2, 2]]
    level.save()

    level = Level.objects.get(pk=25)
    level.destinations = [[8, 2]]
    level.save()

    level = Level.objects.get(pk=26)
    level.destinations = [[]]
    level.save()

    level = Level.objects.get(pk=27)
    level.destinations = [[]]
    level.save()

    level = Level.objects.get(pk=28)
    level.destinations = [[]]
    level.save()

    level = Level.objects.get(pk=29)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=30)
    level.destinations = [[4, 6]]
    level.save()
    level = Level.objects.get(pk=31)
    level.destinations = [[3, 7]]
    level.save()

    level = Level.objects.get(pk=32)
    level.destinations = [[5, 0]]
    level.save()

    level = Level.objects.get(pk=33)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=34)
    level.destinations = [[6, 6]]
    level.save()

    level = Level.objects.get(pk=35)
    level.destinations = [[1, 1]]
    level.save()

    level = Level.objects.get(pk=36)
    level.destinations = [[5, 3]]
    level.save()

    level = Level.objects.get(pk=37)
    level.destinations = [[3, 2]]
    level.save()

    level = Level.objects.get(pk=38)
    level.destinations = [[6, 0]]
    level.save()

    level = Level.objects.get(pk=39)
    level.destinations = [[4, 2]]
    level.save()

    level = Level.objects.get(pk=40)
    level.destinations = [[8, 2]]
    level.save()

    level = Level.objects.get(pk=41)
    level.destinations = [[5, 3]]
    level.save()

    level = Level.objects.get(pk=42)
    level.destinations = [[4, 2]]
    level.save()

    level = Level.objects.get(pk=43)
    level.destinations = [[5, 7]]
    level.save()

    level = Level.objects.get(pk=44)
    level.destinations = [[6, 3]]
    level.save()

    level = Level.objects.get(pk=45)
    level.destinations = [[0, 3]]
    level.save()

    level = Level.objects.get(pk=46)
    level.destinations = [[2, 6]]
    level.save()

    level = Level.objects.get(pk=47)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=48)
    level.destinations = [[1, 2]]
    level.save()

    level = Level.objects.get(pk=49)
    level.destinations = [[9, 6]]
    level.save()

    level = Level.objects.get(pk=50)
    level.destinations = [[6, 4]]
    level.save()

    level = Level.objects.get(pk=51)
    level.destinations = [[7, 7]]
    level.save()

    level = Level.objects.get(pk=52)
    level.destinations = [[4, 2]]
    level.save()

    level = Level.objects.get(pk=53)
    level.destinations = [[4, 3]]
    level.save()

    level = Level.objects.get(pk=54)
    level.destinations = [[4, 2], [4, 4]]
    level.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0054_level_destinations'),
    ]

    operations = [
    	migrations.RunPython(populate_destinations)
    ]
