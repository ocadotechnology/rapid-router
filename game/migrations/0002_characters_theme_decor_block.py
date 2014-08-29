# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def add_characters(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    Character.objects.all().delete()

    van = Character(pk=1, name="Van", en_face='/static/game/image/characters/front_view/Van.svg',
                    top_down='/static/game/image/characters/top_view/Van.svg', height='20',
                    width='40')
    van.save()

    Dee = Character(pk=2, name="Dee", en_face='/static/game/image/characters/front_view/Dee.svg',
                    top_down='/static/game/image/characters/top_view/Dee.svg', height='28',
                    width='52')
    Dee.save()

    Nigel = Character(pk=3, name="Nigel", width='56', height='32',
                      en_face='/static/game/image/characters/front_view/Nigel.svg',
                      top_down='/static/game/image/characters/top_view/Nigel.svg')
    Nigel.save()

    Kirsty = Character(pk=4, name="Kirsty", height='32', width='60',
                       en_face='/static/game/image/characters/front_view/Kirsty.svg',
                       top_down='/static/game/image/characters/top_view/Kirsty.svg')
    Kirsty.save()

    Wes = Character(pk=5, name="Wes", en_face='/static/game/image/characters/front_view/Wes.svg',
                    top_down='/static/game/image/characters/top_view/Wes.svg', height='20',
                    width='40')
    Wes.save()

    Phil = Character(pk=6, name="Phil", height='32', width='60',
                     en_face='/static/game/image/characters/front_view/Phil.svg',
                     top_down='/static/game/image/characters/top_view/Phil.svg')
    Phil.save()


