from django.apps.registry import Apps
from django.db import migrations


def swap_episodes_13_14(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode20 = Episode.objects.get(pk=20)

    episode13_levels = Level.objects.filter(
        default=True, name__in=range(1026, 1041)
    )
    episode14_levels = Level.objects.filter(
        default=True, name__in=range(1014, 1026)
    )

    episode13_levels.update(episode=episode14)
    episode14_levels.update(episode=episode13)

    old_episode13_name = episode13.name
    old_episode13_lesson_plan_link = episode13.lesson_plan_link
    old_episode13_slides_link = episode13.slides_link
    old_episode13_worksheet_link = episode13.worksheet_link
    old_episode13_video_link = episode13.video_link
    old_episode14_name = episode14.name
    old_episode14_lesson_plan_link = episode14.lesson_plan_link
    old_episode14_slides_link = episode14.slides_link
    old_episode14_worksheet_link = episode14.worksheet_link
    old_episode14_video_link = episode14.video_link

    episode13.name = old_episode14_name
    episode13.lesson_plan_link = old_episode14_lesson_plan_link
    episode13.slides_link = old_episode14_slides_link
    episode13.worksheet_link = old_episode14_worksheet_link
    episode13.video_link = old_episode14_video_link
    episode14.name = old_episode13_name
    episode14.lesson_plan_link = old_episode13_lesson_plan_link
    episode14.slides_link = old_episode13_slides_link
    episode14.worksheet_link = old_episode13_worksheet_link
    episode14.video_link = old_episode13_video_link

    episode12.next_episode = episode13
    episode13.next_episode = episode14
    episode14.next_episode = episode20

    episode12.save()
    episode13.save()
    episode14.save()

    episode12_last_level = episode12.level_set.first()
    episode13_last_level = episode13.level_set.last()
    episode14_last_level = episode14.level_set.last()

    episode12_last_level.next_level = episode13.level_set.all()[0]
    episode13_last_level.next_level = episode14.level_set.all()[0]
    episode14_last_level.next_level = None

    episode12_last_level.save()
    episode13_last_level.save()
    episode14_last_level.save()


def unswap_episodes_13_14(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode12 = Episode.objects.get(pk=12)
    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode20 = Episode.objects.get(pk=20)

    episode13_levels = Level.objects.filter(
        default=True, name__in=range(1014, 1026)
    )
    episode14_levels = Level.objects.filter(
        default=True, name__in=range(1026, 1041)
    )

    episode13_levels.update(episode=episode14)
    episode14_levels.update(episode=episode13)

    old_episode13_name = episode13.name
    old_episode13_lesson_plan_link = episode13.lesson_plan_link
    old_episode13_slides_link = episode13.slides_link
    old_episode13_worksheet_link = episode13.worksheet_link
    old_episode13_video_link = episode13.video_link
    old_episode14_name = episode14.name
    old_episode14_lesson_plan_link = episode14.lesson_plan_link
    old_episode14_slides_link = episode14.slides_link
    old_episode14_worksheet_link = episode14.worksheet_link
    old_episode14_video_link = episode14.video_link

    episode13.name = old_episode14_name
    episode13.lesson_plan_link = old_episode14_lesson_plan_link
    episode13.slides_link = old_episode14_slides_link
    episode13.worksheet_link = old_episode14_worksheet_link
    episode13.video_link = old_episode14_video_link
    episode14.name = old_episode13_name
    episode14.lesson_plan_link = old_episode13_lesson_plan_link
    episode14.slides_link = old_episode13_slides_link
    episode14.worksheet_link = old_episode13_worksheet_link
    episode14.video_link = old_episode13_video_link

    episode12.next_episode = episode14
    episode14.next_episode = episode13
    episode13.next_episode = episode20

    episode12.save()
    episode13.save()
    episode14.save()

    episode12_last_level = episode12.level_set.first()
    episode13_last_level = episode13.level_set.last()
    episode14_last_level = episode14.level_set.last()

    episode12_last_level.next_level = episode14.level_set.all()[0]
    episode14_last_level.next_level = episode13.level_set.all()[0]
    episode13_last_level.next_level = None

    episode12_last_level.save()
    episode13_last_level.save()
    episode14_last_level.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0101_rename_episodes")]

    operations = [
        migrations.RunPython(
            code=swap_episodes_13_14, reverse_code=unswap_episodes_13_14
        )
    ]
