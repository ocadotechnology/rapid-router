from django.apps.registry import Apps
from django.db import migrations

def disable_algo_score_for_existing_custom_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(
        default=False
    ).update(disable_algorithm_score=True)

def enable_algo_score_for_existing_custom_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(
        default=False
    ).update(disable_algorithm_score=False)

class Migration(migrations.Migration):
    dependencies = [
        ("game", "0091_disable_algo_score_if_no_model_solution")
    ]

    operations = [
        migrations.RunPython(
            disable_algo_score_for_existing_custom_levels, 
            reverse_code=enable_algo_score_for_existing_custom_levels
        )
    ]