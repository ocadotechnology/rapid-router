from django.db import migrations
from game.level_management import set_decor_inner, set_blocks_inner
import json


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level = Level.objects.get(name="40", default=1)
    level.model_solution = "[6,7]"
    level.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0049_level_score_34")]

    operations = [migrations.RunPython(update_level)]
