# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def decor_and_length(apps, schema_editor):

    Level = apps.get_model('game', 'Level')

    move_decor(Level)
    shorten_path(Level)


def move_decor(Level):

    level5 = Level.objects.get(id=5)
    level5.decor = '[{"coordinate":{"x":19,"y":459},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":135,"y":564},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":240,"y":666},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":184},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":208,"y":291},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":338,"y":410},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":497,"y":519},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":467,"y":701},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":898,"y":26},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":755,"y":22},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":901,"y":168},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":900,"y":322},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":607,"y":22},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":893,"y":638},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":899,"y":479},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":445,"y":23},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":293,"y":23},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":126,"y":23},"url":"/static/game/image/bush.svg"}]'
    level5.save()

    level7 = Level.objects.get(id=7)
    level7.decor = '[{"coordinate":{"x":6,"y":424},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":5,"y":559},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":5,"y":688},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":676,"y":644},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":588,"y":633},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":686,"y":578},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":766,"y":659},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":625,"y":669},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":801,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":610,"y":576},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":583,"y":524},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":762,"y":584},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":682,"y":511},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":699,"y":716},"url":"/static/game/image/tree2.svg"}]'
    level7.save()

    level19 = Level.objects.get(id=19)
    level19.decor = '[{"coordinate":{"x":393,"y":539},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":271,"y":613},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":340,"y":648},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":77,"y":639},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":147,"y":624},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":227,"y":682},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":228,"y":532},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":80,"y":518},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":327,"y":437},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":770,"y":-12},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":432,"y":-1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":468,"y":-9},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":632,"y":-8},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":542,"y":-18},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":622,"y":187},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":645,"y":45},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":542,"y":91},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":707,"y":284},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":711,"y":35},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":826,"y":26},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":782,"y":107},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":748,"y":135},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":848,"y":138},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":334,"y":94},"url":"/static/game/image/tree1.svg"}]'
    level19.save()

    level20 = Level.objects.get(id=20)
    level20.decor = '[{"coordinate":{"x":676,"y":311},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":700,"y":145},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":527,"y":190},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":829,"y":471},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":782,"y":188},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":650,"y":466},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":622,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":758,"y":318},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":856,"y":269},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":831,"y":386},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":153,"y":669},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":4,"y":548},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":86,"y":565},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":64,"y":665},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":393,"y":109},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":424,"y":352},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":595,"y":86},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":755,"y":407},"url":"/static/game/image/tree2.svg"}]'
    level20.save()

    level30 = Level.objects.get(id=30)
    level30.decor = '[{"coordinate":{"x":117,"y":700},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":244,"y":697},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":-6,"y":697},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":55,"y":594},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":184,"y":599},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":117,"y":490},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":480,"y":500},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":412,"y":397},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":544,"y":399},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":487,"y":295},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":618,"y":298},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":414,"y":188},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":564,"y":189},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":704,"y":189},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":265,"y":192},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":342,"y":295},"url":"/static/game/image/tree2.svg"}]'
    level30.save()



