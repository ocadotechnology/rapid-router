from django.db import migrations


def update_level(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    level43 = Level.objects.get(name="43", default=1)
    level43.model_solution = "[9]"
    level43.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0081_first_12_levels_no_algo_score")]
    operations = [
        migrations.RunPython(update_level, reverse_code=migrations.RunPython.noop)
    ]
