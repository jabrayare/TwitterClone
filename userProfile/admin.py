from django.contrib import admin
from .models import Profile
from django.utils.html import format_html


class UserProfileAdmin(admin.ModelAdmin):
    def profile_image(self, object):
        return format_html('<img src = {} width="40px" />'.format(object.user_image.url))

    list_display = ('id', 'first_name', 'email', 'profile_image',)
    list_display_links = ('id', 'first_name', 'email',)


admin.site.register(Profile, UserProfileAdmin)
