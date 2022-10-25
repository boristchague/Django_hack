from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('music', views.showSong, name="list_song"),
    path('song', views.add_song, name="adding_song"),
    path('artist', views.add_artist, name='adding_artist'),
    path('album', views.add_album, name='adding_album'),
    path('api/song', views.song_list),
    path('api/album', views.album_list),
    path('api/artist', views.artist_list)
]