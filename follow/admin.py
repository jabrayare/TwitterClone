from django.contrib import admin
from .models import Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'approved', 'user_profile', 'follow_profile')


admin.site.register(Follow, FollowAdmin)
