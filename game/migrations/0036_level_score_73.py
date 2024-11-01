from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level73 = Level.objects.get(name="73", default=1)
    level73.model_solution = "[12]"
    level73.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0035_disable_route_score_level_70")]

    operations = [migrations.RunPython(update_level)]
