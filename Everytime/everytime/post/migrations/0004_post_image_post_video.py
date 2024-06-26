# Generated by Django 5.0.6 on 2024-06-24 08:44

import post.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_scrap'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=post.models.upload_filepath),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, upload_to=post.models.upload_filepath),
        ),
    ]
