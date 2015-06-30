from rest_framework import serializers
from models import Workspace, Level, Episode


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelListSerializer(serializers.ModelSerializer):
    episode = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Level
        fields = ('url', 'name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', )


class LevelDetailSerializer(serializers.ModelSerializer):
    episode = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Level
        fields = ('name', 'episode', 'default', 'blocklyEnabled', 'pythonEnabled', 'pythonViewEnabled')


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Episode
        fields = ('url', 'name')