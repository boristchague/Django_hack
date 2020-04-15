from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil', views.home),
    path('pictures/<int:year>/<int:month>/<int:day>/', views.login, name="test"),
    path('detail/<str:name>/<int:year>/<int:month>/<int:day>/', views.picture_detail),
    #re_path(r'^pictures/(?P<year>\{4})/(?P<month>\{2})/(?P<day>\{2})', views.login, name="test")
    path('song', views.showSong, name="list_song"),
    path('create', views.add_song, name="adding_song")

]