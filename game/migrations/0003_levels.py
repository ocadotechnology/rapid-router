# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def levels(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    level1 = Level(
            destination=[2, 3],
            decor='[{"coordinate":{"x":100,"y":100}, "url": "/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="1",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1]}] ')
    level1.save()

    level2 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":67,"y":570},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":663,"y":443},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":192,"y":58},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="2",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]')
    level2.save()

    level3 = Level(
            destination=[2, 2],
            decor='[{"coordinate":{"x":0,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":404},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":601,"y":403},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":402},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":804,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":903,"y":401},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="3",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,2],"connectedNodes":[2]}]')
    level3.save()

    level4 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":138,"y":457},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":344},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":237,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":259,"y":441},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":355,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":45,"y":363},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="4",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]')
    level4.save()

    level5 = Level(
            destination=[5, 3],
            decor='[{"coordinate":{"x":479,"y":551},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":404,"y":446},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":363,"y":354},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":428,"y":124},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":212,"y":130},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":398,"y":590},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":261,"y":670},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":232,"y":428},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":25,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":230,"y":333},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":227,"y":236},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":133},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-21,"y":-11},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":633,"y":16},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":688,"y":601},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":634,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":827,"y":616},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":751,"y":450},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":833,"y":47},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":842,"y":374},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":703,"y":237},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":535,"y":353},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="5",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]')
    level5.save()

    level6 = Level(
            destination=[4, 1],
            decor='[{"coordinate":{"x":271,"y":406},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y": 392},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":63,"y":397},"url":"/static/game/image/tree1.svg" },{"coordinate":{"x":114,"y":478},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":697,"y":198},"url": "/static/game/image/tree2.svg"},{"coordinate":{"x":532,"y":76},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":705,"y":44},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="6",
            path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,1],"connectedNodes":[4]}]')
    level6.save()

    level7 = Level(
            destination=[8, 1],
            decor='[{"coordinate":{"x":167,"y":207},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":364,"y":202},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":571,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":465,"y":199},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":29,"y":433},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":505,"y":652},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="7",
            path='[{"coordinate":[6,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[2,0]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[1,1],"connectedNodes":[6,8]},{"coordinate":[2,1],"connectedNodes":[7,9]},{"coordinate":[3,1],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[12,14]},{"coordinate":[8,1],"connectedNodes":[13]}]')
    level7.save()

    level8 = Level(
            destination=[7 ,3],
            decor='[{"coordinate":{"x":596,"y":585},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":233,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":248,"y":32},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":709,"y":20},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":603},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":99,"y":490},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":597,"y":352},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="8",
            path='[{"coordinate":[9,5],"connectedNodes":[1]},{"coordinate":[8,5],"connectedNodes":[2,0]},{"coordinate":[7,5],"connectedNodes":[3,1]},{"coordinate":[7,6],"connectedNodes":[4,2]},{"coordinate":[7,7],"connectedNodes":[5,3]},{"coordinate":[6,7],"connectedNodes":[6,4]},{"coordinate":[5,7],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[5,3],"connectedNodes":[11,9]},{"coordinate":[4,3],"connectedNodes":[12,10]},{"coordinate":[3,3],"connectedNodes":[13,11]},{"coordinate":[3,4],"connectedNodes":[14,12]},{"coordinate":[3,5],"connectedNodes":[15,13]},{"coordinate":[2,5],"connectedNodes":[14,16]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[18,16]},{"coordinate":[0,4],"connectedNodes":[17,19]},{"coordinate":[0,3],"connectedNodes":[18,20]},{"coordinate":[0,2],"connectedNodes":[19,21]},{"coordinate":[0,1],"connectedNodes":[20,22]},{"coordinate":[1,1],"connectedNodes":[21,23]},{"coordinate":[2,1],"connectedNodes":[22,24]},{"coordinate":[3,1],"connectedNodes":[23,25]},{"coordinate":[4,1],"connectedNodes":[24,26]},{"coordinate":[5,1],"connectedNodes":[25,27]},{"coordinate":[6,1],"connectedNodes":[26,28]},{"coordinate":[7,1],"connectedNodes":[27,29]},{"coordinate":[7,2],"connectedNodes":[30,28]},{"coordinate":[7,3],"connectedNodes":[29]}]')
    level8.save()

    level9 = Level(
            destination=[0, 4],
            decor='[{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":293,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":606},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":407,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":507,"y":603},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":304,"y":200},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":408,"y":198},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":509,"y":208},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":506,"y":-3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":402,"y":8},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":295,"y":11},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name='9',
            path='[{"coordinate":[4,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[0,2]},{"coordinate":[6,3],"connectedNodes":[1,3]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[7,9]},{"coordinate":[2,4],"connectedNodes":[8,10]},{"coordinate":[2,3],"connectedNodes":[9,11]},{"coordinate":[2,2],"connectedNodes":[10,12]},{"coordinate":[2,1],"connectedNodes":[11,13]},{"coordinate":[3,1],"connectedNodes":[12,14]},{"coordinate":[4,1],"connectedNodes":[13,15]},{"coordinate":[5,1],"connectedNodes":[14,16]},{"coordinate":[6,1],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[8,1],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[20,18]},{"coordinate":[8,3],"connectedNodes":[21,19]},{"coordinate":[8,4],"connectedNodes":[22,20]},{"coordinate":[8,5],"connectedNodes":[23,21]},{"coordinate":[8,6],"connectedNodes":[24,22]},{"coordinate":[8,7],"connectedNodes":[25,23]},{"coordinate":[7,7],"connectedNodes":[26,24]},{"coordinate":[6,7],"connectedNodes":[27,25]},{"coordinate":[5,7],"connectedNodes":[28,26]},{"coordinate":[4,7],"connectedNodes":[29,27]},{"coordinate":[3,7],"connectedNodes":[30,28]},{"coordinate":[2,7],"connectedNodes":[31,29]},{"coordinate":[1,7],"connectedNodes":[30,32]},{"coordinate":[1,6],"connectedNodes":[31,33]},{"coordinate":[1,5],"connectedNodes":[32,34]},{"coordinate":[1,4],"connectedNodes":[35,33]},{"coordinate":[0,4],"connectedNodes":[34]}]')
    level9.save()

    level10 = Level(
            destination=[9, 7],
            decor='[{"coordinate":{"x":195,"y":619},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":108,"y":356},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":515,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":595,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":700,"y":510},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":496,"y":306},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":296,"y":63},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":691,"y":147},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":887,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":891,"y":68},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=57,
            name='10',
            path='[{"coordinate":[0,0],"connectedNodes":[57]},{"coordinate":[8,2],"connectedNodes":[2,58]},{"coordinate":[8,3],"connectedNodes":[3,1]},{"coordinate":[7,3],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[6,1],"connectedNodes":[7,5]},{"coordinate":[5,1],"connectedNodes":[8,6]},{"coordinate":[4,1],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,14]},{"coordinate":[0,1],"connectedNodes":[17,15]},{"coordinate":[0,2],"connectedNodes":[18,16]},{"coordinate":[0,3],"connectedNodes":[19,17]},{"coordinate":[0,4],"connectedNodes":[20,18]},{"coordinate":[0,5],"connectedNodes":[21,19]},{"coordinate":[1,5],"connectedNodes":[20,22]},{"coordinate":[1,6],"connectedNodes":[23,21]},{"coordinate":[0,6],"connectedNodes":[24,22]},{"coordinate":[0,7],"connectedNodes":[25,23]},{"coordinate":[1,7],"connectedNodes":[24,26]},{"coordinate":[2,7],"connectedNodes":[25,27]},{"coordinate":[3,7],"connectedNodes":[26,28]},{"coordinate":[3,6],"connectedNodes":[27,29]},{"coordinate":[4,6],"connectedNodes":[28,30]},{"coordinate":[5,6],"connectedNodes":[29,31]},{"coordinate":[5,5],"connectedNodes":[32,30]},{"coordinate":[4,5],"connectedNodes":[33,31]},{"coordinate":[3,5],"connectedNodes":[34,32]},{"coordinate":[2,5],"connectedNodes":[33,35]},{"coordinate":[2,4],"connectedNodes":[34,36]},{"coordinate":[3,4],"connectedNodes":[35,37]},{"coordinate":[4,4],"connectedNodes":[36,38]},{"coordinate":[5,4],"connectedNodes":[37,39]},{"coordinate":[6,4],"connectedNodes":[38,40]},{"coordinate":[7,4],"connectedNodes":[39,41]},{"coordinate":[8,4],"connectedNodes":[40,42]},{"coordinate":[8,5],"connectedNodes":[43,41]},{"coordinate":[8,6],"connectedNodes":[44,42]},{"coordinate":[7,6],"connectedNodes":[45,43]},{"coordinate":[6,6],"connectedNodes":[46,44]},{"coordinate":[6,7],"connectedNodes":[47,45]},{"coordinate":[7,7],"connectedNodes":[46,48]},{"coordinate":[8,7],"connectedNodes":[47,49]},{"coordinate":[9,7],"connectedNodes":[48]},{"coordinate":[8,0],"connectedNodes":[51,58]},{"coordinate":[7,0],"connectedNodes":[52,50]},{"coordinate":[6,0],"connectedNodes":[53,51]},{"coordinate":[5,0],"connectedNodes":[54,52]},{"coordinate":[4,0],"connectedNodes":[55,53]},{"coordinate":[3,0],"connectedNodes":[56,54]},{"coordinate":[2,0],"connectedNodes":[57,55]},{"coordinate":[1,0],"connectedNodes":[0,56]},{"coordinate":[8,1],"connectedNodes":[1,50]}]')
    level10.save()

    # add blocks
    Block = apps.get_model('game', 'Block')
    forwards = Block.objects.filter(type__in=["move_forward"])
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forward"])

    level1.blocks = forwards
    level1.next_level = level2
    level2.blocks = forwards
    level2.next_level = level3
    level3.blocks = Block.objects.filter(type__in=["move_forward", "turn_right"])
    level3.next_level = level4
    level4.blocks = episode_blocks
    level4.next_level = level5
    level5.blocks = episode_blocks
    level5.next_level = level6
    level6.blocks = episode_blocks
    level6.next_level = level7
    level7.blocks = episode_blocks
    level7.next_level = level8
    level8.blocks = episode_blocks
    level8.next_level = level9
    level9.blocks = episode_blocks
    level9.next_level = level10
    level10.blocks = episode_blocks
    for level in [level1, level2, level3, level4, level5, level6, \
            level7, level8, level9, level10]:
        level.save()

    Episode = apps.get_model('game', 'Episode')
    episode1 = Episode(name="Basic", first_level=level1)
    episode1.save()

    # episode 2

    level11 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":136,"y":260},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":192,"y":342},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":240,"y":255},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":292,"y":342},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":339,"y":256},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":240,"y":428},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=57,
            name="11",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ')
    level11.save()

    level12 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":348,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":341,"y":536},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":454,"y":667},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":454,"y":532},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":335,"y":403},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":455,"y":411},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":232,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":230,"y":558},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":239,"y":411},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":135,"y":674},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":128,"y":554},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":127,"y":463},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":140,"y":342},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":21,"y":557},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":20,"y":439},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":7,"y":352},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":34,"y":240},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":138,"y":250},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":242,"y":279},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":347,"y":274},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":449,"y":297},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":556,"y":677},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":551,"y":544},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":558,"y":427},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":557,"y":289},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":22,"y":683},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":559,"y":174},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":348,"y":169},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":235,"y":167},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":135,"y":146},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":18,"y":134},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":20,"y":29},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":131,"y":30},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":240,"y":36},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":349,"y":48},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":451,"y":44},' + \
                    '"url":"/static/game/image/bush.svg"},{"coordinate":{"x":559,"y":39},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":659,"y":46},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":667,"y":153},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":663,"y":271},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":660,"y":395},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":660,"y":525},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":657,"y":648},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":757,"y":651},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":756,"y":522},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":756,"y":398},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":759,"y":278},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":765,"y":129},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":759,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":873,"y":683},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":863,"y":567},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":869,"y":458},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":864,"y":340},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":862,"y":222},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":865,"y":124},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":866,"y":8},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":448,"y":192},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":490,"y":-61},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="12",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ')
    level12.save()

    # add blocks
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forward", "controls_repeat"])

    level11.blocks = episode_blocks
    level11.next_level = level12
    level12.blocks = episode_blocks
    level11.save()
    level12.save()

    episode2 = Episode(name="Loop", first_level=level11)
    episode2.save()

    # episode 3

    level13 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":96,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":257,"y":514},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":512},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":431},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=57,
            name="13",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]')
    level13.save()

    level14 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":96,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":257,"y":514},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":512},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":431},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":188},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":132,"y":118},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":261,"y":102},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":190,"y":33},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":75,"y":35},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":11},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="14",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] '
        )
    level14.save()

    # add blocks
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forward", "controls_whileUntil"])

    level13.blocks = episode_blocks
    level13.next_level = level14
    level14.blocks = episode_blocks
    level13.save()
    level14.save()

    episode3 = Episode(name="Repeat .. Until", first_level=level13)
    episode3.save()


    # episode 4

    level15 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":2,"y":101},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":100},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":203,"y":98},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":306,"y":101},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":403,"y":97},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="15",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ')
    level15.save()

    level16 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":101,"y":205},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":203},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":198,"y":99},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":302,"y":99},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":294,"y":-1},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":4},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":0,"y":601},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":104,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":4,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":899,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":798,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":897,"y":598},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":695,"y":693},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":597,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":498,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":400,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":299,"y":697},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="16",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]'
        )
    level16.save()

    # add blocks
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forward", \
            "controls_whileUntil", "logic_negate"])

    level15.blocks = episode_blocks
    level15.next_level = level16
    level16.blocks = episode_blocks
    level15.save()
    level16.save()

    episode4 = Episode(name="Repeat .. While", first_level=level15)
    episode4.save()

    # episode 5

    level17 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":454,"y":354},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":455,"y":249},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":555,"y":349},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":558,"y":249},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="17",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ')
    level17.save()

    level18 = Level(
            destination=[4, 6],
            decor='[{"coordinate":{"x":156,"y":344},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":252,"y":443},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":349,"y":543},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":49,"y":354},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":142,"y":458},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":239,"y":556},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":52,"y":249},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":338,"y":657},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":230,"y":659},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":157,"y":239},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="18",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ')
    level18.save()

    level19 = Level(
            destination=[5, 3],
            decor='[{"coordinate":{"x":350,"y":337},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":348,"y":439},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":344,"y":540},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":342,"y":645},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="19",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ')
    level19.save()

    level20 = Level(
            destination=[5, 3],
            decor='[{"coordinate":{"x":244,"y":339},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":246,"y":232},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":246,"y":127},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":669,"y":639},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":469,"y":597},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":596,"y":512},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="20",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}] ')
    level20.save()

    # add blocks
    episode_blocks = Block.objects.filter(
            type__in=["move_forwards", "turn_left", "turn_right", \
                    "controls_whileUntil", "controls_if", "logic_negate", \
                    "road_exists", "at_destination"])

    level17.blocks = episode_blocks
    level17.next_level = level18
    level18.blocks = episode_blocks
    level18.next_level = level19
    level19.blocks = episode_blocks
    level19.next_level = level20
    level20.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left", "turn_right", \
        "controls_whileUntil", "controls_if", "logic_negate", \
        "road_exists", "at_destination", "turn_around", "controls_repeat"])
    level17.save()
    level18.save()
    level19.save()
    level20.save()

    Episode = apps.get_model('game', 'Episode')
    episode5 = Episode(name="If ... only", first_level=level17)
    episode5.save()

    # episode 6

    level21 = Level(
            destination=[4, 3],
            decor='[{"coordinate":{"x":197,"y":202},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":196,"y":94},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="21",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3,5]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3]},{"coordinate":[3,3],"connectedNodes":[2,6]},{"coordinate":[4,3],"connectedNodes":[5]}]')
    level21.save()

    level22 = Level(
            destination=[3, 3],
            decor='[{"coordinate":{"x":152,"y":339},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":302,"y":505},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":403,"y":503},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":508,"y":512},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":3,"y":103},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":104,"y":101},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":207,"y":94},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":399,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":506,"y":3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":604,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":407,"y":605},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":503,"y":609},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":600,"y":599},"url":"/static/game/image/bush.svg"}]',
            default=True,
            max_fuel=50,
            name="22",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,4,2]},{"coordinate":[2,3],"connectedNodes":[1,3,5]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2]}]')
    level22.save()

    level23 = Level(
            destination=[5, 3],
            decor='[{"coordinate":{"x":99,"y":597},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":100,"y":495},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":117,"y":408},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":197},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":92,"y":107},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":1},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":607,"y":593},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":590,"y":493},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":513,"y":412},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":597,"y":3},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":697,"y":1},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":799,"y":0},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="23",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3,9]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[3,4],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,10,7]},{"coordinate":[4,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,9]},{"coordinate":[2,2],"connectedNodes":[2,8]},{"coordinate":[5,3],"connectedNodes":[6]}]'
            )
    level23.save()

    # add blocks
    episode_blocks = Block.objects.filter(
            type__in=["move_forwards", "turn_left", "turn_right", \
                    "controls_whileUntil", "controls_if", "logic_negate", \
                    "road_exists", "at_destination", "turn_around", \
                    "controls_repeat", "road_exists", "dead_end"])

    level21.blocks = episode_blocks
    level21.next_level = level22
    level22.blocks = episode_blocks
    level22.next_level = level23
    level23.blocks = episode_blocks
    level21.save()
    level22.save()
    level23.save()

    episode6 = Episode(name="Junction", first_level=level21)
    episode6.save()

    # episode 7

    level24 = Level(
            destination=[7, 7],
            decor='[{"coordinate":{"x":566,"y":175},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":838,"y":565},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":223,"y":56},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":121,"y":44},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":351,"y":546},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":547,"y":548},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":643,"y":654},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":251,"y":654},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":247,"y":436},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":48,"y":242},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":443,"y":656},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":443,"y":440},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":651,"y":438},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":653,"y":62},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":853,"y":244},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":848,"y":40},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="24",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2,20]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4,10]},{"coordinate":[0,5],"connectedNodes":[3,5]},{"coordinate":[0,6],"connectedNodes":[4,6]},{"coordinate":[0,7],"connectedNodes":[5,7]},{"coordinate":[1,7],"connectedNodes":[6,8]},{"coordinate":[2,7],"connectedNodes":[7,9]},{"coordinate":[2,6],"connectedNodes":[8,11,10]},{"coordinate":[2,5],"connectedNodes":[3,9]},{"coordinate":[3,6],"connectedNodes":[9,13]},{"coordinate":[4,7],"connectedNodes":[13]},{"coordinate":[4,6],"connectedNodes":[11,12,14]},{"coordinate":[4,5],"connectedNodes":[13,15]},{"coordinate":[4,4],"connectedNodes":[14,42,16]},{"coordinate":[3,4],"connectedNodes":[15,17]},{"coordinate":[3,3],"connectedNodes":[16,18]},{"coordinate":[3,2],"connectedNodes":[17,28,27,19]},{"coordinate":[2,2],"connectedNodes":[18,20]},{"coordinate":[1,2],"connectedNodes":[19,21,1]},{"coordinate":[0,2],"connectedNodes":[20,22]},{"coordinate":[0,1],"connectedNodes":[21,23]},{"coordinate":[0,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[2,0],"connectedNodes":[24,26]},{"coordinate":[3,0],"connectedNodes":[25,27]},{"coordinate":[3,1],"connectedNodes":[18,26]},{"coordinate":[4,2],"connectedNodes":[18,29]},{"coordinate":[5,2],"connectedNodes":[28,30]},{"coordinate":[5,1],"connectedNodes":[29,31]},{"coordinate":[5,0],"connectedNodes":[30,32]},{"coordinate":[6,0],"connectedNodes":[31,33]},{"coordinate":[6,1],"connectedNodes":[32,34]},{"coordinate":[6,2],"connectedNodes":[33,35]},{"coordinate":[6,3],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[38,37,35,42]},{"coordinate":[7,4],"connectedNodes":[36]},{"coordinate":[6,5],"connectedNodes":[36,39]},{"coordinate":[6,6],"connectedNodes":[38,41]},{"coordinate":[5,7],"connectedNodes":[41]},{"coordinate":[6,7],"connectedNodes":[39,40,43]},{"coordinate":[5,4],"connectedNodes":[15,36]},{"coordinate":[7,7],"connectedNodes":[41]}]')
    level24.save()

    level25 = Level(
            destination=[4, 2],
            decor='[{"coordinate":{"x":0,"y":595},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":2,"y":502},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":6,"y":398},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":5,"y":201},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":8,"y":104},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":5},"url":"/static/game/image/tree1.svg"}]',
            default=True,
            max_fuel=50,
            name="25",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[2,27,26,0]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[1,7],"connectedNodes":[4,6]},{"coordinate":[2,7],"connectedNodes":[5,7]},{"coordinate":[3,7],"connectedNodes":[6,8]},{"coordinate":[4,7],"connectedNodes":[7,9]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[6,7],"connectedNodes":[9,11]},{"coordinate":[7,7],"connectedNodes":[10,12]},{"coordinate":[7,6],"connectedNodes":[11,13]},{"coordinate":[7,5],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[13,15]},{"coordinate":[7,3],"connectedNodes":[14,16]},{"coordinate":[7,2],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[7,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[5,0],"connectedNodes":[19,21]},{"coordinate":[4,0],"connectedNodes":[20,22]},{"coordinate":[3,0],"connectedNodes":[21,23]},{"coordinate":[2,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[1,1],"connectedNodes":[24,26]},{"coordinate":[1,2],"connectedNodes":[25,1]},{"coordinate":[2,3],"connectedNodes":[28,45,44,1]},{"coordinate":[2,4],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[2,6],"connectedNodes":[29,31]},{"coordinate":[3,6],"connectedNodes":[30,32]},{"coordinate":[4,6],"connectedNodes":[31,33]},{"coordinate":[5,6],"connectedNodes":[32,34]},{"coordinate":[6,6],"connectedNodes":[33,35]},{"coordinate":[6,5],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[35,37]},{"coordinate":[6,3],"connectedNodes":[36,38]},{"coordinate":[6,2],"connectedNodes":[37,39]},{"coordinate":[6,1],"connectedNodes":[38,40]},{"coordinate":[5,1],"connectedNodes":[39,41]},{"coordinate":[4,1],"connectedNodes":[40,42]},{"coordinate":[3,1],"connectedNodes":[41,43]},{"coordinate":[2,1],"connectedNodes":[42,44]},{"coordinate":[2,2],"connectedNodes":[43,27]},{"coordinate":[3,3],"connectedNodes":[46,54,53,27]},{"coordinate":[3,4],"connectedNodes":[45,47]},{"coordinate":[3,5],"connectedNodes":[46,48]},{"coordinate":[4,5],"connectedNodes":[47,49]},{"coordinate":[5,5],"connectedNodes":[48,50]},{"coordinate":[5,4],"connectedNodes":[49,51]},{"coordinate":[5,3],"connectedNodes":[50,52]},{"coordinate":[5,2],"connectedNodes":[51,56]},{"coordinate":[3,2],"connectedNodes":[45,56]},{"coordinate":[4,3],"connectedNodes":[45,55]},{"coordinate":[4,4],"connectedNodes":[54]},{"coordinate":[4,2],"connectedNodes":[52,53]}]')
    level25.save()

    level26 = Level(
            destination=[6, 4],
            decor='[{"coordinate":{"x":0,"y":595},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":2,"y":502},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":6,"y":398},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":5,"y":201},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":8,"y":104},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":5},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":193,"y":702},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":403,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":598,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":799,"y":694},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="26",
            path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[2,27,26,0]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[1,7],"connectedNodes":[4,6]},{"coordinate":[2,7],"connectedNodes":[5,7]},{"coordinate":[3,7],"connectedNodes":[6,8]},{"coordinate":[4,7],"connectedNodes":[7,9]},{"coordinate":[5,7],"connectedNodes":[8,10]},{"coordinate":[6,7],"connectedNodes":[9,11]},{"coordinate":[7,7],"connectedNodes":[10,12]},{"coordinate":[7,6],"connectedNodes":[11,13]},{"coordinate":[7,5],"connectedNodes":[12,14]},{"coordinate":[7,4],"connectedNodes":[13,15]},{"coordinate":[7,3],"connectedNodes":[14,16]},{"coordinate":[7,2],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[7,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[5,0],"connectedNodes":[19,21]},{"coordinate":[4,0],"connectedNodes":[20,22]},{"coordinate":[3,0],"connectedNodes":[21,23]},{"coordinate":[2,0],"connectedNodes":[22,24]},{"coordinate":[1,0],"connectedNodes":[23,25]},{"coordinate":[1,1],"connectedNodes":[24,26]},{"coordinate":[1,2],"connectedNodes":[25,1]},{"coordinate":[2,3],"connectedNodes":[28,45,44,1]},{"coordinate":[2,4],"connectedNodes":[27,29]},{"coordinate":[2,5],"connectedNodes":[28,30]},{"coordinate":[2,6],"connectedNodes":[29,31]},{"coordinate":[3,6],"connectedNodes":[30,32]},{"coordinate":[4,6],"connectedNodes":[31,33]},{"coordinate":[5,6],"connectedNodes":[32,34]},{"coordinate":[6,6],"connectedNodes":[33,35]},{"coordinate":[6,5],"connectedNodes":[34,36]},{"coordinate":[6,4],"connectedNodes":[35,37]},{"coordinate":[6,3],"connectedNodes":[36,38]},{"coordinate":[6,2],"connectedNodes":[37,39]},{"coordinate":[6,1],"connectedNodes":[38,40]},{"coordinate":[5,1],"connectedNodes":[39,41]},{"coordinate":[4,1],"connectedNodes":[40,42]},{"coordinate":[3,1],"connectedNodes":[41,43]},{"coordinate":[2,1],"connectedNodes":[42,44]},{"coordinate":[2,2],"connectedNodes":[43,27]},{"coordinate":[3,3],"connectedNodes":[46,54,53,27]},{"coordinate":[3,4],"connectedNodes":[45,47]},{"coordinate":[3,5],"connectedNodes":[46,48]},{"coordinate":[4,5],"connectedNodes":[47,49]},{"coordinate":[5,5],"connectedNodes":[48,50]},{"coordinate":[5,4],"connectedNodes":[49,51]},{"coordinate":[5,3],"connectedNodes":[50,52]},{"coordinate":[5,2],"connectedNodes":[51,56]},{"coordinate":[3,2],"connectedNodes":[45,56]},{"coordinate":[4,3],"connectedNodes":[45,55]},{"coordinate":[4,4],"connectedNodes":[54]},{"coordinate":[4,2],"connectedNodes":[52,53]}]')
    level26.save()

    # add blocks
    episode_blocks = Block.objects.filter(
            type__in=["move_forwards", "turn_left", "turn_right", \
                    "controls_whileUntil", "controls_if", "logic_negate", \
                    "road_exists", "at_destination"])

    level24.blocks = episode_blocks
    level24.next_level = level25
    level25.blocks = episode_blocks
    level25.next_level = level26
    level26.blocks = episode_blocks
    level24.save()
    level25.save()
    level26.save()

    Episode = apps.get_model('game', 'Episode')
    episode7 = Episode(name="The rest ...", first_level=level24)
    episode7.save()

    episode1.next_episode = episode2
    episode2.next_episode = episode3
    episode3.next_episode = episode4
    episode4.next_episode = episode5
    episode5.next_episode = episode6
    episode6.next_episode = episode7

    for episode in [episode1, episode2, episode3, episode4, episode5, episode6, episode7]:
        episode.save()


class Migration(migrations.Migration):

    dependencies = [
            ('game', '0002_blocks'),
    ]

    operations = [
            migrations.RunPython(levels),
    ]
