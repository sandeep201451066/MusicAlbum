from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class AlbumList(models.Model):
    user = models.ForeignKey(User, default=1)
    album_title = models.CharField(max_length=500)
    artist = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    album_logo = models.FileField(2000)
    is_public = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.album_title + '-' + self.artist

class SongList(models.Model):
    album = models.ForeignKey(AlbumList , on_delete=models.CASCADE())
    song_title = models.CharField(max_length=200)
    song_file = models.FileField(max_length=1000)
    is_public = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.song_title
