# filter.py
from django_filters import rest_framework as filters
from .models import Shipment


class ShipmentFilter(filters.FilterSet):
    user = filters.CharFilter(
        field_name='user', method='filter_user', label='User ID')
    customer = filters.CharFilter(
        field_name='customer', method='filter_customer', label='Customer ID')
    status = filters.CharFilter(field_name='status',method='filter_status', label='Status')

    def filter_user(self, queryset, name, value):
        user_ids = value.split(',')
        return queryset.filter(user__id__in=user_ids)

    def filter_customer(self, queryset, name, value):
        customer_ids = value.split(',')
        return queryset.filter(customer_branch__id__in=customer_ids)
    def filter_status(self, queryset, name, value):
        status_ids = value.split(',')
        return queryset.filter(status__id__in=status_ids)

    class Meta:
        model = Shipment
        # Ensure 'user' is listed in the fields
        fields = ['status', 'user', 'customer']
