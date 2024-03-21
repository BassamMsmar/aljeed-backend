from django.urls import path
from .views import ShipmentList, ShipmentsDetail,  ShipmentCreateView, waybill, catch_receipt, ShipmentReceipt




urlpatterns = [
    path('<str:status>', ShipmentList.as_view(), name='shipment_list'),
    path('<int:pk>/', ShipmentsDetail.as_view(), name='shipment_detail'),
    path('waybill/<int:pk>/', waybill.as_view(), name='waybill_detail'),
    path('catch_receipt/<int:pk>/', catch_receipt.as_view(), name='catch_receipt'),
    path('create/', ShipmentCreateView.as_view(), name='shipment_create'),
    path('receipt/', ShipmentReceipt.as_view(), name='receipt_create'),

] 