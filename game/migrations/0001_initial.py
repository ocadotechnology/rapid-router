# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
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
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': b'classes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step', models.IntegerField()),
                ('command', models.CharField(default=b'Forward', max_length=15, choices=[(b'Right', b'right'), (b'Left', b'left'), (b'Forward', b'forward'), (b'TurnAround', b'turn around'), (b'While', b'while'), (b'If', b'if')])),
                ('next', models.IntegerField(null=True, blank=True)),
                ('condition', models.CharField(max_length=400, blank=True)),
                ('executedBlock1', models.CommaSeparatedIntegerField(max_length=100, blank=True)),
                ('executedBlock2', models.CommaSeparatedIntegerField(max_length=100, blank=True)),
                ('attempt', models.ForeignKey(to='game.Attempt')),
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
                ('next_episode', models.ForeignKey(default=None, to='game.Episode', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'100')),
                ('path', models.CharField(max_length=10000)),
                ('decor', models.CharField(default=b'[]', max_length=10000)),
                ('destination', models.CharField(max_length=10)),
                ('default', models.BooleanField(default=False)),
                ('block_limit', models.IntegerField(null=True, blank=True)),
                ('max_fuel', models.IntegerField(default=50)),
                ('blocks', models.ManyToManyField(to='game.Block')),
                ('next_level', models.ForeignKey(default=None, to='game.Level', null=True)),
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
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.ForeignKey(to='game.School'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('class_field', models.ForeignKey(to='game.Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='guardian',
            name='children',
            field=models.ManyToManyField(to='game.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attempt',
            name='student',
            field=models.ForeignKey(to='game.Student'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='game.Teacher'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(default=b'static/game/image/avatars/default-avatar.jpeg', null=True, upload_to=b'static/game/image/avatars/', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(to='game.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(to='game.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='owner',
            field=models.ForeignKey(blank=True, to='game.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='guardian',
            name='user',
            field=models.OneToOneField(to='game.UserProfile'),
            preserve_default=True,
        ),
    ]
