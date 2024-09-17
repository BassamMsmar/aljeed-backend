from django.urls import path ,include
from .views import CustomersList, CustomersDetail


from rest_framework import routers

from customers import api
router = routers.DefaultRouter()
router.register('customers', api.CustomersViewSetApi)
router.register('branch', api.BranchViewSetApi)


urlpatterns = [
    path('', CustomersList.as_view(), name='customers_list'),
    path('<int:pk>/', CustomersDetail.as_view(), name='customer_detail'),

    #api 
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),




]