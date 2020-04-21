from django.shortcuts import render
from django.http import request, HttpResponse
from django.template import loader
from biblio.models import Song, Album, Artist
from .forms import SongForm, ArtistForm, AlbumForm


# Create your views here.

#def home(request):
#    return render(request, 'biblio/index.html')


# Create your views here.



def showSong(request):

    song = Song.objects.all()
    album = Album.objects.all()
    artist = Artist.objects.all()
    return  render(request, "biblio/index.html", context={'song': song, 'album': album, 'artist': artist})



def add_song(request):

    #form = SongForm(request.POST or request.GET)
    if request.method == 'POST':
        print("we are in post process !!!")
        form = SongForm(request.POST)
        if request.POST.get('album') or request.POST.get('name'):
            form.album = request.POST.get('album')
            form.name = request.POST.get('name')
            form.duration = request.POST.get('duration')
            form.lyrics = request.POST.get('lyrics')
            form.save()
        #if form.is_valid():
         #   print(f"album: {form.cleaned_data['album']}")
          #  print(f"name: {form.cleaned_data['name']}")
           # print(f"duration: {form.cleaned_data['duration']}")
            #print(f"lyrics: {form.cleaned_data['lyrics']}")


            return render(request, 'biblio/song.html', context={'form': form})
    else:
        form = SongForm()
    return render(request, 'biblio/song.html', context={'form': form})



def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)

        if request.POST.get('name') or request.POST.get('music_type'):
            form.name = request.POST.get('name')
            form.music_type = request.POST.get('music_type')
            form.save() 

            return render(request, 'biblio/artist.html', locals())

    else:
        form = ArtistForm()
        return render(request, 'biblio/artist.html', locals())




def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)

        if request.POST.get('name') or request.POST.get('artist_name'):
            form.name = request.POST.get('name')
            form.artist_name = request.POST.get('artist_name')
            form.release_date = request.POST.get('release_date')
            form.production_house = request.POST.get('production_house')
            form.save()

            return render(request, 'biblio/album.html', context={'form': form})

    else:
        form = AlbumForm()
        return render(request, 'biblio/album.html', context={'form': form})





