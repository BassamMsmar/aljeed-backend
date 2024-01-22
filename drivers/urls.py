from django.urls import path
from .views import DriverList, DriverCreateView




urlpatterns = [
    path('', DriverList.as_view(), name='driver_list'),
    path('create/', DriverCreateView.as_view(), name='driver_create'),

]