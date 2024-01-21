from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    ('Late','Late'),
    ('Completed','Completed'),
 )


# Create your models here.
class Shipments(models.Model):
    user = models.ForeignKey(User,  related_name='shipments_user', on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver,  related_name='shipments_driver', on_delete=models.SET_NULL, null=True)
    customer_branch = models.ForeignKey(Branch, related_name='shipments_company', on_delete=models.SET_NULL, null=True)
    fare = models.IntegerField(_("Fare"),)
    days_stayed = models.IntegerField(_("Days Stayed "), null=True, blank=True)
    stay_cost = models.IntegerField(_("Stay Cost"), null=True, blank=True)
    deducted = models.IntegerField(_("Deducted"), null=True, blank=True)
    status = models.CharField(_("Status "), max_length=20, choices=STATUS, default='Recieved')
    destination = models.CharField(_("Destination"), max_length=20, choices=FLAG_TYPES)
    create_at = models.DateTimeField(_("Create At"), default=timezone.now)
    expected_arrival_date = models.DateTimeField(_("Expected Arrival Date"), null=True, blank=True, default=timezone.now)
    actual_delivery_date = models.DateTimeField(_("Actual Delivery Date "), null=True, blank=True, default=timezone.now)

    def __str__(self) -> str:
        return f'{self.driver} - {self.destination}'