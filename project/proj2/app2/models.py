from django.db import models


# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    title = models.CharField(max_length=30)


def __str__(self):
    return self.album_name


class Meta:
    abstract = "true"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=20)


class Image(models.Model):
    album_logo = models.ImageField(upload_to='images')


class Video(models.Model):
    video = models.FileField(upload_to='videos/')


