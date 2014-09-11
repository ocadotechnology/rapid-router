from rest_framework import serializers
from models import Workspace, Level


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
