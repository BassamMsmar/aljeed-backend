from django.db import models
from django.utils.translation import gettext_lazy as _

TRUCK_TYPE = (
    ('تريلة سطحة','تريلة سطحة'),
    ('تريلة ستارة','تريلة ستارة'),
    ('تريلة جوانب','تريلة جوانب'),
    ('تريلة براد','تريلة براد'),
    ('لوري عايدي','لوري عايدي'),
    ('لوري براد','لوري براد'),
    ('دينه عايدي','دينه عايدي'),
    ('دينة براد','دينة براد'),
)


LANGUAHE = (
    ('ar','عربي'),
    ('en','انجليزية'),
    ('ur','اوردو'),
)

# Create your models here.
class Driver(models.Model):
    name = models.CharField(_("Driver Name"), max_length=120)
    phone = models.CharField(_("Driver Phone"), max_length=120)
    id_number = models.CharField(_("Driver Id Number"), max_length=10, null=True, blank=True)
    language = models.CharField(_("Driver Language"),  max_length=120, choices=LANGUAHE, null=True, blank=True)
    truck_type =models.CharField(_("Truck Type"), max_length=120, choices=TRUCK_TYPE, null=True, blank=True)
    rate = models.IntegerField(_("Rate"), null=True, blank=True)
    image_id = models.ImageField(_("Driver Image"), null=True, blank=True, upload_to='driver_image', default='driver_image/id_defult.png')


    def __str__(self) -> str:
        return self.name