from django.apps.registry import Apps
from django.db import migrations


def update_level_model_solution(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    level43 = Level.objects.get(name="1015", default=True)
    level43.model_solution = "[11,12]"
    level43.save()


def revert_level_model_solution(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    level43 = Level.objects.get(name="1015", default=True)
    level43.model_solution = "[11]"
    level43.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0102_reoder_episodes_13_14")]
    operations = [
        migrations.RunPython(
            update_level_model_solution,
            reverse_code=revert_level_model_solution,
        )
    ]
