from django.apps.registry import Apps
from django.db import migrations

def update_python_den_level_41(apps: Apps, *args):
    Level = apps.get_model("game", "Level")

    level41 = Level.objects.get(default=True, name="1041")
    level41.next_level = None
    level41.save()

def revert_python_den_level_41(apps: Apps, *args):
    Level = apps.get_model("game", "Level")
    
    level41 = Level.objects.get(default=True, name="1041")
    level41.next_level = Level.objects.get(default=True, name="1042")
    level41.save()

class Migration(migrations.Migration):
    dependencies = [("game", "0100_reorder_python_levels")]

    operations = [
        migrations.RunPython(
            code=update_python_den_level_41,
            reverse_code=revert_python_den_level_41
        )
    ]