# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def transferBlockData(apps, schema_editor):
        Level = apps.get_model('game', 'Level')
        Block = apps.get_model('game', 'Block')
        LevelBlock = apps.get_model('game', 'LevelBlock')

        for level in Level.objects.all():
            for block in level.blocks.all():
                newBlock = LevelBlock(type=block, number=None, level=level)
                newBlock.save()

    def addTestLevel(apps, schema_editor):
        Level = apps.get_model('game', 'Level')
        Block = apps.get_model('game', 'Block')
        LevelBlock = apps.get_model('game', 'LevelBlock')
        Character = apps.get_model('game', 'Character')
        Theme = apps.get_model('game', 'Theme')

        van = Character.objects.get(name="Van")
        grass = Theme.objects.get(name="grass")

        testLevel = Level(name='Limited blocks test', anonymous=False, blocklyEnabled=True, character=van, default=True,
                    decor='[{"coordinate":{"x":48,"y":658},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":49,"y":553},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":48,"y":446},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":50,"y":340},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":52,"y":235},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":406,"y":512},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":496,"y":492},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":500,"y":302},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":501,"y":245},"url":"/static/game/image/bush.svg"},{"coordinate":{"x":500,"y":193},"url":"/static/game/image/bush.svg"}]',
                    destinations='[[0, 1]]', direct_drive=True, fuel_gauge=False, max_fuel=50,
                    model_solution='[11]', origin='{"coordinate":[2, 7], "direction":"S"}',
                    path='[{"coordinate":[2,7],"connectedNodes":[1]},{"coordinate":[2,6],"connectedNodes":[0,2]},{"coordinate":[3,6],"connectedNodes":[1,3,10]},{"coordinate":[4,6],"connectedNodes":[2,4]},{"coordinate":[5,6],"connectedNodes":[3,5]},{"coordinate":[6,6],"connectedNodes":[4,6]},{"coordinate":[6,5],"connectedNodes":[5,7]},{"coordinate":[6,4],"connectedNodes":[13,6,8]},{"coordinate":[6,3],"connectedNodes":[7,9]},{"coordinate":[6,2],"connectedNodes":[8,14]},{"coordinate":[3,5],"connectedNodes":[2,11]},{"coordinate":[3,4],"connectedNodes":[10,12]},{"coordinate":[4,4],"connectedNodes":[11,13,18]},{"coordinate":[5,4],"connectedNodes":[12,7]},{"coordinate":[6,1],"connectedNodes":[15,9]},{"coordinate":[5,1],"connectedNodes":[16,14]},{"coordinate":[4,1],"connectedNodes":[19,17,15]},{"coordinate":[4,2],"connectedNodes":[18,16]},{"coordinate":[4,3],"connectedNodes":[12,17]},{"coordinate":[3,1],"connectedNodes":[20,16]},{"coordinate":[2,1],"connectedNodes":[21,19]},{"coordinate":[1,1],"connectedNodes":[22,20]},{"coordinate":[0,1],"connectedNodes":[21]}]',
                    pythonEnabled=False, theme=grass, threads=1, traffic_lights='[]')

        testLevel.save();

        block1 = LevelBlock(type=Block.objects.get(type="move_forwards"), number=1, level=testLevel)
        block2 = LevelBlock(type=Block.objects.get(type="turn_right"), number=2, level=testLevel)
        block3 = LevelBlock(type=Block.objects.get(type="turn_left"),  number=10, level=testLevel)
        block4 = LevelBlock(type=Block.objects.get(type="controls_repeat"), number=1, level=testLevel)
        block5 = LevelBlock(type=Block.objects.get(type="wait"), number=1, level=testLevel)

        block1.save()
        block2.save()
        block3.save()
        block4.save()
        block5.save()

    dependencies = [
        ('game', '0004_leveldecor'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(default=None,  null=True)),
                ('level', models.ForeignKey(to='game.Level')),
                ('type', models.ForeignKey(to='game.Block')),
            ],
            options={
            },
            bases=(models.Model,),
        ),        

        migrations.RunPython(transferBlockData),

        migrations.RemoveField(
            model_name='level',
            name='blocks',
        ),

        migrations.RunPython(addTestLevel)
    ]
