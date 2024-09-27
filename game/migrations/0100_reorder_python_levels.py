from django.apps.registry import Apps
from django.db import migrations
from django.db.models import F, IntegerField, CharField
from django.db.models.functions import Cast


def adjust_python_den_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)

    episode12.next_episode = episode14
    episode14.next_episode = episode13
    episode13.next_episode = Episode.objects.get(pk=20)

    episode12.in_development = False
    episode13.in_development = False
    episode14.in_development = False
    episode15.in_development = False

    episode12.save()
    episode13.save()
    episode14.save()
    episode15.save()

    Level.objects.filter(default=True, name__in=range(1014, 1026)).update(
        episode=episode14
    )
    Level.objects.filter(default=True, name__in=range(1026, 1041)).update(
        episode=episode13
    )


def undo_adjust_python_den_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)

    episode12.next_episode = episode13
    episode13.next_episode = episode14
    episode14.next_episode = Episode.objects.get(pk=20)

    episode12.in_development = True
    episode13.in_development = True
    episode14.in_development = True
    episode15.in_development = True

    episode12.save()
    episode13.save()
    episode14.save()
    episode15.save()

    Level.objects.filter(default=True, name__in=range(1014, 1026)).update(
        episode=episode13
    )
    Level.objects.filter(default=True, name__in=range(1026, 1041)).update(
        episode=episode14
    )


def rename_episode_12_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(default=True, name__in=range(110, 123)).update(
        name=Cast(
            Cast(F("name"), output_field=IntegerField()) + 891,
            output_field=CharField()
        )
    )


def undo_rename_episode_12_levels(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    Level.objects.filter(default=True, name__in=range(1001, 1014)).update(
        name=Cast(
            Cast(F("name"), output_field=IntegerField()) - 891,
            output_field=CharField()
        )
    )


def set_level_order(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level79 = Level.objects.get(name="79", default=True)
    level79.next_level = None
    level79.save()

    level109 = Level.objects.get(name="109", default=True)
    level109.next_level = None
    level109.save()

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = Level.objects.get(name="1014", default=True)
    level1013.save()

    level1040 = Level.objects.get(default=True, name="1040")
    level1040.next_level = None
    level1040.save()


def reset_level_order(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level79 = Level.objects.get(name="79", default=True)
    level79.next_level = Level.objects.get(name="80", default=True)
    level79.save()

    level109 = Level.objects.get(name="109", default=True)
    level109.next_level = Level.objects.get(name="1001", default=True)
    level109.save()

    level1013 = Level.objects.get(name="1013", default=True)
    level1013.next_level = None
    level1013.save()

    level1040 = Level.objects.get(default=True, name="1040")
    level1040.next_level = Level.objects.get(default=True, name="1041")
    level1040.save()


def update_level_score_fields(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level1001 = Level.objects.get(name="1001", default=True)
    level1001.disable_algorithm_score = False
    level1001.model_solution = "[5]"
    level1001.save()

    level1002 = Level.objects.get(name="1002", default=True)
    level1002.disable_algorithm_score = False
    level1002.model_solution = "[10]"
    level1002.save()


def revert_level_score_fields(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level1001 = Level.objects.get(name="1001", default=True)
    level1001.disable_algorithm_score = True
    level1001.model_solution = ""
    level1001.save()

    level1002 = Level.objects.get(name="1002", default=True)
    level1002.disable_algorithm_score = True
    level1002.model_solution = ""
    level1002.save()


class Migration(migrations.Migration):

    dependencies = [("game", "0099_python_episodes_links")]

    operations = [
        migrations.RunPython(
            code=adjust_python_den_episodes,
            reverse_code=undo_adjust_python_den_episodes,
        ),
        migrations.RunPython(
            code=rename_episode_12_levels,
            reverse_code=undo_rename_episode_12_levels,
        ),
        migrations.RunPython(
            code=set_level_order, reverse_code=reset_level_order
        ),
        migrations.RunPython(
            code=update_level_score_fields,
            reverse_code=revert_level_score_fields,
        ),
    ]
