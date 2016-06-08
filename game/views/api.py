# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2016, Ocado Innovation Limited
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
from django.http import HttpResponse
from game.models import Level, Episode, LevelBlock, Block, LevelDecor
from game.serializers import LevelListSerializer, EpisodeListSerializer, LevelDetailSerializer, EpisodeDetailSerializer, \
    LevelBlockSerializer, BlockSerializer, LevelMapDetailSerializer, \
    LevelDecorSerializer, LevelModeSerializer, LevelMapListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

from game.decor import get_all_decor, get_decor_element_by_pk, get_decors_url
from game.theme import get_all_themes, get_theme_by_pk, get_themes_url
from game.character import get_all_character, get_character_by_pk, get_characters_url


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'blocks': reverse('block-list', request=request, format=format),
        'characters': reverse('character-list', request=request, format=format),
        'decors': reverse('decor-list', request=request, format=format),
        'episodes': reverse('episode-list', request=request, format=format),
        'levels': reverse('level-list', request=request, format=format),
        'maps': reverse('map-list', request=request, format=format),
        'themes': reverse('theme-list', request=request, format=format),
    })


@api_view(('GET',))
def decor_list(request, format=None):
    decors = get_all_decor()
    data = [{get_decors_url(i.pk, request)} for i in decors]
    return Response(data)


@api_view(('GET',))
def decor_detail(request, pk, format=None):
    try:
        decor = get_decor_element_by_pk(pk=pk)
    except KeyError:
        return HttpResponse(status=404)
    data = decor.__dict__.copy()
    data['theme'] = get_themes_url(data['theme'].pk, request)
    return Response(data)


@api_view(('GET',))
def level_list(request, format=None):
    levels = Level.objects.sorted_levels()
    serializer = LevelListSerializer(levels, many=True, context={'request': request})
    return Response(serializer.data)


# pk is the episode id
@api_view(('GET',))
def level_for_episode(request, pk, format=None):
    levels = Level.objects.filter(episode__id=pk)
    serializer = LevelListSerializer(levels, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def level_detail(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelDetailSerializer(level, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def map_list(request, format=None):
    levels = Level.objects.sorted_levels()

    serializer = LevelMapListSerializer(levels, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def map_for_level(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelMapDetailSerializer(level, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def mode_for_level(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelModeSerializer(level, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def episode_list(request, format=None):
    episodes = Episode.objects.all()
    serializer = EpisodeListSerializer(episodes, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def episode_detail(request, pk, format=None):
    try:
        episode = Episode.objects.get(pk=pk)
    except Episode.DoesNotExist:
        return HttpResponse(status=404)

    serializer = EpisodeDetailSerializer(episode, context={'request': request})
    return Response(serializer.data)

@api_view(('GET',))
def levelblock_list(request, level, format=None):
    blocks = LevelBlock.objects.filter(level__id=level)

    serializer = LevelBlockSerializer(blocks, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def levelblock_for_level(request, pk, format=None):
    levelblocks = LevelBlock.objects.filter(level__id=pk)
    serializer = LevelBlockSerializer(levelblocks, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def levelblock_detail(request, pk, format=None):
    try:
        levelblock = LevelBlock.objects.get(pk=pk)
    except LevelBlock.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelBlockSerializer(levelblock, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def leveldecor_list(request, level, format=None):
    leveldecors = LevelDecor.objects.filter(level__id=level)

    serializer = LevelDecorSerializer(leveldecors, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def leveldecor_for_level(request, pk, format=None):
    leveldecors = LevelDecor.objects.filter(level__id=pk)
    serializer = LevelDecorSerializer(leveldecors, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def leveldecor_detail(request, pk, format=None):
    try:
        leveldecor = LevelDecor.objects.get(pk=pk)
    except LevelDecor.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelDecorSerializer(leveldecor, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def block_list(request, format=None):
    block = Block.objects.all()
    serializer = BlockSerializer(block, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def block_detail(request, pk, format=None):
    try:
        block = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return HttpResponse(status=404)

    serializer = BlockSerializer(block, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def theme_list(request, format=None):
    themes = get_all_themes()
    data = [{get_themes_url(i.pk, request)} for i in themes]
    return Response(data)


@api_view(('GET',))
def theme_detail(request, pk, format=None):
    try:
        theme = get_theme_by_pk(pk)
    except KeyError:
        return HttpResponse(status=404)
    return Response(theme.__dict__)


@api_view(('GET',))
def character_list(request, format=None):
    characters = get_all_character()
    data = [{get_characters_url(i.pk, request)} for i in characters]
    return Response(data)


@api_view(('GET',))
def character_detail(request, pk, format=None):
    try:
        character = get_character_by_pk(pk)
    except KeyError:
        return HttpResponse(status=404)
    return Response(character.__dict__)


# Maybe used later for when we use a viewset which requires multiple serializer
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
        }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])
