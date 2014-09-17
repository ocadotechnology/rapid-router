# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def enable_random_levels_for_episodes(apps, schema_editor):
    Episode = apps.get_model('game', 'Episode')

    for i in range(1,7):
        episode = Episode.objects.get(id=i)
        episode.r_random_levels_enabled = True
        episode.save()

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_sort_scores_and_add_initial_python_episodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='r_random_levels_enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_blocks',
            field=models.ManyToManyField(related_name=b'episodes', null=True, to=b'game.Block'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_branchiness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_curviness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_loopiness',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='r_num_tiles',
            field=models.IntegerField(default=5, null=True),
        ),
        migrations.RunPython(enable_random_levels_for_episodes)
    ]
