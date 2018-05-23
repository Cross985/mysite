from django.db import models

# Create your models here.
class Album(models.Model):
    def __str__(self):
        return self.album_title
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    song_count = models.IntegerField(default=1)


class Song(models.Model):
    def __str__(self):
        return self.song_title
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='related_%(class)s_record')
    song_title = models.CharField(max_length=100)
    song_duration = models.FloatField(default=0.00)
