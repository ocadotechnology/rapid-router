# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import re


def level_27_farm_theme(Level, Theme, Decor):

    farm = Theme.objects.get(name='farm')
    level27 = Level.objects.get(pk=27)

    level27.theme = farm
    level27.save()


def change_city_size(Theme, Decor):

    city = Theme.objects.get(name='city')

    hospital = Decor.objects.get(theme=city, name='pond')
    hospital.width = 140
    hospital.height = 157
    hospital.save()

    school = Decor.objects.get(theme=city, name='tree2')
    school.width = 120
    school.height = 120


def level_28_city_theme(Level, Theme, Decor, LevelDecor, Character):

    level28 = Level.objects.get(pk=28)
    city = Theme.objects.get(name='city')
    van = Character.objects.get(name='Van')

    LevelDecor.objects.filter(level=level28).delete()

    level28.theme = city
    level28.character = van
    level28.save()

    decor = '[{"coordinate":{"x":678,"y":495},"name":"tree1"},{"coordinate":{"x":356,"y":685},"name":"bush"},{"coordinate":{"x":437,"y":478},"name":"pond"},{"coordinate":{"x":429,"y":684},"name":"bush"},{"coordinate":{"x":509,"y":685},"name":"bush"},{"coordinate":{"x":587,"y":684},"name":"bush"},{"coordinate":{"x":565,"y":559},"name":"bush"},{"coordinate":{"x":385,"y":490},"name":"bush"},{"coordinate":{"x":385,"y":559},"name":"bush"},{"coordinate":{"x":567,"y":489},"name":"bush"},{"coordinate":{"x":516,"y":431},"name":"bush"},{"coordinate":{"x":436,"y":431},"name":"bush"},{"coordinate":{"x":700,"y":199},"name":"tree2"},{"coordinate":{"x":809,"y":307},"name":"bush"},{"coordinate":{"x":752,"y":307},"name":"bush"},{"coordinate":{"x":690,"y":306},"name":"bush"},{"coordinate":{"x":869,"y":308},"name":"bush"}]'
    regex = re.compile('(({"coordinate" *:{"x": *)([0-9]+)(,"y": *)([0-9]+)(}, *"name": *")([a-zA-Z0-9]+)("}))')

    items = regex.findall(decor)

    for item in items:
        name = item[6]
        levelDecor = LevelDecor(level=level28, x=item[2], y=item[4], decorName=name)
        levelDecor.save()


def fix_54_solution(Level):

    level54 = Level.objects.get(pk=54)
    level54.model_solution = '[10]'
    level54.save()


def change_farm_theme(Theme, Decor):

    farm = Theme.objects.get(name='farm')
    grass = Theme.objects.get(name='grass')
    pond = Decor.objects.get(name='pond', theme=farm)
    tree2 = Decor.objects.get(name='tree2', theme=farm)

    pond.url = '/static/game/image/decor/farm/crops.svg'
    pond.width = 97
    pond.height = 168
    pond.save()

    tree2.url = '/static/game/image/decor/farm/house2.svg'
    tree2.width = 65
    tree2.height = 88
    tree2.save()

    farm.background = grass.background
    farm.border = grass.border
    farm.selected = grass.selected
    farm.save()


def apply_changes(apps, schema_editor):

    Decor = apps.get_model('game', 'Decor')
    Level = apps.get_model('game', 'Level')
    LevelDecor = apps.get_model('game', 'LevelDecor')
    Theme = apps.get_model('game', 'Theme')
    Character = apps.get_model('game', 'Character')

    level_27_farm_theme(Level, Theme, Decor)
    fix_54_solution(Level)
    change_farm_theme(Theme, Decor)
    change_city_size(Theme, Decor)
    level_28_city_theme(Level, Theme, Decor, LevelDecor, Character)


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0086_themes_change_colours_set_fuel_gauge'),
    ]

    operations = [
        migrations.RunPython(apply_changes)
    ]
