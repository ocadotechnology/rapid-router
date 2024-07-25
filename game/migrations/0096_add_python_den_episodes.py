from django.apps.registry import Apps
from django.db import migrations, models

# TODO: Need to add first_level values once the levels are sorted out

def add_python_den_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    def update_episode_name(pk: int, name: str):
        episode = Episode.objects.get(pk=pk)
        episode.name = name
        episode.save()

    update_episode_name(10, "Output, Operators and Data")
    update_episode_name(11, "Variables, Input and Casting")
    update_episode_name(12, "Selection")
    update_episode_name(13, "Complex Selection")
    update_episode_name(14, "Counted Loops Using 'While'")
    update_episode_name(15, "Selection in a Loop")

    episode_20 = Episode.objects.create(
        pk=20,
        name="Procedures",
    )

    episode_19 = Episode.objects.create(
        pk=19,
        next_episode = episode_20,
        name="For Loops",
    )

    episode_18 = Episode.objects.create(
        pk=18,
        next_episode = episode_19,
        name="Lists",
    )

    episode_17 = Episode.objects.create(
        pk=17,
        next_episode = episode_18,
        name="String Manipulation",
    )

    episode_16 = Episode.objects.create(
        pk=16,
        next_episode = episode_17,
        name="Indeterminate loops",
    )

def delete_python_den_episodes(apps: Apps, *args):
    update_episode_name(10, "Introduction to Python")
    update_episode_name(11, "Python")
    update_episode_name(12, "Counted Loops Using While")
    update_episode_name(13, "Indeterminate While Loops - coming soon")
    update_episode_name(14, "Selection in a Loop - coming soon")
    update_episode_name(15, "For Loops - coming soon")

    Episode = apps.get_model("game", "Episode")

    Episode.objects.filter(pk__in=range(16, 21)).delete()

class Migration(migrations.Migration):
    dependencies = [("game", "0095_add_python_den_levels")]
    operations = [
        migrations.RunPython(
            add_python_den_episodes,
            reverse_code=delete_python_den_episodes
        )
    ]