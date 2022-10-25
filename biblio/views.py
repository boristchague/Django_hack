from django.shortcuts import render
from django.http import request, HttpResponse
from django.template import loader
from biblio.models import Song, Album, Artist
from .forms import SongForm, ArtistForm, AlbumForm



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer, AlbumSerializer, ArtistSerializer


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



@api_view(['GET', 'POST'])
def song_list(request):
    """//List all snippets, or creates a new snippets"""

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def album_list(request):
    """//List all albums, or creates a new snippets"""

    if request.method == 'GET':
        album = Album.objects.all()
        serializer = SongSerializer(album, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def artist_list(request):
    """//List all albums, or creates a new snippets"""

    if request.method == 'GET':
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




