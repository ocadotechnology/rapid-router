# Generated by Django 3.2.25 on 2024-10-15 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0103_level_1015_solution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='direct_drive',
        ),
    ]