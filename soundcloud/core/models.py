from django.db import models

from soundcloud.helper import get_audio_length
from soundcloud.validators import validate_is_audio


class Artist(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    cover_artist = models.ImageField(upload_to='artist_cover/')


    def __str__(self):
        return self.email


class Genre(models.Model):
    """ Модель жанров треков
    """
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    """ Модель альбомов для треков
    """
    user = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)



class Track(models.Model):
    """ Модель треков
    """
    user = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre, related_name='track_genres')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    time_length = models.DecimalField(max_digits=20, decimal_places=2, blank=True)
    audio_file = models.FileField(upload_to='musics/', validators=[validate_is_audio])
    cover_image = models.ImageField(upload_to='music_images/')

    def save(self, *args, **kwargs):
        if not self.time_length:
            # logic for getting length of audio
            audio_length = get_audio_length(self.audio_file)
            self.time_length = f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} - {self.title}'


class PlayList(models.Model):
    """ Модель плейлистов пользователя
    """
    user = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='play_lists')
    title = models.CharField(max_length=50)
    tracks = models.ManyToManyField(Track, related_name='track_play_lists')

