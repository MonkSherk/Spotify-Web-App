from django.contrib import admin

# Register your models here.
from mine_APP import models

admin.site.register([models.Genre, models.Album, models.music, models.PlayList, models.History])