from django.apps.registry import Apps
from django.db import migrations


def set_successful_python_attempts_to_10(apps: Apps, *args):
    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(
        level__default=True, level__blocklyEnabled=False,
        level__disable_algorithm_score=True, score=20
    ).update(score=10)


def set_successful_python_attempts_to_20(apps: Apps, *args):
    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(
        level__default=True, level__blocklyEnabled=False,
        level__disable_algorithm_score=True, score=10
    ).update(score=20)


class Migration(migrations.Migration):
    dependencies = [("game", "0090_python_levels_no_algo_score")]
    operations = [
        migrations.RunPython(
            set_successful_python_attempts_to_10,
            reverse_code=set_successful_python_attempts_to_20,
        )
    ]
