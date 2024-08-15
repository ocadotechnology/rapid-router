from django.apps.registry import Apps
from django.db import migrations, models

def rename_episode_12_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    new_name = 1001

    for i in range(110, 123):
        level = Level.objects.get(name=i, default=True)
        level.name = str(new_name)
        level.save()
        new_name += 1


def undo_rename_episode_12_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    new_name = 110
    for i in range(1001, 1014):
        level = Level.objects.get(name=i, default=True)
        level.name = str(new_name)
        level.save()
        new_name += 1


def delete_old_python_levels(apps: Apps, *args):



def add_back_old_python_levels(apps: Apps, *args):
    


def set_order_of_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level79 = Level.objects.get(name="79", default=True)
    level79.next_level = None

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = Level.objects.get(name="1014", default=True)


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0098_add_episode_resource_link_fields'),
    ]

    operations = [
        migrations.RunPython(
            code=rename_episode_12_levels,
            reverse_code=undo_rename_episode_12_levels
        )
    ]