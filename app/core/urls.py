from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"song", views.SongViewSet)
router.register(r"podcast", views.PodcastViewSet)
router.register(r"audiobook", views.AudiobookViewSet)
router.register(r"music", views.MusicViewSet, basename='music')

app_name = 'music'

urlpatterns = [
    path("", include(router.urls))
]
