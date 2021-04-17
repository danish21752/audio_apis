from rest_framework import serializers, exceptions

from core.models import Song, Podcast, Audiobook


class SongSerializer(serializers.ModelSerializer):
    """Serializer for the song object"""

    class Meta:
        model = Song
        fields = ["id",
                  "name",
                  "duration",
                  "uploaded_time"
                  ]


class PodcastSerializer(serializers.ModelSerializer):
    """Serializer for the podcast object"""

    class Meta:
        model = Podcast
        fields = ["id",
                  "name",
                  "duration",
                  "uploaded_time",
                  "host",
                  "participants"
                  ]

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.host = validated_data.get("host", instance.host)
        instance.participants = validated_data.get(
            "participants", instance.participants)
        instance.save()
        return instance


class AudiobookSerializer(serializers.ModelSerializer):
    """Serializer for the Audiobook object"""

    class Meta:
        model = Audiobook
        fields = ["id",
                  "title",
                  "author",
                  "narrator",
                  "duration",
                  "uploaded_time"
                  ]


class MusicSerializer(serializers.Serializer):
    """Serializer for music object"""

    audioFileType = serializers.IntegerField(required=True)
    audioFileMetadata = serializers.JSONField()

    def create(self, validated_data):
        audioFileType = validated_data.get('audioFileType', 0)
        audioFileMetadata = validated_data.get('audioFileMetadata', None)

        if audioFileMetadata is not None:
            if audioFileType == 0:
                song = Song.objects.create(**audioFileMetadata)
                return song

            if audioFileType == 1:
                podcast = Podcast.objects.create(**audioFileMetadata)
                return podcast

            if audioFileType == 2:
                audiobook = Audiobook.objects.create(**audioFileMetadata)
                return audiobook

            else:
                raise exceptions.AuthenticationFailed("Unknown Field Type,"
                                                      "Valid audioFieldType  "
                                                      "[ 0 - song, "
                                                      "1 - podcast, "
                                                      "2 - audiobook ]")

        return None
