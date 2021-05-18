from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth_date = models.DateField()
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    user_image = models.ImageField(upload_to='media/userProfile/%Y/%m/')
    bio = RichTextField()
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name
