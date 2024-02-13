from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models.aggregates import  Count

from .models import Customers, Branch
from shipments.models import Shipments


# Create your views here.
class CustomersList(ListView):
    model = Customers

    
    


class CustomersDetail(DetailView):
    model = Customers

    