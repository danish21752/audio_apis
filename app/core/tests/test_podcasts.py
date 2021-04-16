import datetime

from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core import models


CREATE_PODCAST_URL = reverse('music:podcast-list')


def detail_url(podcast_id):
    """Return podcast detail URL"""
    return reverse('music:podcast-detail', args=[podcast_id])


def create_podcast(**param):
    """Create and return a podcast object"""
    return models.Podcast.objects.create(**param)


class PodcastApiTest(TestCase):
    """Test the Podcast API's"""

    def setUp(self):
        self.client = APIClient()
        self.time = datetime.datetime.now() + datetime.timedelta(hours=4)

    def test_create_podcast_successfull(self):
        """Test creatng a podcast successful"""
        payload = {
            "name": "pluto",
            "duration": 400,
            "uploaded_time": self.time,
            "host": 'Danish',
            "participants": ['abc', 'bcd', 'cde']
        }
        response = self.client.post(CREATE_PODCAST_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        podcast = models.Podcast.objects.filter(**response.data).exists()
        self.assertTrue(podcast)

    def test_update_podcast_successfull(self):
        """Test updating a podcast successfull"""
        podcast = create_podcast(
            name="pluto",
            duration=400,
            uploaded_time=self.time,
            host='Danish',
            participants=['abc', 'bcd', 'cde']
        )

        payload = {
            "name": "pluto",
            "duration": 402,
            "host": 'Khan',
            "participants": ['abc', 'bcd', 'cde']
        }
        url = detail_url(podcast.id)
        response = self.client.put(url, payload)
        podcast.refresh_from_db()
        self.assertEqual(podcast.name, payload['name'])
        self.assertEqual(response.data['duration'], payload['duration'])
