from django.apps.registry import Apps
from django.db import migrations


def rename_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    def update_episode_name(pk: int, name: str):
        episode = Episode.objects.get(pk=pk)
        episode.name = name
        episode.save()

    update_episode_name(pk=12, name="Counted Loops Using While")
    update_episode_name(pk=13, name="Indeterminate While Loops - coming soon")


def undo_rename_episodes(apps: Apps, *args):
    Episode = apps.get_model("game", "Episode")

    def update_episode_name(pk: int, name: str):
        episode = Episode.objects.get(pk=pk)
        episode.name = name
        episode.save()

    update_episode_name(pk=12, name="Sequencing and Counted Loops")
    update_episode_name(pk=13, name="Indeterminate WHILE Loops - coming soon")

class Migration(migrations.Migration):
    dependencies = [("game", "0087_workspace_python_view_enabled")]
    operations = [
        migrations.RunPython(
            rename_episodes,
            reverse_code=undo_rename_episodes,
        )
    ]
