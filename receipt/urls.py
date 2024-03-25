from django.urls import path

from .views import ReceiptList, ReceiptDetail, ReceiptCreate

urlpatterns = [
    path('', ReceiptList.as_view(), name='receipt_list'),
    path('create/', ReceiptCreate.as_view(), name='receipt_create', ),
    path('<int:pk>/', ReceiptDetail.as_view(), name='receipt_detail', ),
]
