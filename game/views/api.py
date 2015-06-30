from django.http import HttpResponse
from game.models import Level, Episode
from game.serializers import LevelListSerializer, EpisodeSerializer, LevelDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'levels': reverse('level-list', request=request, format=format),
    })


@api_view(('GET',))
def level_list(request, format=None):
    levels = Level.objects.all()
    serializer = LevelListSerializer(levels, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(('GET',))
def level_detail(request, pk, format=None):
    try:
        level = Level.objects.get(pk=pk)
    except Level.DoesNotExist:
        return HttpResponse(status=404)

    serializer = LevelDetailSerializer(level, context={'request': request})
    return Response(serializer.data)


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


# Maybe used later for when we use a viewset which requires multiple serializer
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
        }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])
