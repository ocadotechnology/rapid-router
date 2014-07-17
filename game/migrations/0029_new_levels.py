# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def drop_and_add_new(apps, schema_editor):

    Level = apps.get_model('game', 'Level')
    Block = apps.get_model('game', 'Block')

    Level.objects.all().delete()


def levels(Level, Block):

    ##### Basic episode

    level1 = Level(name=1, default=1, destination=[2, 3],
                   decor='[{"coordinate":{"x":100,"y":100}, "url": "/static/game/image/tree1.svg"}]',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1]}] ')

    level2 = Level(name=2, default=1, destination=[4, 3],
                   decor='[{"coordinate":{"x":67,"y":570},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":663,"y":443},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":192,"y":58},"url":"/static/game/image/bush.svg"}]',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]')

    level3 = Level(name=3, default=1, destination=[2, 2],
                   decor='[{"coordinate":{"x":0,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":404},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":601,"y":403},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":402},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":804,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":903,"y":401},"url":"/static/game/image/tree2.svg"}]',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[2,2],"connectedNodes":[2]}]')

    level4 = Level(name=4, default=1, destination=[4, 5], model_solution=5,
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[5]}]',
                   decor='[{"coordinate":{"x":531,"y":624},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":442,"y":632},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":531,"y":498},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":495,"y":564},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":584,"y":565},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":615,"y":630},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":669,"y":565},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":621,"y":497},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":500,"y":694},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":633},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":380,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":365,"y":596},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":287,"y":713},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":596,"y":714},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":711,"y":704},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":813,"y":702},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":906,"y":700},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":897,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":807,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":719,"y":636},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":857,"y":659},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":766,"y":701},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":665,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":851,"y":568},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":766,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":155,"y":680},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":216,"y":541},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":530,"y":402},"url":"/static/game/image/tree1.svg"}]')

    level5 = Level(name=5, default=1, destination=[4, 6],
                   decor='[{"coordinate":{"x":138,"y":457},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":344},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":237,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":259,"y":441},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":355,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":45,"y":363},"url":"/static/game/image/tree1.svg"}]',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}]')

    level6 = Level(name=6, default=1, destination=[6, 1], model_solution=10,
                   path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                   decor='[{"coordinate":{"x":224,"y":654},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":87,"y":656},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":591},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":163,"y":562},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":153,"y":624},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":608,"y":480},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":584,"y":366},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":591,"y":220},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":676,"y":254},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":689,"y":351},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":673,"y":509},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":557,"y":574},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":201},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":102,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":103},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":147,"y":197},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":240,"y":127},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":154,"y":121},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":262,"y":215},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":328,"y":155},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":147,"y":715},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":65,"y":144},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":78,"y":220},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":262,"y":70},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":371,"y":85},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":64,"y":63},"url":"/static/game/image/tree2.svg"}]')

    level7 = Level(name=7, default=1, destination=[5, 3],
                   decor='[{"coordinate":{"x":479,"y":551},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":404,"y":446},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":363,"y":354},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":428,"y":124},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":212,"y":130},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":398,"y":590},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":261,"y":670},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":232,"y":428},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":25,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":230,"y":333},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":227,"y":236},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":133},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-21,"y":-11},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":633,"y":16},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":688,"y":601},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":634,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":827,"y":616},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":751,"y":450},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":833,"y":47},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":842,"y":374},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":703,"y":237},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":535,"y":353},"url":"/static/game/image/tree2.svg"}]',
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,6],"connectedNodes":[3,5]},{"coordinate":[2,6],"connectedNodes":[4,6]},{"coordinate":[2,5],"connectedNodes":[5,7]},{"coordinate":[3,5],"connectedNodes":[6,8]},{"coordinate":[3,4],"connectedNodes":[7,9]},{"coordinate":[3,3],"connectedNodes":[8,10]},{"coordinate":[3,2],"connectedNodes":[9,11]},{"coordinate":[4,2],"connectedNodes":[10,12]},{"coordinate":[4,3],"connectedNodes":[11,13]},{"coordinate":[5,3],"connectedNodes":[12]}]')

    level8 = Level(name=8, default=1, destination=[4, 1],
                   decor='[{"coordinate":{"x":271,"y":406},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y": 392},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":63,"y":397},"url":"/static/game/image/tree1.svg" },{"coordinate":{"x":114,"y":478},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":697,"y":198},"url": "/static/game/image/tree2.svg"},{"coordinate":{"x":532,"y":76},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":705,"y":44},"url":"/static/game/image/tree2.svg"}]',
                   path='[{"coordinate":[4,6],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[0,2]},{"coordinate":[4,4],"connectedNodes":[1,3]},{"coordinate":[4,3],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,1],"connectedNodes":[4]}]')

    level9 = Level(name=9, default=1, destination=[8, 1],
                   decor='[{"coordinate":{"x":167,"y":207},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":263,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":364,"y":202},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":571,"y":203},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":465,"y":199},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":29,"y":433},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":505,"y":652},"url":"/static/game/image/bush.svg"}]',
                   path='[{"coordinate":[6,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[2,0]},{"coordinate":[4,3],"connectedNodes":[3,1]},{"coordinate":[3,3],"connectedNodes":[4,2]},{"coordinate":[2,3],"connectedNodes":[5,3]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[1,1],"connectedNodes":[6,8]},{"coordinate":[2,1],"connectedNodes":[7,9]},{"coordinate":[3,1],"connectedNodes":[8,10]},{"coordinate":[4,1],"connectedNodes":[9,11]},{"coordinate":[5,1],"connectedNodes":[10,12]},{"coordinate":[6,1],"connectedNodes":[11,13]},{"coordinate":[7,1],"connectedNodes":[12,14]},{"coordinate":[8,1],"connectedNodes":[13]}]')

    level10 = Level(name=10, default=1, destination=[3, 3], model_solution=7,
                    path='[{"coordinate":[5,5],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[3,5]},{"coordinate":[2,5],"connectedNodes":[4,6]},{"coordinate":[2,4],"connectedNodes":[5,7]},{"coordinate":[2,3],"connectedNodes":[6,8]},{"coordinate":[3,3],"connectedNodes":[7]}]',
                    decor='[{"coordinate":{"x":99,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":54,"y":634},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":143,"y":632},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-5,"y":703},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":298,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":94,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":504,"y":389},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-13,"y":584},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":17,"y":503},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":484,"y":604},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":582,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":599,"y":413},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":606,"y":501},"url":"/static/game/image/bush.svg"}]')

    level11 = Level(name=11, default=1, destination=[1, 3], model_solution=12,
                    path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[2,0]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]}]',
                    decor='[{"coordinate":{"x":396,"y":304},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":302},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":242,"y":301},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":601,"y":434},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":599,"y":701},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":598,"y":580},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":116,"y":701},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":236,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":359,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":480,"y":698},"url":"/static/game/image/tree2.svg"}]')

    level12 = Level(name=12, default=1, destination=[1, 3], model_solution=17,
                    path='[{"coordinate":[5,7],"connectedNodes":[17]},{"coordinate":[2,6],"connectedNodes":[18,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[2,4],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]},{"coordinate":[1,7],"connectedNodes":[15,18]},{"coordinate":[2,7],"connectedNodes":[14,16]},{"coordinate":[3,7],"connectedNodes":[15,17]},{"coordinate":[4,7],"connectedNodes":[16,0]},{"coordinate":[1,6],"connectedNodes":[14,1]}]',
                    decor='[{"coordinate":{"x":331,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":267,"y":489},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":284,"y":561},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":402,"y":479},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":452,"y":532},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":418,"y":583},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":376,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":356,"y":606},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":86},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-15,"y":-11},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":279,"y":-20},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":202,"y":4},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":73,"y":109},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":84},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":18},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":119,"y":2},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":381,"y":-14},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":323,"y":40},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":565,"y":81},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":493,"y":148},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":445,"y":-23},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":417,"y":72},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":549,"y":7},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":265,"y":120},"url":"/static/game/image/tree2.svg"}]')
    
    level1.save()
    level2.save()
    level3.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()

    level1.next_level = level2
    level2.next_level = level3
    level3.next_level = level4
    level4.next_level = level5
    level5.next_level = level6
    level6.next_level = level7
    level7.next_level = level8
    level8.next_level = level9
    level9.next_level = level10
    level10.next_level = level11
    level11.next_level = level12

    forwards = Block.objects.filter(type__in=["move_forwards"])
    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level1.blocks = forwards
    level2.blocks = forwards
    level3.blocks = Block.objects.filter(type__in=["move_forwards", "turn_right"])
    level4.blocks = Block.objects.filter(type__in=["move_forwards", "turn_left"])
    level5.blocks = blocks
    level6.blocks = blocks
    level7.blocks = blocks
    level9.blocks = blocks
    level10.blocks = blocks
    level11.blocks = blocks
    level12.blocks = blocks

    level1.save()
    level2.save()
    level3.save()
    level3.save()
    level4.save()
    level5.save()
    level6.save()
    level7.save()
    level8.save()
    level9.save()
    level10.save()
    level11.save()
    level12.save()

    ##### Shortest path episode

    level13 = Level(name=13, default=1, destination=[0, 1], model_solution=11,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    decor='[{"coordinate":{"x":48,"y":658},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":49,"y":553},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":446},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":50,"y":340},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":406,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":496,"y":492},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":500,"y":302},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":245},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":193},"url":"/static/game/image/bush.svg"}]')

    level14 = Level(name=14, default=1, destination=[2, 5], model_solution=7,
                    path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                    decor='[{"coordinate":{"x":209,"y":392},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":307,"y":302},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":281,"y":187},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":498,"y":197},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":771,"y":662},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":866,"y":557},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":754,"y":491},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":890,"y":310},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":725,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":780,"y":87},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":862,"y":177},"url":"/static/game/image/tree1.svg"}]')
    level15 = Level(name=15, default=1, destination=[7, 2], model_solution=11,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,4,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[9,2]},{"coordinate":[3,6],"connectedNodes":[1,5]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[6,8]},{"coordinate":[5,6],"connectedNodes":[7,13]},{"coordinate":[0,5],"connectedNodes":[3,10]},{"coordinate":[0,4],"connectedNodes":[9,11]},{"coordinate":[1,4],"connectedNodes":[10,12]},{"coordinate":[2,4],"connectedNodes":[11,15]},{"coordinate":[5,5],"connectedNodes":[8,14]},{"coordinate":[5,4],"connectedNodes":[16,13,17]},{"coordinate":[3,4],"connectedNodes":[12,16]},{"coordinate":[4,4],"connectedNodes":[15,14,21]},{"coordinate":[5,3],"connectedNodes":[21,14,18]},{"coordinate":[5,2],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[7,2],"connectedNodes":[19]},{"coordinate":[4,3],"connectedNodes":[16,17]}]',
                    decor='[{"coordinate":{"x":406,"y":205},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":296},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":98,"y":661},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":592},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":15,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":46,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":579,"y":501},"url":"/static/game/image/bush.svg"}]')

    level16 = Level(name=16, default=1, destination=[7, 0], model_solution=13,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[2,0,11]},{"coordinate":[1,6],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,29,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,27,17]},{"coordinate":[2,5],"connectedNodes":[1,12]},{"coordinate":[3,5],"connectedNodes":[11,13]},{"coordinate":[3,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[13,15]},{"coordinate":[4,5],"connectedNodes":[14,21,16]},{"coordinate":[4,4],"connectedNodes":[28,15]},{"coordinate":[5,1],"connectedNodes":[10,18]},{"coordinate":[5,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[7,0],"connectedNodes":[19]},{"coordinate":[5,5],"connectedNodes":[15,22]},{"coordinate":[6,5],"connectedNodes":[21,23]},{"coordinate":[7,5],"connectedNodes":[22,24]},{"coordinate":[7,4],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[24,26]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[6,2],"connectedNodes":[10,26]},{"coordinate":[3,4],"connectedNodes":[16,29]},{"coordinate":[3,3],"connectedNodes":[28,8]}]',
                    decor='[{"coordinate":{"x":188,"y":399},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":587,"y":97},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":652,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":751,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":787,"y":627},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":687,"y":623},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":924,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":922,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":843,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":956,"y":517},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":544,"y":675},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":791,"y":504},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":926,"y":425},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":859,"y":563},"url":"/static/game/image/tree2.svg"}] ')

    level17 = Level(name=17, default=1, destination=[4, 1], model_solution=12,
                    path='[{"coordinate":[2,6],"connectedNodes":[30]},{"coordinate":[3,6],"connectedNodes":[2,28]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[5,6],"connectedNodes":[2,6,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[10,4]},{"coordinate":[6,6],"connectedNodes":[3,7]},{"coordinate":[7,6],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,16]},{"coordinate":[4,4],"connectedNodes":[5,26]},{"coordinate":[1,2],"connectedNodes":[29,19]},{"coordinate":[2,3],"connectedNodes":[29,13]},{"coordinate":[3,3],"connectedNodes":[12,26]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[6,3],"connectedNodes":[14,16]},{"coordinate":[7,3],"connectedNodes":[15,9,25]},{"coordinate":[5,2],"connectedNodes":[27,14,18]},{"coordinate":[5,1],"connectedNodes":[22,17,23]},{"coordinate":[1,1],"connectedNodes":[11,20]},{"coordinate":[2,1],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,18]},{"coordinate":[6,1],"connectedNodes":[18,24]},{"coordinate":[7,1],"connectedNodes":[23,25]},{"coordinate":[7,2],"connectedNodes":[16,24]},{"coordinate":[4,3],"connectedNodes":[13,10,27]},{"coordinate":[4,2],"connectedNodes":[26,17]},{"coordinate":[3,5],"connectedNodes":[30,1]},{"coordinate":[1,3],"connectedNodes":[12,11]},{"coordinate":[2,5],"connectedNodes":[0,28]}]',
                    decor='[{"coordinate":{"x":573,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":674},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":673},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":380,"y":523},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":580,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":196,"y":190},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":402},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-2,"y":532},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-3,"y":224},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-2,"y":68},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":1,"y":674},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":170,"y":403},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":308,"y":190},"url":"/static/game/image/tree1.svg"}]')

    level18 = Level(name=18, default=1, destination=[2, 7], model_solution=15,
                    path='[{"coordinate":[6,1],"connectedNodes":[4]},{"coordinate":[3,0],"connectedNodes":[49,2]},{"coordinate":[4,0],"connectedNodes":[1,3]},{"coordinate":[5,0],"connectedNodes":[2,4]},{"coordinate":[6,0],"connectedNodes":[3,0,5]},{"coordinate":[7,0],"connectedNodes":[4,6]},{"coordinate":[8,0],"connectedNodes":[5,11]},{"coordinate":[1,0],"connectedNodes":[8,49]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8,10]},{"coordinate":[3,1],"connectedNodes":[9,38]},{"coordinate":[8,1],"connectedNodes":[12,6]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[43,18,16,42]},{"coordinate":[7,7],"connectedNodes":[19,17]},{"coordinate":[6,7],"connectedNodes":[20,18]},{"coordinate":[5,7],"connectedNodes":[21,19]},{"coordinate":[4,7],"connectedNodes":[22,20]},{"coordinate":[3,7],"connectedNodes":[30,21]},{"coordinate":[2,6],"connectedNodes":[24,30,48,29]},{"coordinate":[1,6],"connectedNodes":[25,23]},{"coordinate":[0,6],"connectedNodes":[24,26]},{"coordinate":[0,5],"connectedNodes":[25,27]},{"coordinate":[0,4],"connectedNodes":[26,31]},{"coordinate":[2,4],"connectedNodes":[29,34,33]},{"coordinate":[2,5],"connectedNodes":[23,28]},{"coordinate":[2,7],"connectedNodes":[22,23]},{"coordinate":[0,3],"connectedNodes":[27,32]},{"coordinate":[1,3],"connectedNodes":[31,33]},{"coordinate":[2,3],"connectedNodes":[32,28]},{"coordinate":[3,4],"connectedNodes":[28,35]},{"coordinate":[4,4],"connectedNodes":[34,39,36]},{"coordinate":[4,3],"connectedNodes":[35,37]},{"coordinate":[4,2],"connectedNodes":[36,38]},{"coordinate":[4,1],"connectedNodes":[10,37]},{"coordinate":[5,4],"connectedNodes":[35,40]},{"coordinate":[6,4],"connectedNodes":[39,41]},{"coordinate":[7,4],"connectedNodes":[40,42]},{"coordinate":[7,5],"connectedNodes":[17,41]},{"coordinate":[6,6],"connectedNodes":[44,17]},{"coordinate":[5,6],"connectedNodes":[43,45]},{"coordinate":[5,5],"connectedNodes":[46,44]},{"coordinate":[4,5],"connectedNodes":[47,45]},{"coordinate":[4,6],"connectedNodes":[48,46]},{"coordinate":[3,6],"connectedNodes":[23,47]},{"coordinate":[2,0],"connectedNodes":[7,1]}]',
                    decor='[{"coordinate":{"x":875,"y":86},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":874,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":775,"y":688},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":119,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":289},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":487,"y":203},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":231,"y":189},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":73,"y":172},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":604,"y":300},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":672,"y":194},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":516,"y":286},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":587,"y":211},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":283},"url":"/static/game/image/tree2.svg"}]')

    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()

    level13.next_level = level14
    level14.next_level = level15
    level15.next_level = level16
    level16.next_level = level17
    level17.next_level = level18

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level13.blocks = blocks
    level14.blocks = blocks
    level15.blocks = blocks
    level16.blocks = blocks
    level17.blocks = blocks
    level18.blocks = blocks

    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()

    ##### Simple repeat

    level19 = Level(name=11, default=1, destination=[4, 3],
                    decor='[{"coordinate":{"x":136,"y":260},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":192,"y":342},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":240,"y":255},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":292,"y":342},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":339,"y":256},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":240,"y":428},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}] ')

    level20 = Level(name=12, default=1, destination=[4, 6],
                    decor='[{"coordinate":{"x":348,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":341,"y":536},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":454,"y":667},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":454,"y":532},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":335,"y":403},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":455,"y":411},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":232,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":230,"y":558},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":239,"y":411},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":135,"y":674},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":128,"y":554},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":127,"y":463},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":140,"y":342},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":21,"y":557},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":20,"y":439},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":7,"y":352},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":34,"y":240},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":138,"y":250},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":242,"y":279},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":347,"y":274},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":449,"y":297},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":556,"y":677},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":551,"y":544},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":558,"y":427},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":557,"y":289},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":22,"y":683},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":559,"y":174},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":348,"y":169},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":235,"y":167},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":135,"y":146},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":18,"y":134},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":20,"y":29},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":131,"y":30},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":240,"y":36},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":349,"y":48},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":451,"y":44},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":559,"y":39},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":659,"y":46},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":667,"y":153},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":663,"y":271},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":660,"y":395},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":660,"y":525},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":657,"y":648},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":757,"y":651},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":756,"y":522},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":756,"y":398},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":759,"y":278},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":765,"y":129},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":759,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":873,"y":683},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":863,"y":567},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":869,"y":458},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":864,"y":340},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":862,"y":222},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":865,"y":124},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":866,"y":8},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":448,"y":192},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":490,"y":-61},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ')

    level21 = Level(name=21, default=1, destination=[3, 7],
                    decor='[{"coordinate":{"x":300,"y":610},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":294,"y":412},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":525},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":389,"y":515},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":162,"y":688},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":610},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":513},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":26,"y":19},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":148,"y":5},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":216,"y":80},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":-29},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":707,"y":2},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":638,"y":91},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":697,"y":186},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":439,"y":113},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":401,"y":-30},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":302,"y":18},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":89,"y":113},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":516,"y":47},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[1,6],"connectedNodes":[2]},{"coordinate":[1,4],"connectedNodes":[2,3]},{"coordinate":[1,5],"connectedNodes":[0,1]},{"coordinate":[2,4],"connectedNodes":[1,4]},{"coordinate":[2,3],"connectedNodes":[3,5]},{"coordinate":[3,3],"connectedNodes":[4,6]},{"coordinate":[4,3],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[8,6]},{"coordinate":[5,4],"connectedNodes":[7,9]},{"coordinate":[5,5],"connectedNodes":[10,8]},{"coordinate":[5,6],"connectedNodes":[11,9]},{"coordinate":[4,6],"connectedNodes":[12,10]},{"coordinate":[4,7],"connectedNodes":[13,11]},{"coordinate":[3,7],"connectedNodes":[12]}]')

    level22 = Level(name=8, default=1, destination=[7, 3],
                    decor='[{"coordinate":{"x":596,"y":585},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":233,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":248,"y":32},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":709,"y":20},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":106,"y":603},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":99,"y":490},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":597,"y":352},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[9,5],"connectedNodes":[1]},{"coordinate":[8,5],"connectedNodes":[2,0]},{"coordinate":[7,5],"connectedNodes":[3,1]},{"coordinate":[7,6],"connectedNodes":[4,2]},{"coordinate":[7,7],"connectedNodes":[5,3]},{"coordinate":[6,7],"connectedNodes":[6,4]},{"coordinate":[5,7],"connectedNodes":[5,7]},{"coordinate":[5,6],"connectedNodes":[6,8]},{"coordinate":[5,5],"connectedNodes":[7,9]},{"coordinate":[5,4],"connectedNodes":[8,10]},{"coordinate":[5,3],"connectedNodes":[11,9]},{"coordinate":[4,3],"connectedNodes":[12,10]},{"coordinate":[3,3],"connectedNodes":[13,11]},{"coordinate":[3,4],"connectedNodes":[14,12]},{"coordinate":[3,5],"connectedNodes":[15,13]},{"coordinate":[2,5],"connectedNodes":[14,16]},{"coordinate":[2,4],"connectedNodes":[17,15]},{"coordinate":[1,4],"connectedNodes":[18,16]},{"coordinate":[0,4],"connectedNodes":[17,19]},{"coordinate":[0,3],"connectedNodes":[18,20]},{"coordinate":[0,2],"connectedNodes":[19,21]},{"coordinate":[0,1],"connectedNodes":[20,22]},{"coordinate":[1,1],"connectedNodes":[21,23]},{"coordinate":[2,1],"connectedNodes":[22,24]},{"coordinate":[3,1],"connectedNodes":[23,25]},{"coordinate":[4,1],"connectedNodes":[24,26]},{"coordinate":[5,1],"connectedNodes":[25,27]},{"coordinate":[6,1],"connectedNodes":[26,28]},{"coordinate":[7,1],"connectedNodes":[27,29]},{"coordinate":[7,2],"connectedNodes":[30,28]},{"coordinate":[7,3],"connectedNodes":[29]}]')

    level23 = Level(name=9, default=1, destination=[0, 4],
                    decor='[{"coordinate":{"x":499,"y":398},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":293,"y":409},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":300,"y":606},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":407,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":507,"y":603},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":304,"y":200},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":408,"y":198},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":509,"y":208},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":506,"y":-3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":402,"y":8},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":295,"y":11},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[4,3],"connectedNodes":[1]},{"coordinate":[5,3],"connectedNodes":[0,2]},{"coordinate":[6,3],"connectedNodes":[1,3]},{"coordinate":[6,4],"connectedNodes":[4,2]},{"coordinate":[6,5],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[7,5]},{"coordinate":[3,5],"connectedNodes":[8,6]},{"coordinate":[2,5],"connectedNodes":[7,9]},{"coordinate":[2,4],"connectedNodes":[8,10]},{"coordinate":[2,3],"connectedNodes":[9,11]},{"coordinate":[2,2],"connectedNodes":[10,12]},{"coordinate":[2,1],"connectedNodes":[11,13]},{"coordinate":[3,1],"connectedNodes":[12,14]},{"coordinate":[4,1],"connectedNodes":[13,15]},{"coordinate":[5,1],"connectedNodes":[14,16]},{"coordinate":[6,1],"connectedNodes":[15,17]},{"coordinate":[7,1],"connectedNodes":[16,18]},{"coordinate":[8,1],"connectedNodes":[17,19]},{"coordinate":[8,2],"connectedNodes":[20,18]},{"coordinate":[8,3],"connectedNodes":[21,19]},{"coordinate":[8,4],"connectedNodes":[22,20]},{"coordinate":[8,5],"connectedNodes":[23,21]},{"coordinate":[8,6],"connectedNodes":[24,22]},{"coordinate":[8,7],"connectedNodes":[25,23]},{"coordinate":[7,7],"connectedNodes":[26,24]},{"coordinate":[6,7],"connectedNodes":[27,25]},{"coordinate":[5,7],"connectedNodes":[28,26]},{"coordinate":[4,7],"connectedNodes":[29,27]},{"coordinate":[3,7],"connectedNodes":[30,28]},{"coordinate":[2,7],"connectedNodes":[31,29]},{"coordinate":[1,7],"connectedNodes":[30,32]},{"coordinate":[1,6],"connectedNodes":[31,33]},{"coordinate":[1,5],"connectedNodes":[32,34]},{"coordinate":[1,4],"connectedNodes":[35,33]},{"coordinate":[0,4],"connectedNodes":[34]}]')

    level24 = Level(name=10, default=1, destination=[9, 7],
                    decor='[{"coordinate":{"x":195,"y":619},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":108,"y":356},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":399,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":515,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":595,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":700,"y":510},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":496,"y":306},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":296,"y":63},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":691,"y":147},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":887,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":891,"y":68},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[0,0],"connectedNodes":[57]},{"coordinate":[8,2],"connectedNodes":[2,58]},{"coordinate":[8,3],"connectedNodes":[3,1]},{"coordinate":[7,3],"connectedNodes":[4,2]},{"coordinate":[6,3],"connectedNodes":[3,5]},{"coordinate":[6,2],"connectedNodes":[4,6]},{"coordinate":[6,1],"connectedNodes":[7,5]},{"coordinate":[5,1],"connectedNodes":[8,6]},{"coordinate":[4,1],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[4,3],"connectedNodes":[11,9]},{"coordinate":[3,3],"connectedNodes":[12,10]},{"coordinate":[2,3],"connectedNodes":[11,13]},{"coordinate":[2,2],"connectedNodes":[12,14]},{"coordinate":[2,1],"connectedNodes":[15,13]},{"coordinate":[1,1],"connectedNodes":[16,14]},{"coordinate":[0,1],"connectedNodes":[17,15]},{"coordinate":[0,2],"connectedNodes":[18,16]},{"coordinate":[0,3],"connectedNodes":[19,17]},{"coordinate":[0,4],"connectedNodes":[20,18]},{"coordinate":[0,5],"connectedNodes":[21,19]},{"coordinate":[1,5],"connectedNodes":[20,22]},{"coordinate":[1,6],"connectedNodes":[23,21]},{"coordinate":[0,6],"connectedNodes":[24,22]},{"coordinate":[0,7],"connectedNodes":[25,23]},{"coordinate":[1,7],"connectedNodes":[24,26]},{"coordinate":[2,7],"connectedNodes":[25,27]},{"coordinate":[3,7],"connectedNodes":[26,28]},{"coordinate":[3,6],"connectedNodes":[27,29]},{"coordinate":[4,6],"connectedNodes":[28,30]},{"coordinate":[5,6],"connectedNodes":[29,31]},{"coordinate":[5,5],"connectedNodes":[32,30]},{"coordinate":[4,5],"connectedNodes":[33,31]},{"coordinate":[3,5],"connectedNodes":[34,32]},{"coordinate":[2,5],"connectedNodes":[33,35]},{"coordinate":[2,4],"connectedNodes":[34,36]},{"coordinate":[3,4],"connectedNodes":[35,37]},{"coordinate":[4,4],"connectedNodes":[36,38]},{"coordinate":[5,4],"connectedNodes":[37,39]},{"coordinate":[6,4],"connectedNodes":[38,40]},{"coordinate":[7,4],"connectedNodes":[39,41]},{"coordinate":[8,4],"connectedNodes":[40,42]},{"coordinate":[8,5],"connectedNodes":[43,41]},{"coordinate":[8,6],"connectedNodes":[44,42]},{"coordinate":[7,6],"connectedNodes":[45,43]},{"coordinate":[6,6],"connectedNodes":[46,44]},{"coordinate":[6,7],"connectedNodes":[47,45]},{"coordinate":[7,7],"connectedNodes":[46,48]},{"coordinate":[8,7],"connectedNodes":[47,49]},{"coordinate":[9,7],"connectedNodes":[48]},{"coordinate":[8,0],"connectedNodes":[51,58]},{"coordinate":[7,0],"connectedNodes":[52,50]},{"coordinate":[6,0],"connectedNodes":[53,51]},{"coordinate":[5,0],"connectedNodes":[54,52]},{"coordinate":[4,0],"connectedNodes":[55,53]},{"coordinate":[3,0],"connectedNodes":[56,54]},{"coordinate":[2,0],"connectedNodes":[57,55]},{"coordinate":[1,0],"connectedNodes":[0,56]},{"coordinate":[8,1],"connectedNodes":[1,50]}]')

    level25 = Level(name=25, default=1, destination=[8, 2],
                    decor='[{"coordinate":{"x":295,"y":589},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":403,"y":489},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":207,"y":399},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":108,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":596,"y":391},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":401,"y":301},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":497,"y":205},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":294},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":6,"y":110},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":109,"y":-2},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":4,"y":6},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":222,"y":-6},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":230},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":885,"y":687},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":651,"y":689},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":767,"y":693},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":885,"y":575},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":887,"y":463},"url":"/static/game/image/tree1.svg"}]',
                    path='[{"coordinate":[0,6],"connectedNodes":[1]},{"coordinate":[1,6],"connectedNodes":[0,2]},{"coordinate":[2,6],"connectedNodes":[1,3]},{"coordinate":[2,5],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[3,5]},{"coordinate":[3,4],"connectedNodes":[4,6]},{"coordinate":[4,4],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[8,10]},{"coordinate":[6,2],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11]}]')

    # Data for levels 26, 27, 28 will come once we can change the theme of the level.
    level26 = Level(name=26, default=0, destination=[], 
                    decor='',
                    path='') 

    level27 = Level(name=27, default=0, destination=[],
                    decor='',
                    path='')

    level28 = Level(name=28, default=0, destination=[],
                    decor='',
                    path='')

    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards", "controls_repeat"])

    level19.next_level = level20
    level20.next_level = level21
    level21.next_level = level22
    level22.next_level = level23
    level23.next_level = level24
    level24.next_level = level25

    level19.blocks = blocks
    level20.blocks = blocks
    level21.blocks = blocks
    level22.blocks = blocks
    level23.blocks = blocks
    level24.blocks = blocks
    level25.blocks = blocks
    level26.blocks = blocks
    level27.blocks = blocks
    level28.blocks = blocks
    
    level19.save()
    level20.save()
    level21.save()
    level22.save()
    level23.save()
    level24.save()
    level25.save()
    level26.save()
    level27.save()
    level28.save()

    ##### Until

    level29 = Level(name=13, default=1, destination=[4, 3],
                    decor='[{"coordinate":{"x":96,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":257,"y":514},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":512},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":431},"url":"/static/game/image/tree1.svg"}]',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3]}]')

    level30 = Level(name=14, default=1, destination=[4, 6],
                    decor='[{"coordinate":{"x":96,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":200,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":257,"y":514},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":149,"y":512},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":431},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":188},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":132,"y":118},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":261,"y":102},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":190,"y":33},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":75,"y":35},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":11},"url":"/static/game/image/tree2.svg"}]',
                    path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[1,4],"connectedNodes":[1,3]},{"coordinate":[2,4],"connectedNodes":[2,4]},{"coordinate":[2,5],"connectedNodes":[3,5]},{"coordinate":[3,5],"connectedNodes":[4,6]},{"coordinate":[3,6],"connectedNodes":[5,7]},{"coordinate":[4,6],"connectedNodes":[6]}] ')

    level31 = Level(name=31, default=1, destination=[],
                    decor='',
                    path='')

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards", "controls_whileUntil"])



    # add blocks



    # add blocks

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
    episode_blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards", \
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


