from django.contrib import admin

from core import models


class SongAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id',
                    'name',
                    'duration',
                    'uploaded_time'
                    ]


class PodcastAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['id',
                    'name',
                    'duration',
                    'uploaded_time',
                    'host',
                    'participants'
                    ]


class AudiobookAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['id',
                    'title',
                    'author',
                    'narrator',
                    'duration',
                    'uploaded_time'
                    ]


admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Podcast, PodcastAdmin)
admin.site.register(models.Audiobook, AudiobookAdmin)
