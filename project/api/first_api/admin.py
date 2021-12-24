from django.contrib import admin
from . import models
# Register your models here.


class GeeksModelAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(models.GeeksModel, GeeksModelAdmin)
