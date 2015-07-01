from game import messages
from game.messages import description_level_default, hint_level_default
from requests import request
from rest_framework import serializers
from models import Workspace, Level, Episode, LevelDecor, LevelBlock, Block, Theme, Character


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelListSerializer(serializers.ModelSerializer):
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


class LevelDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    hint = serializers.SerializerMethodField()

    class Meta:
        model = Level
        depth = 1
        fields = ('__unicode__', 'episode', 'name', 'title', 'description', 'hint', 'default', 'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled', 'levelblock_set')

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


class EpisodeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name')


class EpisodeDetailSerializer(serializers.HyperlinkedModelSerializer):
    level_set = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        depth = 1
        fields = ('url', '__unicode__', 'name', 'level_set')

    def get_level_set(self, obj):
        levels = Level.objects.filter(episode__id=obj.id)
        serializer = LevelListSerializer(levels, many=True, context={'request': self.context.get('request', None)})
        return serializer.data


class LevelBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelBlock


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character