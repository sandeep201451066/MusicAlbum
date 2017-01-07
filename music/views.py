from django.shortcuts import render

# Create your views here.
from music.forms import AlbumListForm
from music.models import AlbumList

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    albums = AlbumList.objects.all()
    return render(request , 'music/index.html' ,{'albums': albums})


def create_album(request):

    form = AlbumListForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        albums = form.save(commit=False)
        albums.user = request.user
        albums.album_logo = request.FILES['album_logo']
        file_type = albums.album_logo.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'albums': albums,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'music/create_album.html', context)
        albums.save()
        return render(request, 'music/detail.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/create_album.html', context)

