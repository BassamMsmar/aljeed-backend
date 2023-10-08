from django.db import models

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
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    id_number = models.CharField(max_length=10, null=True, blank=True)
    language = models.CharField( max_length=120, choices=LANGUAHE, null=True, blank=True)
    truck_type =models.CharField(max_length=120, choices=TRUCK_TYPE, null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name