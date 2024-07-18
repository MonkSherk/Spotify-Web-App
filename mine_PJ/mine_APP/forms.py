from mine_APP import models
from django import forms
class AddMusicForm(forms.ModelForm):
    class Meta:
        model = models.music
        fields = ['name', 'image', 'audio_file', 'genres' , 'album']

class PlayListForm(forms.ModelForm):
    class Meta:
        model = models.PlayList
        fields = 'name' , 'is_public'