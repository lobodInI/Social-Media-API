from django.contrib import admin

from social_media.models import (
    UserProfile, Follow, Post, Comment, Like
)

admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
