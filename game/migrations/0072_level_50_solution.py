from django.db import migrations


def update_level(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    level50 = Level.objects.get(name="50", default=1)
    level50.model_solution = "[11]"
    level50.destinations = "[[7,4]]"
    level50.save()


def dummy_reverse(apps, schema_editor):
    """It's not possible to reverse this data migration
    but we want to allow Django to reverse previous migrations.
    """
    pass


class Migration(migrations.Migration):
    dependencies = [("game", "0071_use_common_models")]
    operations = [migrations.RunPython(update_level, reverse_code=dummy_reverse)]
