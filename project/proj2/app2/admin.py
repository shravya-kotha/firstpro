from django.contrib import admin
from .models import Album, Song, Image, Video
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'artist', 'title',)
    list_display_links = ('album_name',)


class SongAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    list_display = ['album_logo']


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