def shorten_path(Level):
    
    level22 = Level.objects.get(id=22)
    level22.path = '[{"coordinate":[8,3],"connectedNodes":[1]},{"coordinate":[7,3],"connectedNodes":[2,0]},{"coordinate":[6,3],"connectedNodes":[3,1]},{"coordinate":[5,3],"connectedNodes":[4,2]},{"coordinate":[5,4],"connectedNodes":[5,3]},{"coordinate":[5,5],"connectedNodes":[6,4]},{"coordinate":[5,6],"connectedNodes":[7,5]},{"coordinate":[4,6],"connectedNodes":[8,6]},{"coordinate":[3,6],"connectedNodes":[9,7]},{"coordinate":[2,6],"connectedNodes":[10,8]},{"coordinate":[1,6],"connectedNodes":[9,11]},{"coordinate":[1,5],"connectedNodes":[10,12]},{"coordinate":[1,4],"connectedNodes":[11,13]},{"coordinate":[1,3],"connectedNodes":[12,14]},{"coordinate":[1,2],"connectedNodes":[13,15]},{"coordinate":[1,1],"connectedNodes":[14,16]},{"coordinate":[2,1],"connectedNodes":[15,17]},{"coordinate":[3,1],"connectedNodes":[16,18]},{"coordinate":[4,1],"connectedNodes":[17,19]},{"coordinate":[5,1],"connectedNodes":[18,20]},{"coordinate":[6,1],"connectedNodes":[19,21]},{"coordinate":[7,1],"connectedNodes":[20,22]},{"coordinate":[8,1],"connectedNodes":[21,23]},{"coordinate":[9,1],"connectedNodes":[22,24]},{"coordinate":[9,2],"connectedNodes":[25,23]},{"coordinate":[9,3],"connectedNodes":[26,24]},{"coordinate":[9,4],"connectedNodes":[27,25]},{"coordinate":[9,5],"connectedNodes":[28,26]},{"coordinate":[8,5],"connectedNodes":[29,27]},{"coordinate":[7,5],"connectedNodes":[28]}]'
    level22.decor = '[{"coordinate":{"x":859,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":727,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":574,"y":696},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":414,"y":694},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":256,"y":695},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":83,"y":693},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":840,"y":1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":651,"y":0},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":457,"y":-1},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":257,"y":-2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":58,"y":-3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":378,"y":478},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":209,"y":426},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":409,"y":292},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":233,"y":226},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":629,"y":201},"url":"/static/game/image/tree1.svg"}]'
    level22.model_solution = 19
    level22.destination = [7, 5]
    level22.save()

    level23 = Level.objects.get(id=23)
    level23.path = '[{"coordinate":[8,6],"connectedNodes":[1]},{"coordinate":[7,6],"connectedNodes":[2,0]},{"coordinate":[6,6],"connectedNodes":[3,1]},{"coordinate":[5,6],"connectedNodes":[4,2]},{"coordinate":[4,6],"connectedNodes":[5,3]},{"coordinate":[3,6],"connectedNodes":[6,4]},{"coordinate":[2,6],"connectedNodes":[5,7]},{"coordinate":[2,5],"connectedNodes":[6,8]},{"coordinate":[3,5],"connectedNodes":[7,9]},{"coordinate":[4,5],"connectedNodes":[8,10]},{"coordinate":[5,5],"connectedNodes":[9,11]},{"coordinate":[6,5],"connectedNodes":[10,12]},{"coordinate":[7,5],"connectedNodes":[11,13]},{"coordinate":[8,5],"connectedNodes":[12,14]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[7,4],"connectedNodes":[16,14]},{"coordinate":[6,4],"connectedNodes":[17,15]},{"coordinate":[5,4],"connectedNodes":[18,16]},{"coordinate":[4,4],"connectedNodes":[19,17]},{"coordinate":[3,4],"connectedNodes":[20,18]},{"coordinate":[2,4],"connectedNodes":[19,21]},{"coordinate":[2,3],"connectedNodes":[20,22]},{"coordinate":[3,3],"connectedNodes":[21,23]},{"coordinate":[4,3],"connectedNodes":[22,24]},{"coordinate":[5,3],"connectedNodes":[23,25]},{"coordinate":[6,3],"connectedNodes":[24,26]},{"coordinate":[7,3],"connectedNodes":[25,27]},{"coordinate":[8,3],"connectedNodes":[26,28]},{"coordinate":[8,2],"connectedNodes":[29,27]},{"coordinate":[7,2],"connectedNodes":[28]}] '
    level23.decor = '[{"coordinate":{"x":1,"y":4},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":3,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":-1,"y":199},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":101,"y":697},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":2,"y":600},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":200,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":399,"y":3},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":603,"y":2},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":299,"y":697},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":702,"y":699},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":895,"y":698},"url":"/static/game/image/bush.svg"}]'
    level23.destination = [7, 2]
    level23.model_solution = 9
    level23.save()

    level24 = Level.objects.get(id=24)
    level24.path = '[{"coordinate":[2,6],"connectedNodes":[27]},{"coordinate":[2,3],"connectedNodes":[2,28]},{"coordinate":[3,3],"connectedNodes":[1,3]},{"coordinate":[3,2],"connectedNodes":[2,4]},{"coordinate":[4,2],"connectedNodes":[3,5]},{"coordinate":[4,3],"connectedNodes":[6,4]},{"coordinate":[5,3],"connectedNodes":[5,7]},{"coordinate":[5,2],"connectedNodes":[6,8]},{"coordinate":[6,2],"connectedNodes":[7,9]},{"coordinate":[6,3],"connectedNodes":[10,8]},{"coordinate":[7,3],"connectedNodes":[9,11]},{"coordinate":[7,2],"connectedNodes":[10,12]},{"coordinate":[8,2],"connectedNodes":[11,13]},{"coordinate":[8,3],"connectedNodes":[14,12]},{"coordinate":[8,4],"connectedNodes":[15,13]},{"coordinate":[8,5],"connectedNodes":[16,14]},{"coordinate":[8,6],"connectedNodes":[17,15]},{"coordinate":[7,6],"connectedNodes":[16,18]},{"coordinate":[7,5],"connectedNodes":[19,17]},{"coordinate":[6,5],"connectedNodes":[20,18]},{"coordinate":[6,6],"connectedNodes":[21,19]},{"coordinate":[5,6],"connectedNodes":[20,22]},{"coordinate":[5,5],"connectedNodes":[23,21]},{"coordinate":[4,5],"connectedNodes":[24,22]},{"coordinate":[4,6],"connectedNodes":[25,23]},{"coordinate":[3,6],"connectedNodes":[24,26]},{"coordinate":[3,5],"connectedNodes":[27,25]},{"coordinate":[2,5],"connectedNodes":[0,26]},{"coordinate":[2,2],"connectedNodes":[1]}]'
    level24.decor = '[{"coordinate":{"x":476,"y":109},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":699,"y":64},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":572,"y":20},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":633,"y":95},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":75,"y":560},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":217,"y":704},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":101,"y":696},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":624},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":700,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":552,"y":402},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":401,"y":400},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":246,"y":401},"url":"/static/game/image/bush.svg"}]'
    level24.destination = [2, 2]
    level24.model_solution = 12
    level24.save()





class Migration(migrations.Migration):

    dependencies = [
        ('game', '0030_new_episodes'),
    ]

    operations = [
        migrations.RunPython(decor_and_length),
    ]
