from django.urls import path
from .views import ShipmentList




urlpatterns = [
    path('', ShipmentList.as_view(), name='shipment_list'),
]