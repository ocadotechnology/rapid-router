from django.db import migrations
import json


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level40 = Level.objects.get(name="40", default=1)
    level40.model_solution = "[7]"
    level40.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0037_level_score_79")]

    operations = [migrations.RunPython(update_level)]
