import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core import models


CREATE_SONG_URL = reverse('song:song-list')


def detail_url(song_id):
    """Return song detail URL"""
    return reverse("song:song-detail", args=[song_id])


def create_song(**param):
    """Create and return a song object"""
    return models.Song.objects.create(**param)


class SongApiTest(TestCase):
    """Test the song API"""

    def setUp(self):
        self.client = APIClient()
        self.time = datetime.datetime.now() + datetime.timedelta(hours=4)

    def test_create_song_successfull(self):
        """Test creating a song is successfull"""
        payload = {
            'name': 'Blame it on me',
            'duration': 300,
            'uploaded_time': self.time
        }
        response = self.client.post(CREATE_SONG_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        song = models.Song.objects.filter(**response.data).exists()
        self.assertTrue(song)

    def test_update_song(self):
        """Test updating a song successful"""
        song = create_song(
            name='Blame it on me',
            duration=300,
            uploaded_time=self.time
        )
        payload = {
            'name': 'Blame it on me',
            'duration': 302,
        }
        url = detail_url(song.id)
        response = self.client.put(url, payload)

        song.refresh_from_db()

        self.assertEqual(song.name, payload['name'])
        self.assertEqual(response.data['duration'], payload['duration'])
