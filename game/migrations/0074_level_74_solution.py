from django.db import migrations


def update_level(apps, schema_editor):

    Level = apps.get_model("game", "Level")
    level74 = Level.objects.get(name="74", default=1)
    level74.model_solution = "[14]"
    level74.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0073_level_75_solution")]
    operations = [
        migrations.RunPython(update_level, reverse_code=migrations.RunPython.noop)
    ]
