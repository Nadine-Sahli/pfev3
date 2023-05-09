from django.contrib import admin
from django.contrib.gis import admin
from .models import *


# Register your models here.

# admin.site.register(nodes)


class nodesAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Latitude', 'Longitude')









admin.site.register(nodes, nodesAdmin)




