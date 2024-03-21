from django.urls import path

from .views import ReceiptList, ReceiptDetail, ReceiptCreate

urlpatterns = [
    path('receipt/', ReceiptList.as_view(), name='receipt_list'),
    path('receipt/create/', ReceiptCreate.as_view(), name='receipt_create', ),
    path('receipt/<int:pk>/', ReceiptDetail.as_view(), name='receipt_detail', ),
]
