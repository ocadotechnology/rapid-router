from django.apps.registry import Apps
from django.db import migrations, models

def add_python_den_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    def update_level_name(pk: int, name: str):
        # should we find the level by pk or by current name?
        # name need not be unique
        level = Level.objects.get(pk=pk)
        level.name = name
        level.save()

class Migration(migrations.Migration):
    dependencies = [("game", "0094_add_hint_lesson_subtitle_to_levels")]
    operations = [
        migrations.RunPython(
            add_python_den_levels
        )
    ]