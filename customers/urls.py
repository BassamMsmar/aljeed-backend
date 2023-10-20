from django.urls import path
from .views import CustomersList




urlpatterns = [
    path('', CustomersList.as_view(), name='customers_list'),
]