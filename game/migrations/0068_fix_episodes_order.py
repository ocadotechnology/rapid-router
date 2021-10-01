from django.db import migrations


def update_episodes(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    episode7_levels = list(Level.objects.filter(name__range=(51, 60)))
    del episode7_levels[0]
    episode8_levels = list(Level.objects.filter(name__range=(61, 67)))

    Episode = apps.get_model("game", "Episode")
    episode6 = Episode.objects.get(id=6)
    episode7 = Episode.objects.get(id=7)
    episode8 = Episode.objects.get(id=8)
    episode9 = Episode.objects.get(id=9)

    episode7.name = "Limited Blocks"
    episode8.name = "Procedures"

    episode7.save()
    episode8.save()

    episode6.next_episode = episode7
    episode7.next_episode = episode8
    episode8.next_episode = episode9

    episode6.save()
    episode7.save()
    episode8.save()

    episode7.level_set.set(episode7_levels)
    episode8.level_set.set(episode8_levels)

    episode7.save()
    episode8.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0067_level_score_27")]

    operations = [
        migrations.RunPython(update_episodes, reverse_code=migrations.RunPython.noop)
    ]
