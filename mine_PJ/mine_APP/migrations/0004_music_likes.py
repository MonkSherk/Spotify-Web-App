# Generated by Django 4.2.14 on 2024-07-15 15:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mine_APP', '0003_remove_genre_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likes',
            field=models.ManyToManyField(related_name='liked_music', to=settings.AUTH_USER_MODEL),
        ),
    ]