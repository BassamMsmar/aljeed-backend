from django.contrib import admin
from .models import Shipment, City, Stages, ShipmentStatus
# from drivers.models import Driver

# Register your models here.
# class DriverTabular(admin.TabularInline):
#     model = Driver


class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'driver', 'customer_branch']
    list_filter = ['user', 'driver', 'customer_branch']
    search_fields = ['user', 'driver', 'customer_branch']
    # inlines = [DriverTabular]


admin.site.register(ShipmentStatus) 
admin.site.register(Shipment, ShipmentsAdmin)
admin.site.register(City)
admin.site.register(Stages)
