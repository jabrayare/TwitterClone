from django.db import models
from userProfile.models import Profile
from django.contrib.auth.models import User


class Follow(models.Model):
    user_profile = models.ForeignKey(
        Profile, default=None, on_delete=models.CASCADE, related_name='user_profile')
    follow_profile = models.ForeignKey(
        Profile, default=None, on_delete=models.CASCADE, related_name='follow_profile')
    approved = models.BooleanField(default=False)
