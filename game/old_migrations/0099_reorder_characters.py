# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def level_27_character(apps, schema_editor):

    Character = apps.get_model('game', 'Character')
    Level = apps.get_model('game', 'Level')

    Dee = Character.objects.get(name='Dee')
    level27 = Level.objects.get(pk=27)
    level27.character = Dee
    level27.save()


def reorder_characters(apps, schema_editor):

    Character = apps.get_model('game', 'Character')

    Character.objects.all().delete()

    van = Character(pk=1, name="Van", en_face='/static/game/image/characters/front_view/Van.svg',
                    top_down='/static/game/image/characters/top_view/Van.svg', height='20',
                    width='40')
    van.save()

    Dee = Character(pk=2, name="Dee", en_face='/static/game/image/characters/front_view/Dee.svg',
                    top_down='/static/game/image/characters/top_view/Dee.svg', height='28',
                    width='52')
    Dee.save()

    Nigel = Character(pk=3, name="Nigel", width='56', height='32',
                      en_face='/static/game/image/characters/front_view/Nigel.svg',
                      top_down='/static/game/image/characters/top_view/Nigel.svg')
    Nigel.save()

    Kirsty = Character(pk=4, name="Van", height='32', width='60',
                       en_face='/static/game/image/characters/front_view/Kirsty.svg',
                       top_down='/static/game/image/characters/top_view/Kirsty.svg')
    Kirsty.save()

    Wes = Character(pk=5, name="Wes", en_face='/static/game/image/characters/front_view/Wes.svg',
                    top_down='/static/game/image/characters/top_view/Wes.svg', height='20',
                    width='40')
    Wes.save()

    Phil = Character(pk=6, name="Phil", height='32', width='60',
                     en_face='/static/game/image/characters/front_view/Van.svg',
                     top_down='/static/game/image/characters/top_view/Van.svg')
    Phil.save()


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0098_episodes_primary_key_fix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='character',
        ),
        migrations.RunPython(reorder_characters),
        migrations.AddField(
            model_name='level',
            name='character',
            field=models.ForeignKey(default=1, to='game.Character'),
            preserve_default=True,
        ),
        migrations.RunPython(level_27_character)
    ]
