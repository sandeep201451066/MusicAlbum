from django.shortcuts import render

# Create your views here.
from music.models import AlbumList


def index(request):
    albums = AlbumList.objects.all()
    return render(request , 'music/index.html' ,{'albums': albums})