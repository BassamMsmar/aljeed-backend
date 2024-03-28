from django.urls import path

from .views import ReceiptList, ReceiptDetail, ReceiptCreate, receipt_create_from_list

urlpatterns = [
    path('', ReceiptList.as_view(), name='receipt_list'),
    path('create/', ReceiptCreate.as_view(), name='receipt_create', ),
    path('create_from_list/<int:pk>/', receipt_create_from_list, name='receipt_create_from_list', ),
    path('<int:pk>/', ReceiptDetail.as_view(), name='receipt_detail', ),
]
