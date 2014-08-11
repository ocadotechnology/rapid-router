# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_farm_theme(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')
    Level = apps.get_model('game', 'Theme')
    Decor = apps.get_model('game', 'Decor')

    farm = Theme(name='farm', background='#413127', border='#392518', selected='#67564c')
    farm.save()

    house = Decor(name='house', url='/static/game/image/logCabin.svg', width=184, height=224,
                  theme=farm)
    house.save()

    cfc = Decor(name='cfc', url='/static/game/image/barn.svg', width=332, height=301, theme=farm)
    cfc.save()

    bush = Decor(name='bush', url='/static/game/image/hayBale.svg', width=50, height=30, theme=farm)
    bush.save()

    tree1 = Decor(name='tree1', url='/static/game/image/tree1.svg', width=100, height=1000,
                  theme=farm)
    tree1.save()

    tree2 = Decor(name='tree2', url='/static/game/image/tree2.svg', width=100, height=100,
                  theme=farm)
    tree2.save()

    pond = Decor(name='pond', url='/static/game/image/pond.svg', width=150, height=100, theme=farm)
    pond.save()

    tile1 = Decor(name='tile1', url='/static/game/image/farmCropsTile.svg', width=194, height=337,
                  theme=farm)
    tile1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0068_change_winter_colours'),
    ]

    operations = [
        migrations.RunPython(add_farm_theme)
    ]
