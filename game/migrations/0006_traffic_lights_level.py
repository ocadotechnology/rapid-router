from django.db import models, migrations


def load_level(apps, schema_editor):
    Level = apps.get_model('game', 'Level')

    level27 = Level(
            destination=[6, 4],
            decor='[{"coordinate":{"x":0,"y":595},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":2,"y":502},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":6,"y":398},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":5,"y":201},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":8,"y":104},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":5},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":0,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":193,"y":702},"url":"/static/game/image/tree1.svg"},{"coordinate":{"x":403,"y":698},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":598,"y":700},"url":"/static/game/image/tree2.svg"},{"coordinate":{"x":799,"y":694},"url":"/static/game/image/tree2.svg"}]',
            default=True,
            max_fuel=50,
            name="27",
            path='[{"coordinate":[0,3],"connectedNodes":[1]}, {"coordinate":[1,3],"connectedNodes":[0,27,2]}, {"coordinate":[1,2],"connectedNodes":[1,3]}, {"coordinate":[1,1],"connectedNodes":[2,4]}, {"coordinate":[2,1],"connectedNodes":[3,6,5]}, {"coordinate":[2,0],"connectedNodes":[4]}, {"coordinate":[3,1],"connectedNodes":[4,7]}, {"coordinate":[4,1],"connectedNodes":[6,8]}, {"coordinate":[4,2],"connectedNodes":[9,11,7]}, {"coordinate":[4,3],"connectedNodes":[10,36,8]}, {"coordinate":[3,3],"connectedNodes":[9]}, {"coordinate":[5,2],"connectedNodes":[8,12]}, {"coordinate":[6,2],"connectedNodes":[11,15,13]}, {"coordinate":[6,1],"connectedNodes":[12,14]}, {"coordinate":[6,0],"connectedNodes":[13]}, {"coordinate":[7,2],"connectedNodes":[12,16]}, {"coordinate":[8,2],"connectedNodes":[15,25,17]}, {"coordinate":[8,1],"connectedNodes":[16,18]}, {"coordinate":[8,0],"connectedNodes":[17,19]}, {"coordinate":[9,0],"connectedNodes":[18,20]}, {"coordinate":[9,1],"connectedNodes":[21,19]}, {"coordinate":[9,2],"connectedNodes":[22,20]}, {"coordinate":[9,3],"connectedNodes":[23,21]}, {"coordinate":[9,4],"connectedNodes":[24,22]}, {"coordinate":[8,4],"connectedNodes":[26,23,25]}, {"coordinate":[8,3],"connectedNodes":[24,16]}, {"coordinate":[7,4],"connectedNodes":[42,28,24]}, {"coordinate":[1,4],"connectedNodes":[41,1]}, {"coordinate":[7,5],"connectedNodes":[29,26]}, {"coordinate":[7,6],"connectedNodes":[32,30,28]}, {"coordinate":[8,6],"connectedNodes":[29,31]}, {"coordinate":[9,6],"connectedNodes":[30]}, {"coordinate":[6,6],"connectedNodes":[33,29]}, {"coordinate":[5,6],"connectedNodes":[34,32]}, {"coordinate":[4,6],"connectedNodes":[33,35]}, {"coordinate":[4,5],"connectedNodes":[37,34,36]}, {"coordinate":[4,4],"connectedNodes":[35,9]}, {"coordinate":[3,5],"connectedNodes":[38,35]}, {"coordinate":[2,5],"connectedNodes":[39,37]}, {"coordinate":[2,6],"connectedNodes":[40,38]}, {"coordinate":[1,6],"connectedNodes":[39,41]}, {"coordinate":[1,5],"connectedNodes":[40,27]}, {"coordinate":[6,4],"connectedNodes":[26]} ]',
            traffic_lights='[{"node":4, "sourceNode":3, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"RED"},{"node":4, "sourceNode":5, "redDuration":4, "greenDuration":2, "startTime":2, "startingState":"RED"},{"node":4, "sourceNode":6, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"GREEN"},{"node":8, "sourceNode":7, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"RED"},{"node":8, "sourceNode":9, "redDuration":4, "greenDuration":2, "startTime":2, "startingState":"RED"},{"node":8, "sourceNode":11, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"GREEN"},{"node":35, "sourceNode":37, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"RED"},{"node":35, "sourceNode":34, "redDuration":4, "greenDuration":2, "startTime":2, "startingState":"RED"},{"node":35, "sourceNode":36, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"GREEN"},{"node":40, "sourceNode":39, "redDuration":2, "greenDuration":4, "startTime":0, "startingState":"RED"},{"node":24, "sourceNode":23, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"RED"},{"node":24, "sourceNode":25, "redDuration":4, "greenDuration":2, "startTime":2, "startingState":"RED"},{"node":24, "sourceNode":26, "redDuration":4, "greenDuration":2, "startTime":0, "startingState":"GREEN"}]'
        )
    level27.save()

    Block = apps.get_model('game', 'Block')
    level27.blocks = Block.objects.filter(
            type__in=["move_forwards", "turn_left", "turn_right", \
                    "controls_whileUntil", "controls_if", "logic_negate", \
                    "road_exists", "at_destination", "traffic_light", "wait"])
    level27.save()
    
    level26 = Level.objects.filter(name="26").first()
    level26.next_level = level27
    level26.save()


class Migration(migrations.Migration):

    dependencies = [
            ('game', '0005_auto_20140702_1829'),
    ]

    operations = [
            migrations.RunPython(load_level),
    ]

