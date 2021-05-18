from django.contrib import admin
from .models import Post
from django.utils.html import format_html
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    def tweetImage(self, object):
        return format_html('<img src={} width="40" />'.format(object.tweet_image.url))
    list_display = ('id', 'tweet_text', 'tweetImage', )
    list_display_links = ('id', 'tweet_text',)


admin.site.register(Post, PostAdmin)
