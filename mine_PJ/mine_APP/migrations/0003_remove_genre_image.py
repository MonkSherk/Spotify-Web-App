# Generated by Django 4.2.14 on 2024-07-15 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mine_APP', '0002_alter_album_image_alter_genre_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='image',
        ),
    ]
