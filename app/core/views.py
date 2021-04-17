from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from core.serializers import SongSerializer, \
    PodcastSerializer, AudiobookSerializer, \
    MusicSerializer
from core.models import Song, Podcast, Audiobook


class SongViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Handling CRUD operations for Song object"""

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        _queryset = Song.objects.all()
        return _queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        data = request.data
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class PodcastViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Handling CRUD operations for podcast object"""

    serializer_class = PodcastSerializer
    queryset = Podcast.objects.all()

    def get_queryset(self):
        _queryset = Podcast.objects.all()
        return _queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED, headers=headers)


class AudiobookViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Handling CRUD ooperations for Audiobook"""

    serializer_class = AudiobookSerializer
    queryset = Audiobook.objects.all()

    def get_queryset(self):
        _queryset = Audiobook.objects.all()
        return _queryset

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class MusicViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    """Handling create operation for diff Music types"""

    serializer_class = MusicSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            headers = self.get_success_headers(serializer.data)
            return Response(
                "Created",
                status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)
