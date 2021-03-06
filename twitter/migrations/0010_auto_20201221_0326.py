# Generated by Django 3.1.4 on 2020-12-21 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0009_remove_post_tweet_downloads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tweeter',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='tweet_downloads',
            field=models.IntegerField(default=0),
        ),
    ]
