from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^index/$' ,views.index , name='index' ),
    url(r'^create_album/$' , views.create_album , name='create_album'),
    url(r'' , views.index , name='index'),
]