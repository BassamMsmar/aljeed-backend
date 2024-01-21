from django.urls import path
from .views import ShipmentList, ShipmentCreateView




urlpatterns = [
    path('<str:status>', ShipmentList.as_view(), name='shipment_list'),
    path('create/', ShipmentCreateView.as_view(), name='shipment_create'),

]