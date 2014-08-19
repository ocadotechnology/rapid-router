# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def change_snow(Theme):

    snow = Theme.objects.get(name='snow')

    snow.background = '#eef7ff'
    snow.selected = '#b3deff'
    snow.save()


def fix_farm_house(Decor, Theme):

    farm = Theme.objects.get(name='farm')

    house = Decor.objects.get(name='house', theme=farm)
    house.url = '/static/game/image/decor/farm/house1.svg'
    house.save()


def assign_fuel_gauge(Level):

    levels = Level.objects.filter(pk__lte=38)

    for level in levels:
        level.fuel_gauge = False
        level.save()


def run_changes(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')
    Level = apps.get_model('game', 'Level')
    Theme = apps.get_model('game', 'Theme')

    change_snow(Theme)
    fix_farm_house(Decor, Theme)
    assign_fuel_gauge(Level)


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0085_level_fuel_gauge'),
    ]

    operations = [
        migrations.RunPython(run_changes)
    ]
