from django.db import migrations


def update_episodes_level_order(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")
    Level = apps.get_model("game", "Level")

    episode7 = Episode.objects.get(id=7)
    episode8 = Episode.objects.get(id=8)

    episode7_new_levels = Level.objects.filter(episode=episode7, owner=None)
    episode8_new_levels = Level.objects.filter(episode=episode8, owner=None)

    episode7.level_set.set(episode7_new_levels)
    episode8.level_set.set(episode8_new_levels)

    episode7.save()
    episode8.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0068_fix_episodes_order")]

    operations = [
        migrations.RunPython(
            update_episodes_level_order, reverse_code=migrations.RunPython.noop
        )
    ]
