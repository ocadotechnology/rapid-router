from django.apps.registry import Apps
from django.db import migrations


def set_level_order(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = Level.objects.get(name="1014", default=True)
    level1013.save()


class Migration(migrations.Migration):

    dependencies = [("game", "0120_delete_attempt")]

    operations = [
        migrations.RunPython(
            code=set_level_order, reverse_code=migrations.RunPython.noop
        ),
    ]
