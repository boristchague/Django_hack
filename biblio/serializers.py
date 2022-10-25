from rest_framework import serializers
from .models import Album,Artist,Song



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('album', 'name','duration', 'lyrics')
        album = serializers.CharField(max_length=200)
        name = serializers.CharField(max_length=200)
        duration = serializers.IntegerField()
        lyrics = serializers.CharField()


class AlbumSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Album
        fields = ('name', 'artist_name', 'release_date', 'production_house')
        name = serializers.CharField(max_length=200)
        artist_name = serializers.CharField(max_length=200)
        release_date = serializers.DateField()
        production_house = serializers.CharField(max_length=200)



class ArtistSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Artist
        fields = '__all__'




