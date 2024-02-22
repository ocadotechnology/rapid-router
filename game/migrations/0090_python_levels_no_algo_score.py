from django.apps.registry import Apps
from django.db import migrations


def disable_algo_score_for_python_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(default=True, blocklyEnabled=False).update(
        disable_algorithm_score=True
    )


def enable_algo_score_for_python_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(default=True, blocklyEnabled=False).update(
        disable_algorithm_score=False
    )


class Migration(migrations.Migration):
    dependencies = [("game", "0089_episodes_in_development")]
    operations = [
        migrations.RunPython(
            disable_algo_score_for_python_levels,
            reverse_code=enable_algo_score_for_python_levels,
        )
    ]
