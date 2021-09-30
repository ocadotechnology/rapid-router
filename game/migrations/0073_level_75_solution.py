from django.db import migrations


def update_level(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    level75 = Level.objects.get(name="75", default=1)
    level75.model_solution = "[9]"
    level75.save()


def dummy_reverse(apps, schema_editor):
    """It's not possible to reverse this data migration
    but we want to allow Django to reverse previous migrations.
    """
    pass


class Migration(migrations.Migration):
    dependencies = [("game", "0072_level_50_solution")]
    operations = [migrations.RunPython(update_level, reverse_code=dummy_reverse)]
