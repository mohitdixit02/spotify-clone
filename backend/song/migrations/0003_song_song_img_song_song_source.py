# Generated by Django 4.1.1 on 2022-11-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_remove_song_length_alter_song_plays'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_img',
            field=models.ImageField(default='', upload_to='song/media'),
        ),
        migrations.AddField(
            model_name='song',
            name='song_source',
            field=models.FileField(default='', upload_to='song/media'),
        ),
    ]
