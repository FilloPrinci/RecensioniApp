# Generated by Django 3.1 on 2020-08-20 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_post_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
    ]
