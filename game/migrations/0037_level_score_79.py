from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner
import json


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level79 = Level.objects.get(name="79", default=1)
    level79.model_solution = "[16]"
    level79.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0036_level_score_73")]

    operations = [migrations.RunPython(update_level)]
