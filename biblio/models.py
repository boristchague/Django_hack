from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=300)
    music_type = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id}"



class Album(models.Model):
    name = models.CharField(max_length=225)
    artist_name = models.ForeignKey(to='Artist', on_delete=models.CASCADE, )
    release_date = models.DateField(auto_now_add=True)
    production_house = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}"

class Song(models.Model):
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=220, default="Aucune musique")
    duration = models.IntegerField(default=0, help_text="Durée en séconde")
    lyrics = models.TextField(blank=True)



    def __str__(self):
        return self.name
# Create your models here



