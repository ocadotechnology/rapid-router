# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def new_theme(Theme, Level, Decor):

    city = Theme(name='city', background='#969696', border='#686868', selected='#C1C1C1')
    city.save()

    tile = Decor(name='tile1', url='/static/game/image/decor/city/pavementTile.png', width=100,
                 height=100, theme=city)

    house = Decor(name='house', url='/static/game/image/decor/city/house.svg', width=50,
                  height=50, theme=city)

    bush = Decor(name='bush', url='/static/game/image/decor/city/bush.svg', width=50,
                 height=50, theme=city)

    shop = Decor(name='tree1', url='/static/game/image/decor/city/shop.svg', width=70,
                 height=70, theme=city)

    school = Decor(name='tree2', url='/static/game/image/decor/city/school.svg', width=100,
                   height=100, theme=city)

    hospital = Decor(name='pond', url='/static/game/image/decor/city/hospital.svg', width=113,
                     height=130, theme=city)

    tile.save()
    house.save()
    bush.save()
    shop.save()
    school.save()
    hospital.save()


def change_house_farm(Theme, Decor):

    farm = Theme.objects.get(name='farm')
    house = Decor.objects.get(name='house', theme=farm)
    house.url = '/static/game/image/decor/farm.house1.svg'
    house.save()


def populate_colours(Theme):
    
    grass = Theme.objects.get(name='grass')
    winter = Theme.objects.get(name='snow')
    farm = Theme.objects.get(name='farm')

    grass.background = '#a0c53a'
    grass.border = '#70961f'
    grass.selected = '#bce369'
    grass.save()

    winter.background = '#b3deff'
    winter.border = '#83c9fe'
    winter.selected = '#eff8ff'
    winter.save()

    farm.background = '#edd56b'
    farm.border = '#67564c'
    farm.selected = '#413127'
    farm.save()


def add_Phill(Character):

    Phil = Character(name='Phil', en_face='/static/game/image/characters/front_view/Phil.svg',
                     top_down='/static/game/image/characters/top_view/Phil.svg')
    Phil.save()


def run_changes(apps, schema_editor):
    
    Theme = apps.get_model('game', 'Theme')
    Level = apps.get_model('game', 'Level')
    Decor = apps.get_model('game', 'Decor')
    Character = apps.get_model('game', 'Character')

    new_theme(Theme, Level, Decor)
    change_house_farm(Theme, Decor)
    populate_colours(Theme)
    add_Phill(Character)


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0083_insert_colours_into_theme'),
    ]

    operations = [
        migrations.RunPython(run_changes)
    ]
