# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0062_rm_old_theme_decor_models'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='character_name',
            field=models.CharField(
                    default=None,
                    max_length=20,
                    null=True,
                    blank=True,
                    choices=[('Nigel', 'Nigel'), ('Kirsty', 'Kirsty'), ('Phil', 'Phil'), ('Wes', 'Wes'), ('Van', 'Van'), ('Dee', 'Dee')]),
        ),
    ]
