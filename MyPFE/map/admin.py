from django.contrib import admin
from django.contrib.gis import admin
from .models import *


# Register your models here.

# admin.site.register(nodes)


# class nodesAdmin(admin.ModelAdmin):
#     list_display = ('Name', 'Latitude', 'Longitude')



class nodesAdmin(admin.ModelAdmin):
    list_display = ('proj_name', 'Latitude', 'Longitude', )
    
    def proj_name(self, obj):
        return obj.proj.Nom_projet
    
    proj_name.short_description = 'Project Name'


admin.site.register(nodes, nodesAdmin)
admin.site.register(Post)