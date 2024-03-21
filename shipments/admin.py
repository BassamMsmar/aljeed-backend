from django.contrib import admin
from .models import Shipment, City, Stages, Receipt
# from drivers.models import Driver

# Register your models here.
# class DriverTabular(admin.TabularInline):
#     model = Driver


class ShipmentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'driver', 'customer_branch', 'status']
    list_filter = ['user', 'driver', 'customer_branch', 'status']
    search_fields = ['user', 'driver', 'customer_branch', 'status']
    # inlines = [DriverTabular]
               
admin.site.register(Shipment, ShipmentsAdmin)
admin.site.register(City)
admin.site.register(Stages)
admin.site.register(Receipt)