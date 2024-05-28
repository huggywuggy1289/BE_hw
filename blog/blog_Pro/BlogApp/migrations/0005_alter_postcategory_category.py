# Generated by Django 5.0.3 on 2024-05-27 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_category_postcategory_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts_postcategory', to='BlogApp.category'),
        ),
    ]