from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"song", views.SongViewSet)

app_name = 'song'

urlpatterns = [
    path("", include(router.urls))
]
