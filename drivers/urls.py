from django.urls import path
from .views import DriverList




urlpatterns = [
    path('', DriverList.as_view(), name='driver_list'),
]