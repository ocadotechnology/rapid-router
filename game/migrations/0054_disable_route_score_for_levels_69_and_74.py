from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level69 = Level.objects.get(name="69", default=1)
    level69.disable_route_score = True
    level69.save()

    level74 = Level.objects.get(name="74", default=1)
    level74.disable_route_score = True
    level74.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0053_level_70_is_unsolveable_again")]

    operations = [migrations.RunPython(update_level)]
