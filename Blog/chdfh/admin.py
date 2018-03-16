from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'QQ','blog', 'location', 'occupation', 'reward', 'topic_count', 'post_count')

admin.site.register(Blog)

admin.site.register(EmployeeInfo)

@admin.register(AlcoholDetection)
class AlcoholDetectionAdmin(admin.ModelAdmin):
    list_display = ('jobnumber','concentration','status','unit','date','time','picurl' )