from django.db import migrations


def disable_route_score(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level70 = Level.objects.get(name="70", default=1)
    level70.disable_route_score = True
    level70.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0034_joes_level")]

    operations = [migrations.RunPython(disable_route_score)]
