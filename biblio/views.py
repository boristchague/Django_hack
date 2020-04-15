from django.shortcuts import render
from django.http import request, HttpResponse
from django.template import loader
from biblio.models import Song, Album, Artist


# Create your views here.

def home(request):

    return render(request, 'biblio/index.html')


def login(request, year, month, day):
    template = loader.get_template('biblio/index.html')

    context = {"year": year,
               "month": month,
               "day": day}
    #return render(request, "biblio/index.html", context=context)
    return HttpResponse(template.render({"year": year,
               "month": month,
               "day": day}, request))




# Create your views here.
def djangorocks(request):
    return HttpResponse('<h1><center>hello Django !!C\'est une réponse de Jazzy</center></h1>')
def picture_detail(request, name, year, month, day):
    template = loader.get_template('biblio/index.html')

    context = {
            'pictures' : {
                    'name' : 'Killer',
                    'filename' : '_w3css_img_nature.jpg'
                },
            "year": year,
            "month": month,
            "day": day
            
    }
    return HttpResponse(template.render(context, request))


def showSong(request):

    song = Song.objects.all()
    album = Album.objects.all()
    artist = Artist.objects.all()
    return  render(request, "biblio/song.html", context={'song': song, 'album': album, 'artist': artist})



def add_song(request):

    form = Song(request.POST or None)
    if request.method == 'POST':
        if request.POST.get('album') or request.POST.get('name'):
            form.album = request.POST.get('album')
            form.name = request.POST.get('name')
            form.duration = request.POST.get('duration')
            form.lyrics = request.POST.get('lyrics')
            form.save()

            return render(request, 'biblio/form.html', locals())
    else:
        return render(request, 'biblio/form.html', locals())









