# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def initialise_themes_and_decor(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')
    Level = apps.get_model('game', 'Level')
    Decor = apps.get_model('game', 'Decor')

    initialise_themes(Theme, Level)
    initialise_decor(Theme, Decor)


def initialise_themes(Theme, Level):

    default = Theme(name='default')
    snow = Theme(name='snow')

    default.save()
    snow.save()


def initialise_decor(Theme, Decor):
    
    default = Theme.objects.get(name='default')
    snow = Theme.objects.get(name='snow')

    # initialise decor for the default theme
    tree1 = Decor(name='tree1', url='/static/game/image/tree1.svg', width=100, 
                  height=100, theme=default)
    tree2 = Decor(name='tree2', url='/static/game/image/tree2.svg', width=100,
                  height=100, theme=default)
    bush = Decor(name='bush', url='/static/game/image/bush.svg', width=50,
                 height=50, theme=default)
    destination = Decor(name='house', url='/static/game/image/house1_noGreen.svg',
                        width=50, height=50, theme=default)
    start = Decor(name='cfc', url='/static/game/image/OcadoCFC_no_road.svg',
                  width=100, height=107, theme=default)
    pond = Decor(name='pond', url='/static/game/image/pond.svg', width=300,
                 height=200, theme=default)

    tree1.save()
    tree2.save()
    bush.save()
    destination.save()
    start.save()
    pond.save()

    # initialise decor for the snow theme
    tree1 = Decor(name='tree1', url='/static/game/image/tree_snow1.svg', width=100, 
                  height=100, theme=snow)
    tree2 = Decor(name='tree2', url='/static/game/image/tree_snow2.svg', width=100,
                  height=100, theme=snow)
    bush = Decor(name='bush', url='/static/game/image/bush_snow.svg', width=50,
                 height=50, theme=snow)
    destination = Decor(name='house', url='/static/game/image/house_snow1.svg',
                        width=50, height=50, theme=snow)
    start = Decor(name='cfc', url='/static/game/image/OcadoCFC_no_road.svg',
                  width=100, height=107, theme=snow)
    pond = Decor(name='pond', url='/static/game/image/pond_snow.svg', width=300,
                 height=200, theme=snow)

    tree1.save()
    tree2.save()
    bush.save()
    destination.save()
    start.save()
    pond.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0040_decor_and_themes'),
    ]

    operations = [
        migrations.RunPython(initialise_themes_and_decor)
    ]
