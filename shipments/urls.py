from django.urls import path
from .views import ShipmentList, ShipmentsDetail,  ShipmentCreateView, waybill, change_stutus




urlpatterns = [
    path('<str:status>', ShipmentList.as_view(), name='shipment_list'),
    path('<int:pk>/', ShipmentsDetail.as_view(), name='shipment_detail'),
    path('change_stutus/<int:pk>/', change_stutus, name='change_stutus'),
    path('change_stutus_detail/<int:pk>/', change_stutus, name='change_stutus_detail'),
    path('waybill/<int:pk>/', waybill.as_view(), name='waybill_detail'),
    
    path('create/', ShipmentCreateView.as_view(), name='shipment_create'),

] 