from django import forms
from .models import Artist, Album, Song


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

#class SongForm(forms.Form):
 #   album = forms.CharField(max_length=300, required=False)
  #  name = forms.CharField(max_length=300, required=False)
   # duration = forms.IntegerField(required=False)
    #lyrics = forms.CharField(required=False)


#class AlbumForm(forms.Form):
 #   name = forms.CharField(max_length=225)
  #  artist_name = forms.CharField()
   # release_date = forms.DateField(required=False)
    #production_house = forms.CharField(max_length=200, required=False)






class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'