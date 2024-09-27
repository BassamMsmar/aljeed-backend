# filter.py
from django_filters import rest_framework as filters 
from .models import Shipment


class ShipmentFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status')
    user = filters.CharFilter(field_name='user')


    class Meta:
        model = Shipment
        fields = ['status', 'user']  # Ensure 'user' is listed in the fields
