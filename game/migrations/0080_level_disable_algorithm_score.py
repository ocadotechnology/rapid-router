# Generated by Django 3.2.16 on 2023-01-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0079_populate_block_type_add_cow_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='disable_algorithm_score',
            field=models.BooleanField(default=False),
        ),
    ]
