from django.urls import path

from .views import ReceiptList, ReceiptDetail, ReceiptCreate, ReceiptUpdate, create_receipt_from_list

urlpatterns = [
    path('', ReceiptList.as_view(), name='receipt_list'),
    path('create/', ReceiptCreate.as_view(), name='receipt_create', ),
    path('create_from_list/<int:pk>/', create_receipt_from_list, name='receipt_create_from_list', ),
    path('update/<int:pk>/', ReceiptUpdate.as_view(), name='receipt_update', ),
    path('<int:pk>/', ReceiptDetail.as_view(), name='receipt_detail', ),
]
