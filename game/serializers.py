from __future__ import absolute_import

from builtins import object

from rest_framework import serializers

from game import messages
from game.messages import description_level_default, hint_level_default
from game.theme import get_theme, get_themes_url
from .models import Workspace, Level, Episode, LevelDecor, LevelBlock, Block


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Workspace


class LevelListSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta(object):
        model = Level
        fields = (
            "url",
            "__str__",
            "episode",
            "name",
            "title",
            "default",
            "blocklyEnabled",
            "pythonEnabled",
        )

    def get_title(self, obj):
        if obj.default:
            title = getattr(messages, "title_level" + obj.name)()
            return title
        else:
            return "Custom Level"


class LevelDetailSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    hint = serializers.SerializerMethodField()
    levelblock_set = serializers.HyperlinkedIdentityField(
        view_name="levelblock-for-level", read_only=True
    )
    map = serializers.HyperlinkedIdentityField(
        view_name="map-for-level", read_only=True
    )
    mode = serializers.HyperlinkedIdentityField(
        view_name="mode-for-level", read_only=True
    )

    class Meta(object):
        model = Level
        fields = (
            "__str__",
            "episode",
            "name",
            "title",
            "description",
            "hint",
            "next_level",
            "default",
            "levelblock_set",
            "map",
            "mode",
            "blocklyEnabled",
            "pythonEnabled",
            "pythonViewEnabled",
        )

    def get_title(self, obj):
        if obj.default:
            title = getattr(messages, "title_level" + obj.name)()
            return title
        else:
            return "Custom Level"

    def get_description(self, obj):
        if obj.default:
            description = getattr(messages, "description_level" + obj.name)()
            return description
        else:
            return description_level_default()

    def get_hint(self, obj):
        if obj.default:
            hint = getattr(messages, "hint_level" + obj.name)()
            return hint
        else:
            return hint_level_default()

    def get_leveldecor_set(self, obj):
        leveldecors = LevelDecor.objects.filter(level__id=obj.id)
        serializer = LevelDecorSerializer(
            leveldecors,
            many=True,
            context={"request": self.context.get("request", None)},
        )
        return serializer.data


class LevelModeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Level
        fields = ("blocklyEnabled", "pythonEnabled", "pythonViewEnabled")


class LevelMapListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="map-for-level", read_only=True
    )

    class Meta(object):
        model = Level
        fields = ("url",)


class LevelMapDetailSerializer(serializers.HyperlinkedModelSerializer):
    leveldecor_set = serializers.SerializerMethodField()
    theme = serializers.SerializerMethodField()

    class Meta(object):
        model = Level
        fields = (
            "origin",
            "destinations",
            "path",
            "traffic_lights",
            "max_fuel",
            "theme",
            "leveldecor_set",
        )

    def get_leveldecor_set(self, obj):
        leveldecors = LevelDecor.objects.filter(level__id=obj.id)
        serializer = LevelDecorSerializer(
            leveldecors,
            many=True,
            context={"request": self.context.get("request", None)},
        )
        return serializer.data

    def get_theme(self, obj):
        pk = get_theme(obj.theme_name).pk
        return get_themes_url(pk, self.context.get("request", None))


class EpisodeListSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta(object):
        model = Episode
        fields = ("url", "__str__", "name")

    def get_name(self, obj):
        return messages.get_episode_title(obj.id)


class EpisodeDetailSerializer(serializers.HyperlinkedModelSerializer):
    level_set = serializers.SerializerMethodField()
    level_set_url = serializers.HyperlinkedIdentityField(
        view_name="level-for-episode", read_only=True
    )
    name = serializers.SerializerMethodField()

    class Meta(object):
        model = Episode
        depth = 1
        fields = ("url", "__str__", "name", "level_set", "level_set_url")

    def get_level_set(self, obj):
        levels = Level.objects.filter(episode__id=obj.id)
        serializer = LevelListSerializer(
            levels, many=True, context={"request": self.context.get("request", None)}
        )
        return serializer.data

    def get_name(self, obj):
        return messages.get_episode_title(obj.id)


class LevelBlockSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = LevelBlock


class LevelDecorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = LevelDecor


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Block
        fields = ("url", "id", "type")
