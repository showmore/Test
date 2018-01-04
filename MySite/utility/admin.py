from django.contrib import admin

from utility.models import xajtdx_instrument

class instrumentAdmin(admin.ModelAdmin):
    list_display = ('cname', 'requirement','instrCategory','subject','org','status',)


# Register your models here.
admin.site.register(xajtdx_instrument)

