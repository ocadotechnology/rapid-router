from __future__ import absolute_import

from builtins import object

from rest_framework import serializers

from game import messages
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
            "blockly_enabled",
            "python_enabled",
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
    commands = serializers.SerializerMethodField()
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
            "blockly_enabled",
            "python_enabled",
            "python_view_enabled",
        )

    def get_title(self, obj):
        if obj.default:
            title = getattr(messages, "title_level" + obj.name)()
            return title
        else:
            return "Custom Level"

    def get_description(self, obj):
        return getattr(messages, "description_level" + obj.name)() if obj.default else obj.description

    def get_hint(self, obj):
        return getattr(messages, "hint_level" + obj.name)() if obj.default else obj.hint

    def get_commands(self, obj):
        return getattr(messages, "commands_level" + obj.name)() if obj.default else obj.commands

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
        fields = ("blockly_enabled", "python_enabled", "python_view_enabled")


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
