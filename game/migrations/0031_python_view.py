from django.db import migrations


def set_python_view(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    levels = [63, 64, 65, 66, 67, 68, 69, 93, 94, 95, 96, 97]
    for level_id in levels:
        level = Level.objects.get(pk=level_id)
        level.pythonEnabled = False
        level.pythonViewEnabled = True
        level.blocklyEnabled = True
        level.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0030_merge")]

    operations = [migrations.RunPython(set_python_view)]
