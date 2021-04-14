import datetime

from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def setUp(self):
        self.time = datetime.datetime.now() + datetime.timedelta(hours=4)

    def test_song_file_fields(self):
        """Test creating a new entry in Song file is successfull"""
        name = 'Blame it on me'
        duration = 300
        uploaded_time = self.time
        song = models.Song.objects.create(
            name=name,
            duration=duration,
            uploaded_time=uploaded_time
        )

        self.assertEqual(song.name, name)
        self.assertEqual(song.duration, duration)

    def test_song_str(self):
        """Test song string representation"""
        name = 'Blame it on me'
        duration = 300
        uploaded_time = self.time
        song = models.Song.objects.create(
            name=name,
            duration=duration,
            uploaded_time=uploaded_time
        )

        self.assertEqual(str(song), song.name)
