from django.urls import path

from .views import ReceiptList, ReceiptDetail, ReceiptCreate, ReceiptUpdate

urlpatterns = [
    path('', ReceiptList.as_view(), name='receipt_list'),
    path('create/', ReceiptCreate.as_view(), name='receipt_create', ),
    path('update/<int:pk>/', ReceiptUpdate.as_view(), name='receipt_update', ),
    path('<int:pk>/', ReceiptDetail.as_view(), name='receipt_detail', ),
]
