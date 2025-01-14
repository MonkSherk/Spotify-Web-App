# Generated by Django 4.2.14 on 2024-07-17 16:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mine_APP', '0005_alter_music_history_alter_music_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists_au', to=settings.AUTH_USER_MODEL),
        ),
    ]
