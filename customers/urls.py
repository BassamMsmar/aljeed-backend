from django.urls import path
from .views import CustomersList, CustomersDetail




urlpatterns = [
    path('', CustomersList.as_view(), name='customers_list'),
    path('<int:pk>/', CustomersDetail.as_view(), name='customer_detail'),
]