from django.db import models
from django.contrib.postgres.fields import ArrayField

from core import services


class Song(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=services.CommonService.generate_id,
        editable=False,
        db_index=True,
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    duration = models.IntegerField(default=0, null=False, blank=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Podcast(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=services.CommonService.generate_id,
        editable=False,
        db_index=True,
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    duration = models.IntegerField(default=0, null=False, blank=False)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, null=False, blank=False)
    participants = ArrayField(models.CharField(
        max_length=100, blank=True, null=True),
        size=10)

    def __str__(self):
        return self.name
