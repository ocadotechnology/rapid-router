from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level = Level.objects.get(name="34", default=1)
    level.model_solution = "[8,7,6]"
    level.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0048_add_cow_field_and_blocks")]

    operations = [migrations.RunPython(update_level)]
