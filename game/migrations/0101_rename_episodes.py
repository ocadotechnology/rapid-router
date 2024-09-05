from django.apps.registry import Apps
from django.db import migrations


def rename_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)

    episode13.name = "Indeterminate Loops"
    episode14.name = "Selection in a Loop"
    episode15.name = "For Loops"

    episode13.save()
    episode14.save()
    episode15.save()


def unrename_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    episode13 = Episode.objects.get(pk=13)
    episode14 = Episode.objects.get(pk=14)
    episode15 = Episode.objects.get(pk=15)

    episode13.name = "Indeterminate While Loops - coming soon"
    episode14.name = "Selection in a Loop - coming soon"
    episode15.name = "For Loops - coming soon"

    episode13.save()
    episode14.save()
    episode15.save()


class Migration(migrations.Migration):

    dependencies = [("game", "0100_reorder_python_levels")]

    operations = [
        migrations.RunPython(
            code=rename_episodes, reverse_code=unrename_episodes
        )
    ]
