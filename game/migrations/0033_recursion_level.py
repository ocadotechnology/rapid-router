from django.db import migrations
from game.level_management import set_blocks_inner
import json


def new_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    Character = apps.get_model("game", "Character")
    Theme = apps.get_model("game", "Theme")
    LevelDecor = apps.get_model("game", "LevelDecor")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")
    LevelDecor = apps.get_model("game", "LevelDecor")
    LevelBlock = apps.get_model("game", "LevelBlock")
    Block = apps.get_model("game", "Block")

    def set_decor(level, decor):
        """Helper method creating LevelDecor objects given a list of decor in dictionary form."""
        LevelDecor.objects.filter(level=level).delete()

        level_decors = []
        for data in decor:
            level_decors.append(
                LevelDecor(
                    level_id=level.id, x=data["x"], y=data["y"], decorName=data[
                        "decorName"]
                )
            )
        LevelDecor.objects.bulk_create(level_decors)

    def set_blocks(level, blocks):
        set_blocks_inner(level, blocks, LevelBlock, Block)

    level77 = Level(
        name="77",
        default=True,
        path='[{"coordinate":[2,2],"connectedNodes":[1]},{"coordinate":[3,2],"connectedNodes":[0,2]},{"coordinate":[4,2],"connectedNodes":[1,3]},{"coordinate":[5,2],"connectedNodes":[2,4]},{"coordinate":[6,2],"connectedNodes":[3,5]},{"coordinate":[7,2],"connectedNodes":[4,6]},{"coordinate":[8,2],"connectedNodes":[5,7]},{"coordinate":[8,3],"connectedNodes":[8,6]},{"coordinate":[8,4],"connectedNodes":[9,7]},{"coordinate":[8,5],"connectedNodes":[10,8]},{"coordinate":[8,6],"connectedNodes":[11,9]},{"coordinate":[7,6],"connectedNodes":[12,10]},{"coordinate":[6,6],"connectedNodes":[13,11]},{"coordinate":[5,6],"connectedNodes":[14,12]},{"coordinate":[4,6],"connectedNodes":[15,13]},{"coordinate":[3,6],"connectedNodes":[14,16]},{"coordinate":[3,5],"connectedNodes":[15,17]},{"coordinate":[3,4],"connectedNodes":[16,18]},{"coordinate":[4,4],"connectedNodes":[17,19]},{"coordinate":[5,4],"connectedNodes":[18,20]},{"coordinate":[6,4],"connectedNodes":[19]}]',
        traffic_lights="[]",
        destinations="[[6,4]]",
        origin='{"coordinate":[2,2],"direction":"E"}',
        max_fuel=50,
        blocklyEnabled=True,
        pythonEnabled=False,
        theme=Theme.objects.get(id=1),
        character=Character.objects.get(id="1"),
        model_solution="[9]",
        next_level=None,
        disable_route_score=True,
    )
    level77.save()
    set_decor(
        level77,
        json.loads(
            '[{"x":900,"y":410,"decorName":"tree1"},{"x":480,"y":490,"decorName":"tree1"},{"x":388,"y":284,"decorName":"tree1"},{"x":330,"y":318,"decorName":"tree1"},{"x":629,"y":292,"decorName":"tree1"},{"x":205,"y":622,"decorName":"tree2"},{"x":440,"y":290,"decorName":"tree2"},{"x":688,"y":469,"decorName":"tree2"},{"x":387,"y":518,"decorName":"tree2"},{"x":220,"y":314,"decorName":"tree2"},{"x":78,"y":259,"decorName":"bush"},{"x":82,"y":177,"decorName":"bush"},{"x":139,"y":117,"decorName":"bush"},{"x":232,"y":127,"decorName":"bush"},{"x":320,"y":135,"decorName":"bush"},{"x":397,"y":138,"decorName":"bush"},{"x":75,"y":490,"decorName":"tree1"},{"x":656,"y":17,"decorName":"tree2"}]'
        ),
    )
    set_blocks(
        level77,
        json.loads(
            '[{"type":"move_forwards","number":1},{"type":"turn_left","number":1},{"type":"wait"},{"type":"controls_if"},{"type":"road_exists"},{"type":"call_proc"},{"type":"declare_proc","number":2}]'
        ),
    )

    level76 = Level.objects.get(name="76", default=1)
    level76.next_level = level77
    level76.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0032_cannot_turn_left_level")]

    operations = [migrations.RunPython(new_level)]
