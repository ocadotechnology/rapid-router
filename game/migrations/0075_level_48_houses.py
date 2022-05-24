from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level48 = Level.objects.get(name="48", default=1)
    level48.destinations = "[[1, 2], [6, 2], [6, 7], [7, 4]]"
    level48.model_solution = "[14, 15]"
    level48.save()


def revert_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level48 = Level.objects.get(name="48", default=1)
    level48.destinations = "[[1, 2]]"
    level48.model_solution = "[12, 13]"
    level48.save()


def add_levelblock(apps, schema_editor):
    Block = apps.get_model("game", "Block")
    Level = apps.get_model("game", "Level")
    LevelBlock = apps.get_model("game", "LevelBlock")

    level48 = Level.objects.get(name="48", default=1)
    deliver_block = Block.objects.get(type="deliver")

    newBlock = LevelBlock(type=deliver_block, number=None, level=level48)
    newBlock.save()


def remove_levelblock(apps, schema_editor):
    Block = apps.get_model("game", "Block")
    Level = apps.get_model("game", "Level")
    LevelBlock = apps.get_model("game", "LevelBlock")

    level48 = Level.objects.get(name="48", default=1)
    deliver_block = Block.objects.get(type="deliver")

    LevelBlock.objects.filter(level=level48, type=deliver_block).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0074_level_74_solution"),
    ]

    operations = [
        migrations.RunPython(update_level, reverse_code=revert_level),
        migrations.RunPython(add_levelblock, reverse_code=remove_levelblock),
    ]
