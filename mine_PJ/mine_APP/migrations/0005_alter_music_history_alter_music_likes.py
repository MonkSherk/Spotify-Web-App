# Generated by Django 4.2.14 on 2024-07-17 14:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mine_APP', '0004_music_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='history',
            field=models.ManyToManyField(blank=True, related_name='music_history', through='mine_APP.History', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='music',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_music', to=settings.AUTH_USER_MODEL),
        ),
    ]