# Add new episodes for the simple junctions
# Shuffle up all the episodes by swapping?
def insert_shortest_path_episode(Level, Episode, Block):

    first = insert_new_shortest_path(Level, Block)
    episode = Episode(name="Shortest route", first_level=first)
    basic = Episode.objects.get(id=1)
    loops = basic.next_episode

    episode.next_episode = loops
    basic.next_episode = episode

    episode.save()
    basic.save()


def insert_new_shortest_path(Level, Block):

    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level13 = Level(name=13, default=1, destination=[0, 1], model_solution=11,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    decor='[{"coordinate":{"x":48,"y":658},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":49,"y":553},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":446},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":50,"y":340},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":406,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":496,"y":492},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":500,"y":302},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":245},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":193},"url":"/static/game/image/bush.svg"}]'
                    )

    level14 = Level(name=14, default=1, destination=[2, 5], model_solution=7,
                    path='[{"coordinate":[7,2],"connectedNodes":[27]},{"coordinate":[4,2],"connectedNodes":[4,14]},{"coordinate":[3,1],"connectedNodes":[3,14]},{"coordinate":[2,1],"connectedNodes":[7,2]},{"coordinate":[4,3],"connectedNodes":[10,5,1]},{"coordinate":[5,3],"connectedNodes":[4,6]},{"coordinate":[6,3],"connectedNodes":[5,11,27]},{"coordinate":[1,1],"connectedNodes":[8,3]},{"coordinate":[1,2],"connectedNodes":[21,7]},{"coordinate":[3,4],"connectedNodes":[16,10]},{"coordinate":[4,4],"connectedNodes":[9,4]},{"coordinate":[6,4],"connectedNodes":[12,6]},{"coordinate":[6,5],"connectedNodes":[20,11]},{"coordinate":[5,1],"connectedNodes":[14,15]},{"coordinate":[4,1],"connectedNodes":[2,1,13]},{"coordinate":[6,1],"connectedNodes":[13,27]},{"coordinate":[3,5],"connectedNodes":[26,17,9]},{"coordinate":[3,6],"connectedNodes":[18,16]},{"coordinate":[4,6],"connectedNodes":[17,19]},{"coordinate":[5,6],"connectedNodes":[18,20]},{"coordinate":[6,6],"connectedNodes":[19,12]},{"coordinate":[2,2],"connectedNodes":[8,22]},{"coordinate":[2,3],"connectedNodes":[23,21]},{"coordinate":[1,3],"connectedNodes":[24,22]},{"coordinate":[1,4],"connectedNodes":[25,23]},{"coordinate":[1,5],"connectedNodes":[26,24]},{"coordinate":[2,5],"connectedNodes":[25,16]},{"coordinate":[6,2],"connectedNodes":[6,0,15]}]',
                    decor='[{"coordinate":{"x":209,"y":392},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":307,"y":302},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":281,"y":187},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":498,"y":197},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":771,"y":662},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":866,"y":557},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":754,"y":491},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":890,"y":310},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":725,"y":353},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":780,"y":87},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":862,"y":177},"url":"/static/game/image/tree1.svg"}]'
                    )
    level15 = Level(name=15, default=1, destination=[7, 2], model_solution=11,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,4,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[9,2]},{"coordinate":[3,6],"connectedNodes":[1,5]},{"coordinate":[4,6],"connectedNodes":[4,6]},{"coordinate":[4,7],"connectedNodes":[7,5]},{"coordinate":[5,7],"connectedNodes":[6,8]},{"coordinate":[5,6],"connectedNodes":[7,13]},{"coordinate":[0,5],"connectedNodes":[3,10]},{"coordinate":[0,4],"connectedNodes":[9,11]},{"coordinate":[1,4],"connectedNodes":[10,12]},{"coordinate":[2,4],"connectedNodes":[11,15]},{"coordinate":[5,5],"connectedNodes":[8,14]},{"coordinate":[5,4],"connectedNodes":[16,13,17]},{"coordinate":[3,4],"connectedNodes":[12,16]},{"coordinate":[4,4],"connectedNodes":[15,14,21]},{"coordinate":[5,3],"connectedNodes":[21,14,18]},{"coordinate":[5,2],"connectedNodes":[17,19]},{"coordinate":[6,2],"connectedNodes":[18,20]},{"coordinate":[7,2],"connectedNodes":[19]},{"coordinate":[4,3],"connectedNodes":[16,17]}]',
                    decor='[{"coordinate":{"x":406,"y":205},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":296},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":98,"y":661},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":592},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":15,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":46,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":579,"y":501},"url":"/static/game/image/bush.svg"}]'
                    )

    level16 = Level(name=16, default=1, destination=[7, 0], model_solution=13,
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[2,0,11]},{"coordinate":[1,6],"connectedNodes":[1,3]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[1,3],"connectedNodes":[4,6]},{"coordinate":[1,2],"connectedNodes":[5,7]},{"coordinate":[2,2],"connectedNodes":[6,8]},{"coordinate":[3,2],"connectedNodes":[7,29,9]},{"coordinate":[4,2],"connectedNodes":[8,10]},{"coordinate":[5,2],"connectedNodes":[9,27,17]},{"coordinate":[2,5],"connectedNodes":[1,12]},{"coordinate":[3,5],"connectedNodes":[11,13]},{"coordinate":[3,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[13,15]},{"coordinate":[4,5],"connectedNodes":[14,21,16]},{"coordinate":[4,4],"connectedNodes":[28,15]},{"coordinate":[5,1],"connectedNodes":[10,18]},{"coordinate":[5,0],"connectedNodes":[17,19]},{"coordinate":[6,0],"connectedNodes":[18,20]},{"coordinate":[7,0],"connectedNodes":[19]},{"coordinate":[5,5],"connectedNodes":[15,22]},{"coordinate":[6,5],"connectedNodes":[21,23]},{"coordinate":[7,5],"connectedNodes":[22,24]},{"coordinate":[7,4],"connectedNodes":[23,25]},{"coordinate":[7,3],"connectedNodes":[24,26]},{"coordinate":[7,2],"connectedNodes":[27,25]},{"coordinate":[6,2],"connectedNodes":[10,26]},{"coordinate":[3,4],"connectedNodes":[16,29]},{"coordinate":[3,3],"connectedNodes":[28,8]}]',
                    decor='[{"coordinate":{"x":188,"y":399},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":587,"y":97},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":652,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":751,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":787,"y":627},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":687,"y":623},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":924,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":922,"y":608},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":843,"y":690},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":956,"y":517},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":544,"y":675},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":791,"y":504},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":926,"y":425},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":859,"y":563},"url":"/static/game/image/tree2.svg"}] '
                    )

    level17 = Level(name=17, default=1, destination=[4, 1], model_solution=12,
                    path='[{"coordinate":[2,6],"connectedNodes":[30]},{"coordinate":[3,6],"connectedNodes":[2,28]},{"coordinate":[4,6],"connectedNodes":[1,3]},{"coordinate":[5,6],"connectedNodes":[2,6,4]},{"coordinate":[5,5],"connectedNodes":[3,5]},{"coordinate":[5,4],"connectedNodes":[10,4]},{"coordinate":[6,6],"connectedNodes":[3,7]},{"coordinate":[7,6],"connectedNodes":[6,8]},{"coordinate":[7,5],"connectedNodes":[7,9]},{"coordinate":[7,4],"connectedNodes":[8,16]},{"coordinate":[4,4],"connectedNodes":[5,26]},{"coordinate":[1,2],"connectedNodes":[29,19]},{"coordinate":[2,3],"connectedNodes":[29,13]},{"coordinate":[3,3],"connectedNodes":[12,26]},{"coordinate":[5,3],"connectedNodes":[15,17]},{"coordinate":[6,3],"connectedNodes":[14,16]},{"coordinate":[7,3],"connectedNodes":[15,9,25]},{"coordinate":[5,2],"connectedNodes":[27,14,18]},{"coordinate":[5,1],"connectedNodes":[22,17,23]},{"coordinate":[1,1],"connectedNodes":[11,20]},{"coordinate":[2,1],"connectedNodes":[19,21]},{"coordinate":[3,1],"connectedNodes":[20,22]},{"coordinate":[4,1],"connectedNodes":[21,18]},{"coordinate":[6,1],"connectedNodes":[18,24]},{"coordinate":[7,1],"connectedNodes":[23,25]},{"coordinate":[7,2],"connectedNodes":[16,24]},{"coordinate":[4,3],"connectedNodes":[13,10,27]},{"coordinate":[4,2],"connectedNodes":[26,17]},{"coordinate":[3,5],"connectedNodes":[30,1]},{"coordinate":[1,3],"connectedNodes":[12,11]},{"coordinate":[2,5],"connectedNodes":[0,28]}]',
                    decor='[{"coordinate":{"x":573,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":674},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":673},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":380,"y":523},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":580,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":196,"y":190},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":296,"y":402},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-2,"y":532},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":387},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-3,"y":224},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-2,"y":68},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":1,"y":674},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":170,"y":403},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":308,"y":190},"url":"/static/game/image/tree1.svg"}]'
                    )

    level18 = Level(name=18, default=1, destination=[2, 7], model_solution=15,
                    path='[{"coordinate":[6,1],"connectedNodes":[4]},{"coordinate":[3,0],"connectedNodes":[49,2]},{"coordinate":[4,0],"connectedNodes":[1,3]},{"coordinate":[5,0],"connectedNodes":[2,4]},{"coordinate":[6,0],"connectedNodes":[3,0,5]},{"coordinate":[7,0],"connectedNodes":[4,6]},{"coordinate":[8,0],"connectedNodes":[5,11]},{"coordinate":[1,0],"connectedNodes":[8,49]},{"coordinate":[1,1],"connectedNodes":[9,7]},{"coordinate":[2,1],"connectedNodes":[8,10]},{"coordinate":[3,1],"connectedNodes":[9,38]},{"coordinate":[8,1],"connectedNodes":[12,6]},{"coordinate":[8,2],"connectedNodes":[13,11]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[43,18,16,42]},{"coordinate":[7,7],"connectedNodes":[19,17]},{"coordinate":[6,7],"connectedNodes":[20,18]},{"coordinate":[5,7],"connectedNodes":[21,19]},{"coordinate":[4,7],"connectedNodes":[22,20]},{"coordinate":[3,7],"connectedNodes":[30,21]},{"coordinate":[2,6],"connectedNodes":[24,30,48,29]},{"coordinate":[1,6],"connectedNodes":[25,23]},{"coordinate":[0,6],"connectedNodes":[24,26]},{"coordinate":[0,5],"connectedNodes":[25,27]},{"coordinate":[0,4],"connectedNodes":[26,31]},{"coordinate":[2,4],"connectedNodes":[29,34,33]},{"coordinate":[2,5],"connectedNodes":[23,28]},{"coordinate":[2,7],"connectedNodes":[22,23]},{"coordinate":[0,3],"connectedNodes":[27,32]},{"coordinate":[1,3],"connectedNodes":[31,33]},{"coordinate":[2,3],"connectedNodes":[32,28]},{"coordinate":[3,4],"connectedNodes":[28,35]},{"coordinate":[4,4],"connectedNodes":[34,39,36]},{"coordinate":[4,3],"connectedNodes":[35,37]},{"coordinate":[4,2],"connectedNodes":[36,38]},{"coordinate":[4,1],"connectedNodes":[10,37]},{"coordinate":[5,4],"connectedNodes":[35,40]},{"coordinate":[6,4],"connectedNodes":[39,41]},{"coordinate":[7,4],"connectedNodes":[40,42]},{"coordinate":[7,5],"connectedNodes":[17,41]},{"coordinate":[6,6],"connectedNodes":[44,17]},{"coordinate":[5,6],"connectedNodes":[43,45]},{"coordinate":[5,5],"connectedNodes":[46,44]},{"coordinate":[4,5],"connectedNodes":[47,45]},{"coordinate":[4,6],"connectedNodes":[48,46]},{"coordinate":[3,6],"connectedNodes":[23,47]},{"coordinate":[2,0],"connectedNodes":[7,1]}]',
                    decor='[{"coordinate":{"x":875,"y":86},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":874,"y":448},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":775,"y":688},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":119,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":93,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":296,"y":289},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":487,"y":203},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":231,"y":189},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":73,"y":172},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":604,"y":300},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":672,"y":194},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":516,"y":286},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":587,"y":211},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":283},"url":"/static/game/image/tree2.svg"}]'
                    )

    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()

    level13.next_level = level14
    level14.next_level = level15
    level15.next_level = level16
    level16.next_level = level17
    level17.next_level = level18

    level13.blocks = blocks
    level14.blocks = blocks
    level15.blocks = blocks
    level16.blocks = blocks
    level17.blocks = blocks
    level18.blocks = blocks

    level13.save()
    level14.save()
    level15.save()
    level16.save()
    level17.save()
    level18.save()

    return level13


