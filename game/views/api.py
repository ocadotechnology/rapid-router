from django.http import HttpResponse
from game.models import Level, Episode, LevelBlock, Block, Theme, Character, Decor
from game.serializers import LevelListSerializer, EpisodeListSerializer, LevelDetailSerializer, EpisodeDetailSerializer, \
    LevelBlockSerializer, BlockSerializer, ThemeSerializer, CharacterSerializer, DecorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import generics


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'blocks': reverse('block-list', request=request, format=format),
        'characters': reverse('character-list', request=request, format=format),
        'episodes': reverse('episode-list', request=request, format=format),
        'levels': reverse('level-list', request=request, format=format),
        'themes': reverse('theme-list', request=request, format=format),
    })


@api_view(('GET',))
def decor_list(request, format=None):
    decors = Decor.objects.all()
    serializer = DecorSerializer(decors, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def decor_detail(request, pk, format=None):
    try:
        decor = Decor.objects.get(pk=pk)
    except Decor.DoesNotExist:
        return HttpResponse(status=404)

    serializer = DecorSerializer(decor, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def level_list(request, format=None):
    levels = Level.objects.all()
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

    print repr(EpisodeDetailSerializer)
    serializer = LevelDetailSerializer(level, context={'request': request})
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
    themes = Theme.objects.all()
    serializer = ThemeSerializer(themes, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def theme_detail(request, pk, format=None):
    try:
        theme = Theme.objects.get(pk=pk)
    except Theme.DoesNotExist:
        return HttpResponse(status=404)

    serializer = ThemeSerializer(theme, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def character_list(request, format=None):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def character_detail(request, pk, format=None):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return HttpResponse(status=404)

    serializer = CharacterSerializer(character, context={'request': request})
    return Response(serializer.data)


# Maybe used later for when we use a viewset which requires multiple serializer
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
        }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])
