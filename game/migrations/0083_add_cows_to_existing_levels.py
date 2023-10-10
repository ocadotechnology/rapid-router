from django.apps.registry import Apps
from django.db import migrations


def add_cows_to_existing_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    Block = apps.get_model("game", "Block")
    LevelBlock = apps.get_model("game", "LevelBlock")

    level_38 = Level.objects.get(name="38", default=1)
    level_38.cows = '[{"minCows":1,"maxCows":1,"potentialCoordinates":[{"x":2,"y":6},{"x":3,"y":4},{"x":3,"y":1}],"type":"WHITE"}]'
    level_38.theme_name = "farm"
    level_38.save()

    block_sound_horn = Block.objects.get(type="sound_horn")
    block_cow_crossing = Block.objects.get(type="cow_crossing")

    LevelBlock.objects.bulk_create(
        [
            LevelBlock(level=level_38, type=block_sound_horn),
            LevelBlock(level=level_38, type=block_cow_crossing),
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
