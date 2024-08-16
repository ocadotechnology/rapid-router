from django.apps.registry import Apps
from django.db import migrations, models

def adjust_python_den_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)

    episode12.next_episode = episode14
    episode14.next_episode = episode13
    episode13.next_episode = Episode.objects.get(pk=20)

    episode12.in_development = False
    episode13.in_development = False
    episode14.in_development = False

    episode12.save()
    episode13.save()
    episode14.save()

    for level in Level.objects.filter(name__in=range(1014, 1026)):
        level.episode = episode14
        level.save()

    for level in Level.objects.filter(name__in=range(1026, 1042)):
        level.episode = episode13
        level.save()


def undo_adjust_python_den_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)

    episode12.next_episode = episode13
    episode13.next_episode = episode14
    episode14.next_episode = Episode.objects.get(pk=20)

    episode12.in_development = True
    episode13.in_development = True
    episode14.in_development = True

    episode12.save()
    episode13.save()
    episode14.save()

    for level in Level.objects.filter(name__in=range(1014, 1026)):
        level.episode = episode13
        level.save()

    for level in Level.objects.filter(name__in=range(1026, 1042)):
        level.episode = episode14
        level.save()


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
    

def set_level_order(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level79 = Level.objects.get(name="79", default=True)
    level79.next_level = None

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = Level.objects.get(name="1014", default=True)


def reset_level_order(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level79 = Level.objects.get(name="79", default=True)
    level79.next_level = Level.objects.get(name="80", default=True)

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = None


def delete_old_python_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    Episode.objects.get(pk=10).delete()
    Episode.objects.get(pk=11).delete()


def add_back_old_python(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    level80 = Level.objects.get(name="80", default=True)
    level92 = Level.objects.get(name="92", default=True)

    episode10 = Episode(
        name="Introduction to Python",
        first_level=level80,
        r_branchiness=0.5,
        r_loopiness=0.1,
        r_num_tiles=35,
        r_curviness=0.2,
        r_pythonEnabled=0,
        r_blocklyEnabled=1,
        r_trafficLights=1,
        in_development=False,
    )

    episode11 = Episode(
        name="Python",
        first_level=level92,
        r_branchiness=0.5,
        r_loopiness=0.1,
        r_num_tiles=35,
        r_curviness=0.2,
        r_pythonEnabled=0,
        r_blocklyEnabled=1,
        r_trafficLights=1,
        in_development=False,
    )

    episode10.save()
    episode11.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0098_add_episode_resource_link_fields'),
    ]

    operations = [
        migrations.RunPython(
            code=adjust_python_den_episodes,
            reverse_code=undo_adjust_python_den_episodes
        ),
        migrations.RunPython(
            code=rename_episode_12_levels,
            reverse_code=undo_rename_episode_12_levels
        ),
        migrations.RunPython(
            code=set_level_order,
            reverse_code=reset_level_order
        )
    ]