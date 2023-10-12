from django.apps.registry import Apps
from django.db import migrations


def add_cows_to_existing_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    Block = apps.get_model("game", "Block")
    LevelBlock = apps.get_model("game", "LevelBlock")
    LevelDecor = apps.get_model("game", "LevelDecor")

    level_38 = Level.objects.get(name="38", default=1)
    level_38.cows = '[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":6},{"x":3,"y":4},{"x":3,"y":1}],"type":"WHITE"}]'
    level_38.theme_name = "farm"
    level_38.model_solution = "[10]"
    level_38.save()

    level_39 = Level.objects.get(name="39", default=1)
    level_39.cows = '[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":4,"y":4},{"x":8,"y":4},{"x":8,"y":6}],"type":"WHITE"}]'
    level_39.theme_name = "farm"
    level_39.model_solution = "[10]"
    level_39.disable_route_score = True
    level_39.save()

    level_47 = Level.objects.get(name="47", default=1)
    level_47.traffic_lights = "[]"
    level_47.cows = '[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":6,"y":4},{"x":4,"y":6},{"x":2,"y":4}],"type":"WHITE"}]'
    level_47.theme_name = "farm"
    level_47.model_solution = "[8]"
    level_47.save()

    block_sound_horn = Block.objects.get(type="sound_horn")
    block_cow_crossing = Block.objects.get(type="cow_crossing")

    LevelBlock.objects.filter(
        level=level_47,
        type__type__in=["traffic_light", "wait"],
    ).delete()

    LevelBlock.objects.bulk_create(
        [
            LevelBlock(level=level_38, type=block_sound_horn),
            LevelBlock(level=level_38, type=block_cow_crossing),
            LevelBlock(level=level_39, type=block_sound_horn),
            LevelBlock(level=level_39, type=block_cow_crossing),
            LevelBlock(level=level_47, type=block_sound_horn),
            LevelBlock(level=level_47, type=block_cow_crossing),
        ]
    )

    LevelDecor.objects.filter(
        level_id__in=[
            level_47.id,
        ]
    ).delete()

    LevelDecor.objects.bulk_create(
        [
            LevelDecor(
                x=570,
                y=296,
                decorName="pond",
                level=level_39,
            ),
            LevelDecor(
                x=570,
                y=408,
                decorName="pond",
                level=level_39,
            ),
            LevelDecor(
                x=570,
                y=514,
                decorName="pond",
                level=level_39,
            ),
            LevelDecor(
                x=293,
                y=300,
                decorName="tree1",
                level=level_39,
            ),
            LevelDecor(
                x=711,
                y=101,
                decorName="tree1",
                level=level_39,
            ),
            LevelDecor(
                x=897,
                y=604,
                decorName="tree1",
                level=level_39,
            ),
            LevelDecor(
                x=114,
                y=315,
                decorName="tree1",
                level=level_39,
            ),
            LevelDecor(
                x=37,
                y=502,
                decorName="pond",
                level=level_47,
            ),
            LevelDecor(
                x=39,
                y=400,
                decorName="pond",
                level=level_47,
            ),
            LevelDecor(
                x=39,
                y=296,
                decorName="pond",
                level=level_47,
            ),
            LevelDecor(
                x=720,
                y=657,
                decorName="bush",
                level=level_47,
            ),
            LevelDecor(
                x=720,
                y=556,
                decorName="bush",
                level=level_47,
            ),
            LevelDecor(
                x=720,
                y=455,
                decorName="bush",
                level=level_47,
            ),
            LevelDecor(
                x=720,
                y=343,
                decorName="bush",
                level=level_47,
            ),
            LevelDecor(
                x=720,
                y=220,
                decorName="bush",
                level=level_47,
            ),
            LevelDecor(
                x=403,
                y=378,
                decorName="tree1",
                level=level_47,
            ),
            LevelDecor(
                x=440,
                y=471,
                decorName="tree1",
                level=level_47,
            ),
            LevelDecor(
                x=132,
                y=649,
                decorName="tree1",
                level=level_47,
            ),
            LevelDecor(
                x=620,
                y=689,
                decorName="tree1",
                level=level_47,
            ),
            LevelDecor(
                x=500,
                y=149,
                decorName="tree1",
                level=level_47,
            ),
            LevelDecor(
                x=550,
                y=483,
                decorName="tree2",
                level=level_47,
            ),
        ]
    )


class Migration(migrations.Migration):
    dependencies = [("game", "0082_level_43_solution")]
    operations = [
        migrations.RunPython(
            add_cows_to_existing_levels,
            reverse_code=migrations.RunPython.noop,
        )
    ]
