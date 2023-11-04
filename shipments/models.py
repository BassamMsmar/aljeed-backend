from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from drivers.models import Driver
from customers.models import Customers, Branch
# Create your models here.



FLAG_TYPES = (
    ('Jeddah','Jeddah'),
    ('Riyad','Riyad'),
    ('Dammam','Dammam'),
 )


STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
    ('Feedback','Feedback'),
    ('Completed','Completed'),
 )


# Create your models here.
class Shipments(models.Model):
    user = models.ForeignKey(User,  related_name='shipments_user', on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver,  related_name='shipments_driver', on_delete=models.SET_NULL, null=True)
    customer_branch = models.ForeignKey(Branch, related_name='shipments_company', on_delete=models.SET_NULL, null=True)
    fare = models.IntegerField()
    days_stayed = models.IntegerField(null=True, blank=True)
    stay_cost = models.IntegerField(null=True, blank=True)
    deducted = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Recieved')
    destination = models.CharField(max_length=20, choices=FLAG_TYPES)
    create_at = models.DateTimeField(default=timezone.now)
    expected_arrival_date = models.DateTimeField(null=True, blank=True)
    actual_delivery_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.driver} - {self.destination}'