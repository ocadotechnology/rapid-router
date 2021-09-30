from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy

from game.character import get_all_character, get_character_by_pk, get_characters_url
from game.decor import get_all_decor, get_decor_element_by_pk, get_decors_url
from game.models import Level, Episode, LevelBlock, Block, LevelDecor
from game.serializers import (
    LevelListSerializer,
    EpisodeListSerializer,
    LevelDetailSerializer,
    EpisodeDetailSerializer,
    LevelBlockSerializer,
    BlockSerializer,
    LevelMapDetailSerializer,
    LevelDecorSerializer,
    LevelModeSerializer,
    LevelMapListSerializer,
)
from game.theme import get_all_themes, get_theme_by_pk, get_themes_url


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def api_root(request, format=None):
    return Response(
        {
            "blocks": reverse("block-list", request=request, format=format),
            "characters": reverse("character-list", request=request, format=format),
            "decors": reverse("decor-list", request=request, format=format),
            "episodes": reverse("episode-list", request=request, format=format),
            "levels": reverse("level-list", request=request, format=format),
            "maps": reverse("map-list", request=request, format=format),
            "themes": reverse("theme-list", request=request, format=format),
        }
    )


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def decor_list(request, format=None):
    decors = get_all_decor()
    data = [{get_decors_url(i.pk, request)} for i in decors]
    return Response(data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def decor_detail(request, pk, format=None):
    try:
        decor = get_decor_element_by_pk(pk=pk)
    except KeyError:
        return HttpResponse(status=404)
    data = decor.__dict__.copy()
    data["theme"] = get_themes_url(data["theme"].pk, request)
    return Response(data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def level_list(request, format=None):
    levels = Level.objects.sorted_levels()
    serializer = LevelListSerializer(levels, many=True, context={"request": request})
    return Response(serializer.data)


# pk is the episode id
@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def level_for_episode(request, pk, format=None):
    levels = Level.objects.filter(episode__id=pk)
    serializer = LevelListSerializer(levels, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def level_detail(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelDetailSerializer(level, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def map_list(request, format=None):
    levels = Level.objects.sorted_levels()

    serializer = LevelMapListSerializer(levels, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def map_for_level(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelMapDetailSerializer(level, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def mode_for_level(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelModeSerializer(level, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def episode_list(request, format=None):
    episodes = Episode.objects.all()
    serializer = EpisodeListSerializer(
        episodes, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def episode_detail(request, pk, format=None):
    try:
        episode = Episode.objects.get(pk=pk)
    except Episode.DoesNotExist:
        return HttpResponse(status=404)

    serializer = EpisodeDetailSerializer(episode, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def levelblock_list(request, level, format=None):
    blocks = LevelBlock.objects.filter(level__id=level)

    serializer = LevelBlockSerializer(blocks, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def levelblock_for_level(request, pk, format=None):
    levelblocks = LevelBlock.objects.filter(level__id=pk)
    serializer = LevelBlockSerializer(
        levelblocks, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def levelblock_detail(request, pk, format=None):
    try:
        levelblock = LevelBlock.objects.get(pk=pk)
    except LevelBlock.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelBlockSerializer(levelblock, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def leveldecor_list(request, level, format=None):
    leveldecors = LevelDecor.objects.filter(level__id=level)

    serializer = LevelDecorSerializer(
        leveldecors, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def leveldecor_for_level(request, pk, format=None):
    leveldecors = LevelDecor.objects.filter(level__id=pk)
    serializer = LevelDecorSerializer(
        leveldecors, many=True, context={"request": request}
    )
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def leveldecor_detail(request, pk, format=None):
    try:
        leveldecor = LevelDecor.objects.get(pk=pk)
    except LevelDecor.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelDecorSerializer(leveldecor, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def block_list(request, format=None):
    block = Block.objects.all()
    serializer = BlockSerializer(block, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def block_detail(request, pk, format=None):
    try:
        block = Block.objects.get(pk=pk)
    except Block.DoesNotExist:
        return HttpResponse(status=404)

    serializer = BlockSerializer(block, context={"request": request})
    return Response(serializer.data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def theme_list(request, format=None):
    themes = get_all_themes()
    data = [{get_themes_url(i.pk, request)} for i in themes]
    return Response(data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def theme_detail(request, pk, format=None):
    try:
        theme = get_theme_by_pk(pk)
    except KeyError:
        return HttpResponse(status=404)
    return Response(theme.__dict__)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def character_list(request, format=None):
    characters = get_all_character()
    data = [{get_characters_url(i.pk, request)} for i in characters]
    return Response(data)


@api_view(("GET",))
@login_required(login_url=reverse_lazy("administration_login"))
def character_detail(request, pk, format=None):
    try:
        character = get_character_by_pk(pk)
    except KeyError:
        return HttpResponse(status=404)
    return Response(character.__dict__)


# Maybe used later for when we use a viewset which requires multiple serializer
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {"default": None}

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers["default"])
