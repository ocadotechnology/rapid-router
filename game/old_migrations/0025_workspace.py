# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0024_auto_20140711_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('workspace', models.TextField(default=b'')),
                ('owner', models.ForeignKey(to='game.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
