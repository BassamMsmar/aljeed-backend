# filter.py
from django_filters import rest_framework as filters 
from .models import Shipment


class ShipmentFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status')
    user = filters.CharFilter(field_name='user', method='filter_user')

    def filter_user(self, queryset, name, value):
        user_ids = value.split(',')
        return queryset.filter(user__id__in=user_ids)


    class Meta:
        model = Shipment
        fields = ['status', 'user']  # Ensure 'user' is listed in the fields
