from django.contrib import admin
from .models import Customers, Branch

# Register your models here.



class BranchCustomersTabular(admin.TabularInline):
    model = Branch


class CustomersAdmin(admin.ModelAdmin):

    inlines = [BranchCustomersTabular]
 



admin.site.register(Customers, CustomersAdmin)
admin.site.register(Branch)