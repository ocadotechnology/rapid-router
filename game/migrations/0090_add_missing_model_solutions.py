from django.apps.registry import Apps
from django.db import migrations


def add_missing_model_solutions(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    model_solutions = {
        "80": "[5]",
        "81": "[10]",
        "82": "[11]",
        "83": "[5]",
        "84": "[5]",
        "85": "[3]",
        "86": "[8]",
        "87": "[8]",
        "88": "[11]",
        "89": "[11]",
        "90": "[15]",
        "91": "[15]",
    }

    for level_name, model_solution in model_solutions.items():
        level = Level.objects.get(name=level_name)
        level.model_solution = model_solution
        level.save()

    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(level__episode__pk=10, score=10).update(score=20)


def remove_new_model_solutions(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    episode_10 = Episode.objects.get(pk=10)

    episode_10.level_set.all().update(model_solution="[]")

    Attempt = apps.get_model("game", "Attempt")

    Attempt.objects.filter(level__episode__pk=10, score=20).update(score=10)


class Migration(migrations.Migration):
    dependencies = [("game", "0089_episodes_in_development")]
    operations = [
        migrations.RunPython(
            add_missing_model_solutions,
            reverse_code=remove_new_model_solutions,
        )
    ]
