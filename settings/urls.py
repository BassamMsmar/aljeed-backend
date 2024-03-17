from django.urls import path
from django.shortcuts import redirect

from .views import home


urlpatterns = [
    path('', home, name='home'),
   

]
