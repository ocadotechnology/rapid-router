from game import messages
from game.messages import description_level_default, hint_level_default
from rest_framework import serializers
from models import Workspace, Level, Episode, LevelDecor, LevelBlock, Block, Theme, Character, Decor


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
    leveldecor_set = serializers.HyperlinkedIdentityField(
        view_name='leveldecor-for-level',
        read_only=True
    )
    map = serializers.HyperlinkedIdentityField(
        view_name='map-for-level',
        read_only=True
    )

    class Meta:
        model = Level
        fields = ('__unicode__', 'episode', 'name', 'title', 'description', 'hint', 'next_level', 'default',
                  'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled', 'levelblock_set', 'leveldecor_set',
                  'map')

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


class LevelMapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('origin', 'destinations', 'path', 'traffic_lights', 'max_fuel', 'theme')


class EpisodeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name')


class EpisodeDetailSerializer(serializers.HyperlinkedModelSerializer):
    level_set = serializers.HyperlinkedIdentityField(
        view_name='level-for-episode',
        read_only=True
    )

    class Meta:
        model = Episode
        fields = ('url', 'id', '__unicode__', 'name', 'level_set')


class LevelBlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelBlock


class LevelDecorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelDecor


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theme


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character


class DecorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decor
