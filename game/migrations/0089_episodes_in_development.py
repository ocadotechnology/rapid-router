from django.apps.registry import Apps
from django.db import migrations


def mark_episodes_in_development(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    for i in range(13, 16):
        episode = Episode.objects.get(pk=i)
        episode.in_development = True
        episode.save()


def unmark_episodes_in_development(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    for i in range(13, 16):
        episode = Episode.objects.get(pk=i)
        episode.in_development = False
        episode.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0088_rename_episodes")]
    operations = [
        migrations.RunPython(
            mark_episodes_in_development,
            reverse_code=unmark_episodes_in_development,
        )
    ]
