from django.contrib import admin
from .models import Shipments
# from drivers.models import Driver

# Register your models here.
# class DriverTabular(admin.TabularInline):
#     model = Driver


class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'driver', 'customer', 'destination', 'status']
    list_filter = ['user', 'driver', 'customer', 'destination', 'status']
    search_fields = ['user', 'driver', 'customer', 'destination', 'status']
    # inlines = [DriverTabular]
               
admin.site.register(Shipments, ShipmentsAdmin)