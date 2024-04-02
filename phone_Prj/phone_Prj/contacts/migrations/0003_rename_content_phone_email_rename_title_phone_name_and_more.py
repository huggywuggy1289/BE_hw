# Generated by Django 5.0.3 on 2024-04-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_post_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='content',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='phone',
            name='phone_num',
            field=models.TextField(default=1, max_length=11),
            preserve_default=False,
        ),
    ]