def insert_new_first_episode(Level, Block):

    level3 = Level.objects.get(id=3)
    level5 = Level.objects.get(id=4)
    level7 = Level.objects.get(id=5)
    blocks = Block.objects.filter(type__in=["turn_left", "turn_right", "move_forwards"])

    level4 = Level(name=4, default=1, destination=[4, 5], next_level=level5,
                   path='[{"coordinate":[0,3],"connectedNodes":[1]},{"coordinate":[1,3],"connectedNodes":[0,2]},{"coordinate":[2,3],"connectedNodes":[1,3]},{"coordinate":[3,3],"connectedNodes":[2,4]},{"coordinate":[4,3],"connectedNodes":[3,5]},{"coordinate":[4,4],"connectedNodes":[6,4]},{"coordinate":[4,5],"connectedNodes":[5]}]',
                   decor='[{"coordinate":{"x":531,"y":624},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":442,"y":632},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":531,"y":498},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":495,"y":564},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":584,"y":565},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":615,"y":630},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":669,"y":565},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":621,"y":497},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":500,"y":694},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":300,"y":633},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":380,"y":704},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":365,"y":596},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":287,"y":713},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":596,"y":714},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":711,"y":704},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":813,"y":702},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":906,"y":700},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":897,"y":607},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":807,"y":608},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":719,"y":636},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":857,"y":659},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":766,"y":701},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":665,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":851,"y":568},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":766,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":155,"y":680},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":216,"y":541},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":530,"y":402},"url":"/static/game/image/tree1.svg"}]',
                   model_solution=5
                   )

    level4.save()

    level6 = Level(name=6, default=1, destination=[6, 1], next_level=level7,
                   path='[{"coordinate":[0,4],"connectedNodes":[1]},{"coordinate":[1,4],"connectedNodes":[0,2]},{"coordinate":[2,4],"connectedNodes":[1,3]},{"coordinate":[3,4],"connectedNodes":[2,4]},{"coordinate":[3,5],"connectedNodes":[5,3]},{"coordinate":[4,5],"connectedNodes":[4,6]},{"coordinate":[5,5],"connectedNodes":[5,7]},{"coordinate":[5,4],"connectedNodes":[6,8]},{"coordinate":[5,3],"connectedNodes":[7,9]},{"coordinate":[5,2],"connectedNodes":[8,10]},{"coordinate":[5,1],"connectedNodes":[9,11]},{"coordinate":[6,1],"connectedNodes":[10]}]',
                   decor='[{"coordinate":{"x":224,"y":654},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":87,"y":656},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":591},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":163,"y":562},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":100,"y":506},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":153,"y":624},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":608,"y":480},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":584,"y":366},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":591,"y":220},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":676,"y":254},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":689,"y":351},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":673,"y":509},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":557,"y":574},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":104,"y":200},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":201},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":102,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":201,"y":102},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":301,"y":103},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":147,"y":197},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":240,"y":127},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":154,"y":121},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":262,"y":215},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":328,"y":155},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":147,"y":715},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":65,"y":144},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":78,"y":220},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":262,"y":70},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":371,"y":85},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":64,"y":63},"url":"/static/game/image/tree2.svg"}]',
                   model_solution=10
                  )
    
    level6.save()

    level3.next_level = level4
    level5.next_level = level6
    level3.save()
    level5.save()

    level9 = Level.objects.get(id=7)

    level10 = Level(name=10, default=1, destination=[3, 3], model_solution=7,
                    path='[{"coordinate":[5,5],"connectedNodes":[1]},{"coordinate":[4,5],"connectedNodes":[2,0]},{"coordinate":[4,6],"connectedNodes":[3,1]},{"coordinate":[3,6],"connectedNodes":[4,2]},{"coordinate":[2,6],"connectedNodes":[3,5]},{"coordinate":[2,5],"connectedNodes":[4,6]},{"coordinate":[2,4],"connectedNodes":[5,7]},{"coordinate":[2,3],"connectedNodes":[6,8]},{"coordinate":[3,3],"connectedNodes":[7]}]',
                    decor='[{"coordinate":{"x":99,"y":699},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":201,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":54,"y":634},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":143,"y":632},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-5,"y":703},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":298,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":94,"y":555},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":504,"y":389},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-13,"y":584},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":17,"y":503},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":484,"y":604},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":582,"y":600},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":599,"y":413},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":606,"y":501},"url":"/static/game/image/bush.svg"}]'
                    )

    level11 = Level(name=11, default=1, destination=[1, 3], model_solution=12,
                    path='[{"coordinate":[3,4],"connectedNodes":[1]},{"coordinate":[2,4],"connectedNodes":[2,0]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[3,5],"connectedNodes":[2,4]},{"coordinate":[4,5],"connectedNodes":[3,5]},{"coordinate":[5,5],"connectedNodes":[4,6]},{"coordinate":[5,4],"connectedNodes":[5,7]},{"coordinate":[5,3],"connectedNodes":[6,8]},{"coordinate":[5,2],"connectedNodes":[9,7]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]}]',
                    decor='[{"coordinate":{"x":396,"y":304},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":600,"y":302},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":242,"y":301},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":601,"y":434},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":599,"y":701},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":598,"y":580},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":116,"y":701},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":236,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":359,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":480,"y":698},"url":"/static/game/image/tree2.svg"}]'
                    )

    level12 = Level(name=12, default=1, destination=[1, 3], model_solution=17,
                    path='[{"coordinate":[5,7],"connectedNodes":[17]},{"coordinate":[2,6],"connectedNodes":[18,2]},{"coordinate":[2,5],"connectedNodes":[3,1]},{"coordinate":[1,5],"connectedNodes":[2,4]},{"coordinate":[1,4],"connectedNodes":[3,5]},{"coordinate":[2,4],"connectedNodes":[4,6]},{"coordinate":[3,4],"connectedNodes":[5,7]},{"coordinate":[4,4],"connectedNodes":[6,8]},{"coordinate":[4,3],"connectedNodes":[7,9]},{"coordinate":[4,2],"connectedNodes":[10,8]},{"coordinate":[3,2],"connectedNodes":[11,9]},{"coordinate":[2,2],"connectedNodes":[12,10]},{"coordinate":[1,2],"connectedNodes":[13,11]},{"coordinate":[1,3],"connectedNodes":[12]},{"coordinate":[1,7],"connectedNodes":[15,18]},{"coordinate":[2,7],"connectedNodes":[14,16]},{"coordinate":[3,7],"connectedNodes":[15,17]},{"coordinate":[4,7],"connectedNodes":[16,0]},{"coordinate":[1,6],"connectedNodes":[14,1]}]',
                    decor='[{"coordinate":{"x":331,"y":509},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":267,"y":489},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":284,"y":561},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":402,"y":479},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":452,"y":532},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":418,"y":583},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":376,"y":545},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":356,"y":606},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":164,"y":86},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-15,"y":-11},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":279,"y":-20},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":202,"y":4},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":73,"y":109},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":-4,"y":84},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":63,"y":18},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":119,"y":2},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":381,"y":-14},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":323,"y":40},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":565,"y":81},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":493,"y":148},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":445,"y":-23},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":417,"y":72},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":549,"y":7},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":265,"y":120},"url":"/static/game/image/tree2.svg"}]'
                    )

    level9.save()
    level10.save()
    level11.save()
    level12.save()

    level9.next_level = level10
    level10.next_level = level11
    level11.next_level = level12

    level10.blocks = blocks
    level11.blocks = blocks
    level12.blocks = blocks

    level10.save()
    level11.save()
    level12.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0028_level_name_fix'),
    ]

    operations = [
        migrations.RunPython(drop_and_add_new),
    ]
