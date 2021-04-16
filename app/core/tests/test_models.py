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

    def test_podcast_file_field(self):
        """Test creating a new entry in Podcast file is successfull"""
        name = "pluto"
        duration = 400
        uploaded_time = self.time
        host = 'Danish'
        participants = ['abc', 'bcd', 'cde']
        podcast = models.Podcast.objects.create(
            name=name,
            duration=duration,
            uploaded_time=uploaded_time,
            host=host,
            participants=participants
        )

        self.assertEqual(podcast.name, name)
        self.assertEqual(podcast.host, host)

    def test_podcast_str(self):
        """Test string repr of podcast"""
        name = "pluto"
        duration = 400
        uploaded_time = self.time
        host = 'Danish'
        participants = ['abc', 'bcd', 'cde']
        podcast = models.Podcast.objects.create(
            name=name,
            duration=duration,
            uploaded_time=uploaded_time,
            host=host,
            participants=participants
        )

        self.assertEqual(str(podcast), podcast.name)
