from rest_framework import serializers
from models import Workspace, Level, Episode


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelListSerializer(serializers.ModelSerializer):
    episode = serializers.HyperlinkedRelatedField(view_name='episode-detail', read_only=True)

    class Meta:
        model = Level
        fields = ('url', '__unicode__', 'name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', )


class LevelDetailSerializer(serializers.ModelSerializer):
    episode = serializers.HyperlinkedRelatedField(view_name='episode-detail', read_only=True)

    class Meta:
        model = Level
        fields = ('__unicode__', 'name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled')


class EpisodeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name')


class EpisodeDetailSerializer(serializers.ModelSerializer):
    next_episode = serializers.HyperlinkedRelatedField(view_name='episode-detail', read_only=True)
    levels = serializers.HyperlinkedRelatedField(view_name='level-detail', many=True, read_only=True)

    class Meta:
        model = Episode
        fields = ('url', '__unicode__', 'name', 'next_episode', 'levels')