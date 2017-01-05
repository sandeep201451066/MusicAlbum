from django.contrib import admin

# Register your models here.
from music.models import AlbumList, SongList

admin.site.register(AlbumList)
admin.site.register(SongList)

