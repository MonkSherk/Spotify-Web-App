from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/album')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class music(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/music')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL,null=True , related_name='musics')
    audio_file = models.FileField(upload_to='media/files/music')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='musics')
    history = models.ManyToManyField(User, related_name='music_history',through="History",blank=True) # аргумент Through="History" указывает на модель History
    likes = models.ManyToManyField(User, related_name='liked_music', blank=True)
    def __str__(self):
        return self.name

class PlayList(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists_au')
    is_public = models.BooleanField(default=False)
    musics = models.ManyToManyField(music, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class History(models.Model):
    music = models.ForeignKey(music, on_delete=models.CASCADE,related_name='user_history_music')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listned_at = models.DateTimeField(auto_now_add=True)
