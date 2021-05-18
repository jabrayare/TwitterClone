from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from userProfile.models import Profile


class Post(models.Model):
    authorprofile = models.ForeignKey(
        Profile, default=None, on_delete=models.CASCADE)
    tweet_text = models.CharField(max_length=255, blank=True)
    tweet_image = models.ImageField(upload_to='media/post/%Y/%m')
    tweet_likes = models.IntegerField(default=0)
    tweet_comments = models.IntegerField(default=0)
    tweet_shares = models.IntegerField(default=0)
    tweet_downloads = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.tweet_text
