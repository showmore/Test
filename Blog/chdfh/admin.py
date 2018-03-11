from django.contrib import admin
from chdfh.models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'QQ','blog', 'location', 'occupation', 'reward', 'topic_count', 'post_count')