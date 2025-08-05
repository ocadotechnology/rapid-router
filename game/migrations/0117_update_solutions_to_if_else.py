from django.apps.registry import Apps
from django.db import migrations

new_model_solutions_per_level = {
    34: "[6]",
    35: "[8]",
    36: "[8]",
    37: "[8]",
    40: "[6]",
    41: "[8]",
    44: "[6]",
    45: "[6]",
    46: "[8]",
    48: "[14]",
    49: "[10]",
}

old_model_solutions_per_level = {
    34: "[8,7,6]",
    35: "[11,9,8]",
    36: "[11,9,8]",
    37: "[11,9,8]",
    40: "[6,7]",
    41: "[8,9]",
    44: "[5,6]",
    45: "[6,7]",
    46: "[8,9]",
    48: "[14,15]",
    49: "[10,11,12,13,17]",
}


def update_model_solutions(apps, model_solutions_per_level):
    Level = apps.get_model("game", "Level")

    for level_id, model_solution in model_solutions_per_level.items():
        level = Level.objects.get(pk=level_id)
        level.model_solution = model_solution
        level.save()


def update_solutions_to_if_else(apps: Apps, *args):
    update_model_solutions(apps, new_model_solutions_per_level)


def revert_to_old_solutions(apps: Apps, *args):
    update_model_solutions(apps, old_model_solutions_per_level)


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0116_update_worksheet_video_links"),
    ]

    operations = [
        migrations.RunPython(
            code=update_solutions_to_if_else,
            reverse_code=revert_to_old_solutions,
        )
    ]
