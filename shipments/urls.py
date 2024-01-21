from django.urls import path
from .views import ShipmentList




urlpatterns = [
    path('<str:status>', ShipmentList.as_view(), name='shipment_list'),
]