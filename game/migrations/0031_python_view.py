from django.db import migrations
from game.models import Episode


def set_python_view(apps, schema_editor):
    for level in Episode.objects.get(id=10).levels:
        level.pythonEnabled = False
        level.pythonViewEnabled = True
        level.blocklyEnabled = True
        level.save()


class Migration(migrations.Migration):
    dependencies = [
        ('game', '0030_merge'),
    ]

    operations = [
        migrations.RunPython(set_python_view)
    ]
