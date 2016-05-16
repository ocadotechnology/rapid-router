# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from game import messages
from game.messages import description_level_default, hint_level_default
from game.theme import get_theme, get_themes_url
from rest_framework import serializers
from models import Workspace, Level, Episode, LevelDecor, LevelBlock, Block, Character


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelListSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ('url', '__unicode__', 'episode', 'name', 'title', 'default', 'blocklyEnabled', 'pythonEnabled')

    def get_title(self, obj):
        if obj.default:
            title = getattr(messages, 'title_level' + obj.name)()
            return title
        else:
            return "Custom Level"


class LevelDetailSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    hint = serializers.SerializerMethodField()
    levelblock_set = serializers.HyperlinkedIdentityField(
        view_name='levelblock-for-level',
        read_only=True
    )
    map = serializers.HyperlinkedIdentityField(
        view_name='map-for-level',
        read_only=True
    )
    mode = serializers.HyperlinkedIdentityField(
        view_name='mode-for-level',
        read_only=True
    )

    class Meta:
        model = Level
        fields = ('__unicode__', 'episode', 'name', 'title', 'description', 'hint', 'next_level', 'default',
                  'levelblock_set', 'map', 'mode', 'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled')

    def get_title(self, obj):
        if obj.default:
            title = getattr(messages, 'title_level' + obj.name)()
            return title
        else:
            return "Custom Level"

    def get_description(self, obj):
        if obj.default:
            description = getattr(messages, 'description_level' + obj.name)()
            return description
        else:
            return description_level_default()

    def get_hint(self, obj):
        if obj.default:
            hint = getattr(messages, 'hint_level' + obj.name)()
            return hint
        else:
            return hint_level_default()

    def get_leveldecor_set(self, obj):
        leveldecors = LevelDecor.objects.filter(level__id=obj.id)
        serializer = LevelDecorSerializer(leveldecors, many=True, context={'request': self.context.get('request', None)})
        return serializer.data


class LevelModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled')


class LevelMapListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='map-for-level',
        read_only=True
    )

    class Meta:
        model = Level
        fields = ('url',)


class LevelMapDetailSerializer(serializers.HyperlinkedModelSerializer):
    leveldecor_set = serializers.SerializerMethodField()
    theme = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ('origin', 'destinations', 'path', 'traffic_lights', 'max_fuel', 'theme', 'leveldecor_set')

    def get_leveldecor_set(self, obj):
        leveldecors = LevelDecor.objects.filter(level__id=obj.id)
        serializer = LevelDecorSerializer(leveldecors, many=True, context={'request': self.context.get('request', None)})
        return serializer.data

    def get_theme(self, obj):
        pk = get_theme(obj.theme_name).pk
        return get_themes_url(pk, self.context.get('request', None))


class EpisodeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name')


class EpisodeDetailSerializer(serializers.HyperlinkedModelSerializer):
    level_set = serializers.SerializerMethodField()
    level_set_url = serializers.HyperlinkedIdentityField(view_name='level-for-episode',
                                                          read_only=True)

    class Meta:
        model = Episode
        depth = 1
        fields = ('url', '__unicode__', 'name', 'level_set', 'level_set_url')

    def get_level_set(self, obj):
        levels = Level.objects.filter(episode__id=obj.id)
        serializer = LevelListSerializer(levels, many=True, context={'request': self.context.get('request', None)})
        return serializer.data


class LevelBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelBlock


class LevelDecorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelDecor


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('url', 'id', 'type')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
