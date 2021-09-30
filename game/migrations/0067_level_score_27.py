from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level27 = Level.objects.get(name="27", default=1)
    level27.model_solution = "[13]"
    level27.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0066_rm_character_model")]

    operations = [migrations.RunPython(update_level)]
