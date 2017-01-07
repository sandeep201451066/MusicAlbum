from django import forms
from django.contrib.auth.models import User

from .models import AlbumList


class AlbumListForm(forms.ModelForm):

    class Meta:
        model = AlbumList
        fields = ['artist', 'album_title', 'desc', 'album_logo']

