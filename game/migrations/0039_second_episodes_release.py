from django.db import migrations


def release_levels(apps, schema_editor):
    Episode = apps.get_model("game", "Episode")
    for episode in Episode.objects.all():
        episode.in_development = False
        episode.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0038_level_score_40")]

    operations = [migrations.RunPython(release_levels)]
