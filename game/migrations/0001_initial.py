# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('finish_time', models.DateTimeField(auto_now=True)),
                ('score', models.FloatField(default=0)),
                ('workspace', models.TextField(default=b'')),
                ('student', models.ForeignKey(blank=True, to='portal.Student', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('en_face', models.CharField(max_length=500)),
                ('top_down', models.CharField(max_length=500)),
                ('width', models.IntegerField(default=40)),
                ('height', models.IntegerField(default=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=500)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('r_branchiness', models.FloatField(default=0)),
                ('r_loopiness', models.FloatField(default=0)),
                ('r_curviness', models.FloatField(default=0)),
                ('r_num_tiles', models.IntegerField(default=5)),
                ('r_blocklyEnabled', models.BooleanField(default=True)),
                ('r_pythonEnabled', models.BooleanField(default=False)),
                ('r_trafficLights', models.BooleanField(default=False)),
                ('next_episode', models.ForeignKey(default=None, to='game.Episode', null=True)),
                ('r_blocks', models.ManyToManyField(to='game.Block')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('path', models.TextField(max_length=10000)),
                ('decor', models.TextField(default=b'[]', max_length=10000)),
                ('traffic_lights', models.TextField(default=b'[]', max_length=10000)),
                ('origin', models.CharField(default=b'[]', max_length=50)),
                ('destinations', models.CharField(default=b'[[]]', max_length=50)),
                ('default', models.BooleanField(default=False)),
                ('fuel_gauge', models.BooleanField(default=True)),
                ('max_fuel', models.IntegerField(default=50)),
                ('direct_drive', models.BooleanField(default=False)),
                ('model_solution', models.CharField(default=b'[]', max_length=10, blank=True)),
                ('threads', models.IntegerField(default=1)),
                ('blocklyEnabled', models.BooleanField(default=True)),
                ('pythonEnabled', models.BooleanField(default=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('blocks', models.ManyToManyField(to='game.Block')),
                ('character', models.ForeignKey(default=1, to='game.Character')),
                ('next_level', models.ForeignKey(default=None, to='game.Level', null=True)),
                ('owner', models.ForeignKey(blank=True, to='portal.UserProfile', null=True)),
                ('shared_with', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='episode',
            name='first_level',
            field=models.ForeignKey(to='game.Level'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='level',
            field=models.ForeignKey(to='game.Level'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='LevelDecor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('decorName', models.CharField(default=b'tree1', max_length=100)),
                ('level', models.ForeignKey(to='game.Level')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('background', models.CharField(default=b'#eff8ff', max_length=7)),
                ('border', models.CharField(default=b'#bce369', max_length=7)),
                ('selected', models.CharField(default=b'#70961f', max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='level',
            name='theme',
            field=models.ForeignKey(default=None, blank=True, to='game.Theme', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='decor',
            name='theme',
            field=models.ForeignKey(to='game.Theme'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('contents', models.TextField(default=b'')),
                ('owner', models.ForeignKey(blank=True, to='portal.UserProfile', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
