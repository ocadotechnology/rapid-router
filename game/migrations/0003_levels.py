# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def episode1(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    level10 = Level(
            destination=[9, 7],
            decor='[{"coordinate":{"x":195,"y":619},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":108,"y":356},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":515,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":595,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":700,"y":510},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":496,"y":306},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":296,"y":63},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":691,"y":147},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":887,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":891,"y":68},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=57,
            name='10',
            path='[{"coordinate":[0,0],"connectedNodes":[57]},{"coordinate":[8,2],"connectedNodes":[2,58]},{"coordinate":[8,3],"connectedNodes":[3,1]},{"coordinate":[7,3],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[6,1],"connectedNodes":[7,5]},{"coordinate":[5,1],"connectedNodes":[8,6]},{"coordinate":[4,1],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,14]},{"coordinate":[0,1],"connectedNodes":[17,15]},{"coordinate":[0,2],"connectedNodes":[18,16]},{"coordinate":[0,3],"connectedNodes":[19,17]},{"coordinate":[0,4],"connectedNodes":[20,18]},{"coordinate":[0,5],"connectedNodes":[21,19]},{"coordinate":[1,5],"connectedNodes":[20,22]},{"coordinate":[1,6],"connectedNodes":[23,21]},{"coordinate":[0,6],"connectedNodes":[24,22]},{"coordinate":[0,7],"connectedNodes":[25,23]},{"coordinate":[1,7],"connectedNodes":[24,26]},{"coordinate":[2,7],"connectedNodes":[25,27]},{"coordinate":[3,7],"connectedNodes":[26,28]},{"coordinate":[3,6],"connectedNodes":[27,29]},{"coordinate":[4,6],"connectedNodes":[28,30]},{"coordinate":[5,6],"connectedNodes":[29,31]},{"coordinate":[5,5],"connectedNodes":[32,30]},{"coordinate":[4,5],"connectedNodes":[33,31]},{"coordinate":[3,5],"connectedNodes":[34,32]},{"coordinate":[2,5],"connectedNodes":[33,35]},{"coordinate":[2,4],"connectedNodes":[34,36]},{"coordinate":[3,4],"connectedNodes":[35,37]},{"coordinate":[4,4],"connectedNodes":[36,38]},{"coordinate":[5,4],"connectedNodes":[37,39]},{"coordinate":[6,4],"connectedNodes":[38,40]},{"coordinate":[7,4],"connectedNodes":[39,41]},{"coordinate":[8,4],"connectedNodes":[40,42]},{"coordinate":[8,5],"connectedNodes":[43,41]},{"coordinate":[8,6],"connectedNodes":[44,42]},{"coordinate":[7,6],"connectedNodes":[45,43]},{"coordinate":[6,6],"connectedNodes":[46,44]},{"coordinate":[6,7],"connectedNodes":[47,45]},{"coordinate":[7,7],"connectedNodes":[46,48]},{"coordinate":[8,7],"connectedNodes":[47,49]},{"coordinate":[9,7],"connectedNodes":[48]},{"coordinate":[8,0],"connectedNodes":[51,58]},{"coordinate":[7,0],"connectedNodes":[52,50]},{"coordinate":[6,0],"connectedNodes":[53,51]},{"coordinate":[5,0],"connectedNodes":[54,52]},{"coordinate":[4,0],"connectedNodes":[55,53]},{"coordinate":[3,0],"connectedNodes":[56,54]},{"coordinate":[2,0],"connectedNodes":[57,55]},{"coordinate":[1,0],"connectedNodes":[0,56]},{"coordinate":[8,1],"connectedNodes":[1,50]}]',
            next_level=None)
    level10.save()

    level9 = Level(
            destination=[0, 4],
            decor='[{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":293,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":606},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":407,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":507,"y":603},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":304,"y":200},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":408,"y":198},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":509,"y":208},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":506,"y":-3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":402,"y":8},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":295,"y":11},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name='9',
            path='[{"coordinate":[4,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[0,2]},{"coordinate":[6,3],"connectedNodes":[1,3]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[7,9]},{"coordinate":[2,4],"connectedNodes":[8,10]},{"coordinate":[2,3],"connectedNodes":[9,11]},{"coordinate":[2,2],"connectedNodes":[10,12]},{"coordinate":[2,1],"connectedNodes":[11,13]},{"coordinate":[3,1],"connectedNodes":[12,14]},{"coordinate":[4,1],"connectedNodes":[13,15]},{"coordinate":[5,1],"connectedNodes":[14,16]},{"coordinate":[6,1],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[8,1],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[20,18]},{"coordinate":[8,3],"connectedNodes":[21,19]},{"coordinate":[8,4],"connectedNodes":[22,20]},{"coordinate":[8,5],"connectedNodes":[23,21]},{"coordinate":[8,6],"connectedNodes":[24,22]},{"coordinate":[8,7],"connectedNodes":[25,23]},{"coordinate":[7,7],"connectedNodes":[26,24]},{"coordinate":[6,7],"connectedNodes":[27,25]},{"coordinate":[5,7],"connectedNodes":[28,26]},{"coordinate":[4,7],"connectedNodes":[29,27]},{"coordinate":[3,7],"connectedNodes":[30,28]},{"coordinate":[2,7],"connectedNodes":[31,29]},{"coordinate":[1,7],"connectedNodes":[30,32]},{"coordinate":[1,6],"connectedNodes":[31,33]},{"coordinate":[1,5],"connectedNodes":[32,34]},{"coordinate":[1,4],"connectedNodes":[35,33]},{"coordinate":[0,4],"connectedNodes":[34]}]',
            next_level=level10)
    level9.save()

    level8 = Level(
            destination=[7 ,3],
            decor='[{"coordinate":{"x":596,"y":585},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":233,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":248,"y":32},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":709,"y":20},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":603},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":99,"y":490},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":597,"y":352},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="8",
            path='[{"coordinate":[9,5],"connectedNodes":[1]},{"coordinate":[8,5],"connectedNodes":[2,0]},{"coordinate":[7,5],"connectedNodes":[3,1]},{"coordinate":[7,6],"connectedNodes":[4,2]},{"coordinate":[7,7],"connectedNodes":[5,3]},{"coordinate":[6,7],"connectedNodes":[6,4]},{"coordinate":[5,7],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[5,3],"connectedNodes":[11,9]},{"coordinate":[4,3],"connectedNodes":[12,10]},{"coordinate":[3,3],"connectedNodes":[13,11]},{"coordinate":[3,4],"connectedNodes":[14,12]},{"coordinate":[3,5],"connectedNodes":[15,13]},{"coordinate":[2,5],"connectedNodes":[14,16]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[18,16]},{"coordinate":[0,4],"connectedNodes":[17,19]},{"coordinate":[0,3],"connectedNodes":[18,20]},{"coordinate":[0,2],"connectedNodes":[19,21]},{"coordinate":[0,1],"connectedNodes":[20,22]},{"coordinate":[1,1],"connectedNodes":[21,23]},{"coordinate":[2,1],"connectedNodes":[22,24]},{"coordinate":[3,1],"connectedNodes":[23,25]},{"coordinate":[4,1],"connectedNodes":[24,26]},{"coordinate":[5,1],"connectedNodes":[25,27]},{"coordinate":[6,1],"connectedNodes":[26,28]},{"coordinate":[7,1],"connectedNodes":[27,29]},{"coordinate":[7,2],"connectedNodes":[30,28]},{"coordinate":[7,3],"connectedNodes":[29]}]',
            next_level=level9)
    level8.save()

    level7 = Level(
            destination=[8, 1],
            decor='[{"coordinate":{"x":167,"y":207},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":364,"y":202},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":571,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":465,"y":199},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":29,"y":433},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":505,"y":652},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="7",
            path='[{"coordinate":[6,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[2,0]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[1,1],"connectedNodes":[6,8]},{"coordinate":[2,1],"connectedNodes":[7,9]},{"coordinate":[3,1],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[12,14]},{"coordinate":[8,1],"connectedNodes":[13]}]',
            next_level=level8)
    level7.save()

    level6 = Level(
            destination=[4, 1],
            decor='[{"coordinate":{"x":271,"y":406},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y": 392},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":63,"y":397},"url":"/static/game/image/tree1.svg" },{"coordinate":{"x":114,"y":478},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":697,"y":198},"url": "/static/game/image/tree2.svg"},{"coordinate":{"x":532,"y":76},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":705,"y":44},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="6",
            path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,1],"connectedNodes":[4]}]',
            next_level=level7)
    level6.save()

    level5 = Level(
            destination=[5, 3],
            decor='[{"coordinate":{"x":479,"y":551},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":404,"y":446},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":363,"y":354},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":428,"y":124},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":212,"y":130},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":398,"y":590},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":261,"y":670},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":232,"y":428},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":25,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":230,"y":333},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":227,"y":236},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":133},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-21,"y":-11},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":633,"y":16},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":688,"y":601},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":634,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":827,"y":616},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":751,"y":450},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":833,"y":47},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":842,"y":374},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":703,"y":237},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":535,"y":353},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="5",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]',
            next_level=level6)
    level5.save()

    level4 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":138,"y":457},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":344},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":237,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":259,"y":441},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":355,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":45,"y":363},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="4",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]',
            next_level=level5)
    level4.save()

    level3 = Level(
            destination=[2, 2],
            decor='[{"coordinate":{"x":0,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":404},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":601,"y":403},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":402},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":804,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":903,"y":401},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="3",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,2],"connectedNodes":[2]}]',
            next_level=level4)
    level3.save()

    level2 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":67,"y":570},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":663,"y":443},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":192,"y":58},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="2",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]',
            next_level=level3)
    level2.save()

    level1 = Level(
            destination=[2, 3],
            decor='[{''coordinate'': new ocargo.Coordinate(100, 100), ''url'': ''/static/game/image/tree1.svg''}]',
            default=True,
            max_fuel=50,
            name="1",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1]}] ',
            next_level=level2)
    level1.save()

    # add blocks
    Block = apps.get_model('game', 'Block')
    forwards = Block.objects.filter(type__in=["move_forward"])
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forward"])

    level1.blocks = forwards
    level2.blocks = forwards
    level3.blocks = Block.objects.filter(type__in=["move_forward", "turn_right"])
    level4.blocks = episode_blocks
    level5.blocks = episode_blocks
    level6.blocks = episode_blocks
    level7.blocks = episode_blocks
    level8.blocks = episode_blocks
    level9.blocks = episode_blocks
    level10.blocks = episode_blocks
    for level in [level1, level2, level3, level4, level5, level6, \
            level7, level8, level9, level10]:
        level.save()


class Migration(migrations.Migration):

    dependencies = [
            ('game', '0002_blocks'),
    ]

    operations = [
            migrations.RunPython(episode1),
    ]
