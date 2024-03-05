from django.apps.registry import Apps
from django.db import migrations


def disable_algo_score_for_levels_without_model_solution(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(
        default=True, episode__isnull=False, model_solution="[]"
    ).update(disable_algorithm_score=True)

    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(
        level__default=True,
        level__episode__isnull=False,
        level__model_solution="[]",
        score=20,
    ).update(score=10)


def enable_algo_score_for_levels_without_model_solution(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(
        default=True, episode__isnull=False, model_solution="[]"
    ).update(disable_algorithm_score=False)

    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(
        level__default=True,
        level__episode__isnull=False,
        level__model_solution="[]",
        score=10,
    ).update(score=20)


class Migration(migrations.Migration):
    dependencies = [("game", "0090_add_missing_model_solutions")]
    operations = [
        migrations.RunPython(
            disable_algo_score_for_levels_without_model_solution,
            reverse_code=enable_algo_score_for_levels_without_model_solution,
        )
    ]
