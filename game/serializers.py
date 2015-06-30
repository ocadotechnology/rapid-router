from rest_framework import serializers
from models import Workspace, Level, Episode, LevelDecor, LevelBlock, Block


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('url', '__unicode__', 'name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', )


class LevelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        depth = 2
        fields = ('__unicode__', 'name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled', 'levelblock_set')


class EpisodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name')


class EpisodeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        depth = 1
        fields = ('url', '__unicode__', 'name', 'next_episode', 'level_set')


class LevelBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelBlock


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block