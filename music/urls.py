from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^index/$' ,views.index , name='index' ),
    url(r'' , views.index , name='index'),
]