from rest_framework import serializers

from core.models import Song


class SongSerializer(serializers.ModelSerializer):
    """Serializer for the song object"""

    class Meta:
        model = Song
        fields = ["id", "name", "duration", "uploaded_time"]
