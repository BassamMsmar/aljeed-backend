from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    

class Branch(models.Model):
    customers = models.ForeignKey(Customers, related_name='branch_customers', on_delete=models.CASCADE) 
    name = models.CharField(_("Name"),max_length=255)
    city = models.CharField(_("City"),max_length=255)

    def __str__(self):
        return f'{self.customers} - {self.name}'
    
    