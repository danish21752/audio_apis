from django.contrib import admin

from core import models


class SongAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'duration', 'uploaded_time']


admin.site.register(models.Song, SongAdmin)
