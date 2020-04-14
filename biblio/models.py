from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=220, default="Aucune musique")
    duration = models.IntegerField(default=0, help_text="Durée en séconde")
    album = models.CharField(max_length=200)
    lyrics = models.TextField(blank=True)



    def __str__(self):
        return self.name
# Create your models here
