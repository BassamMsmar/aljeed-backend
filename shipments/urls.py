from django.urls import path
from .views import ShipmentList, ShipmentsDetail,  ShipmentCreateView, Waybill




urlpatterns = [
    path('<str:status>', ShipmentList.as_view(), name='shipment_list'),
    path('<int:pk>/', ShipmentsDetail.as_view(), name='shipment_detail'),
    path('waybill/<int:pk>/', Waybill.as_view(), name='waybill_detail'),
    path('create/', ShipmentCreateView.as_view(), name='shipment_create'),

] 