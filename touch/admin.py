from django.contrib import admin

from django.contrib.admin.sites import site
from touch.models import Touch

class TouchAdmin(admin.ModelAdmin):
    list_display=('name','email','massage')

admin.site.register(Touch,TouchAdmin)

# Register your models here.
