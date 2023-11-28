from django.db import migrations


def add_new_blocks(apps, schema_editor):
    Block = apps.get_model("game", "Block")

    VARIABLE = 5
    MATH = 6

    block1 = Block(type="variables_set", block_type=VARIABLE)
    block2 = Block(type="variables_numeric_set", block_type=VARIABLE)
    block3 = Block(type="variables_increment", block_type=VARIABLE)
    block4 = Block(type="variables_get", block_type=VARIABLE)
    block5 = Block(type="math_number", block_type=MATH)
    block6 = Block(type="math_arithmetic", block_type=MATH)
    block7 = Block(type="logic_compare", block_type=MATH)

    block1.save()
    block2.save()
    block3.save()
    block4.save()
    block5.save()
    block6.save()
    block7.save()


def remove_new_blocks(apps, schema_editor):
    Block = apps.get_model("game", "Block")

    block1 = Block.objects.get(type="variables_set")
    block2 = Block.objects.get(type="variables_numeric_set")
    block3 = Block.objects.get(type="variables_increment")
    block4 = Block.objects.get(type="variables_get")
    block5 = Block.objects.get(type="math_number")
    block6 = Block.objects.get(type="math_arithmetic")
    block7 = Block.objects.get(type="logic_compare")

    block1.delete()
    block2.delete()
    block3.delete()
    block4.delete()
    block5.delete()
    block6.delete()
    block7.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("game", "0084_alter_block_block_type"),
    ]

    operations = [migrations.RunPython(add_new_blocks, reverse_code=remove_new_blocks)]