def add_theme_and_decor(apps, schema_editor):

    Theme = apps.get_model('game', 'Theme')
    Decor = apps.get_model('game', 'Decor')

    grass = Theme(background='#a0c53a', border='#70961f', name='grass', selected='#bce369')
    snow = Theme(background='#eef7ff', border='#83c9fe', name='snow', selected='#b3deff')
    farm = Theme(background='#a0c53a', border='#70961f', name='farm', selected='#bce369')
    city = Theme(background='#969696', border='#686868', name='city', selected='#C1C1C1')

    grass.save()
    snow.save()
    farm.save()
    city.save()

    Decor = apps.get_model('game', 'Decor')

    decor1 = Decor(name='tree1', theme=grass, url='/static/game/image/decor/grass/tree1.svg',
                   height=100, width=100)

    decor2 = Decor(name='tree2', theme=grass, url='/static/game/image/decor/grass/tree2.svg',
                   height=100, width=100)

    decor3 = Decor(name='bush', theme=grass, url='/static/game/image/decor/grass/bush.svg',
                   height=50, width=50)

    decor4 = Decor(name='house', theme=grass, url='/static/game/image/decor/grass/house.svg',
                   height=50, width=50)

    decor5 = Decor(name='cfc', theme=grass, url='/static/game/image/decor/grass/cfc.svg',
                   height=107, width=100)

    decor6 = Decor(name='pond', theme=grass, url='/static/game/image/decor/grass/pond.svg',
                   height=100, width=150)

    decor7 = Decor(name='tree1', theme=snow, url='/static/game/image/decor/snow/tree1.svg',
                   height=100, width=100)

    decor8 = Decor(name='tree2', theme=snow, url='/static/game/image/decor/snow/tree2.svg',
                   height=100, width=100)

    decor9 = Decor(name='bush', theme=snow, url='/static/game/image/decor/snow/bush.svg',
                   height=50, width=50)

    decor10 = Decor(name='house', theme=snow, url='/static/game/image/decor/snow/house.svg',
                    height=50, width=50)
    decor11 = Decor(name='cfc', theme=snow, url='/static/game/image/decor/snow/cfc.svg',
                    height=107, width=100)

    decor12 = Decor(name='pond', theme=snow, url='/static/game/image/decor/snow/pond.svg',
                    height=100, width=150)

    decor13 = Decor(name='tile1', theme=grass, url='/static/game/image/decor/grass/tile1.svg',
                    height=100, width=100)

    decor14 = Decor(name='tile1', theme=snow, url='/static/game/image/decor/snow/tile1.svg',
                    height=100, width=100)

    decor15 = Decor(name='tile2', theme=snow, url='/static/game/image/decor/snow/tile2.svg',
                    height=100, width=100)

    decor16 = Decor(name='house', theme=farm, url='/static/game/image/decor/farm/house1.svg',
                    height=224, width=184)

    decor17 = Decor(name='cfc', theme=farm, url='/static/game/image/decor/farm/cfc.svg',
                    height=301, width=332)

    decor18 = Decor(name='bush', theme=farm, url='/static/game/image/decor/farm/bush.svg',
                    height=30, width=50)

    decor19 = Decor(name='tree1', theme=farm, url='/static/game/image/decor/farm/tree1.svg',
                    height=100, width=100)

    decor20 = Decor(name='tree2', theme=farm, url='/static/game/image/decor/farm/house2.svg',
                    height=88, width=65)

    decor21 = Decor(name='pond', theme=farm, url='/static/game/image/decor/farm/crops.svg',
                    height=100, width=150)

    decor22 = Decor(name='tile1', theme=farm, url='/static/game/image/decor/farm/tile1.svg',
                    height=337, width=194)

    decor23 = Decor(name='tile1', theme=city, url='/static/game/image/decor/city/pavementTile.png',
                    height=100, width=100)

    decor24 = Decor(name='house', theme=city, url='/static/game/image/decor/city/house.svg',
                    height=50, width=50)

    decor25 = Decor(name='bush', theme=city, url='/static/game/image/decor/city/bush.svg',
                    height=50, width=50)

    decor26 = Decor(name='tree1', theme=city, url='/static/game/image/decor/city/shop.svg',
                    height=70, width=70)

    decor27 = Decor(name='tree2', theme=city, url='/static/game/image/decor/city/school.svg',
                    height=100, width=100)

    decor28 = Decor(name='pond', theme=city, url='/static/game/image/decor/city/hospital.svg',
                    height=157, width=140)

    decor1.save()
    decor2.save()
    decor3.save()
    decor4.save()
    decor5.save()
    decor6.save()
    decor7.save()
    decor8.save()
    decor9.save()
    decor10.save()
    decor11.save()
    decor12.save()
    decor13.save()
    decor14.save()
    decor15.save()
    decor16.save()
    decor17.save()
    decor18.save()
    decor19.save()
    decor20.save()
    decor21.save()
    decor22.save()
    decor23.save()
    decor24.save()
    decor25.save()
    decor26.save()
    decor27.save()
    decor28.save()


def add_blocks(apps, schema_editor):

    Block = apps.get_model('game', 'Block')

    block1 = Block(type='move_forwards')
    block2 = Block(type='turn_left')
    block3 = Block(type='turn_right')
    block4 = Block(type='turn_around')
    block5 = Block(type='wait')
    block6 = Block(type='deliver')
    block7 = Block(type='controls_whileUntil')
    block8 = Block(type='controls_repeat')
    block9 = Block(type='controls_if')
    block10 = Block(type='logic_negate')
    block11 = Block(type='at_destination')
    block12 = Block(type='road_exists')
    block13 = Block(type='dead_end')
    block14 = Block(type='traffic_light')
    block15 = Block(type='call_proc')
    block16 = Block(type='declare_proc')
    block17 = Block(type='controls_repeat_while')
    block18 = Block(type='controls_repeat_until')

    block1.save()
    block2.save()
    block3.save()
    block4.save()
    block5.save()
    block6.save()
    block7.save()
    block8.save()
    block9.save()
    block10.save()
    block11.save()
    block12.save()
    block13.save()
    block14.save()
    block15.save()
    block16.save()
    block17.save()
    block18.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_characters),
        migrations.RunPython(add_theme_and_decor),
        migrations.RunPython(add_blocks)
    ]
