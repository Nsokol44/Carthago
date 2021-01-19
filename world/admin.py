from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder, Shop

# Register your models here.
admin.site.register(WorldBorder, admin.OSMGeoAdmin)

@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
