from django.db import migrations


def update_level(apps, schema_editor):
    Level = apps.get_model("game", "Level")
    level70 = Level.objects.get(name="70", default=1)
    level70.traffic_lights = (
        '[{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":4},"direction":"N","startTime":0,"startingState":"GREEN"},'
        '{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":4,"y":2},"direction":"S","startTime":0,"startingState":"GREEN"},'
        '{"redDuration":1,"greenDuration":2,"sourceCoordinate":{"x":4,"y":3},"direction":"E","startTime":0,"startingState":"RED"},'
        '{"redDuration":3,"greenDuration":3,"sourceCoordinate":{"x":2,"y":3},"direction":"E","startTime":0,"startingState":"RED"}]'
    )
    level70.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0046_set_img_order")]

    operations = [migrations.RunPython(update_level)]
