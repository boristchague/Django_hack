from django import forms
from .models import Artist, Album, Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'