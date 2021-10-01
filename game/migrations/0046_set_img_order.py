from django.db import migrations


def update(apps, schema_editor):
    mappings = [
        (13, 0),
        (14, 0),
        (22, 0),
        (23, 0),
        (15, 0),
        (5, 1),
        (11, 1),
        (17, 1),
        (4, 1),
        (10, 1),
        (16, 1),
        (24, 1),
        (6, 2),
        (12, 2),
        (21, 2),
        (28, 2),
        (3, 3),
        (9, 3),
        (18, 3),
        (25, 3),
        (1, 4),
        (7, 4),
        (19, 4),
        (26, 4),
        (2, 4),
        (8, 4),
        (20, 4),
        (27, 4),
    ]
    for mapping in mappings:
        decor = apps.get_model("game", "Decor").objects.get(id=mapping[0])
        decor.z_index = mapping[1]
        decor.save()


class Migration(migrations.Migration):
    dependencies = [("game", "0045_decor_z_index")]

    operations = [migrations.RunPython(update)]
