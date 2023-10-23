from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count


from .models import Customers, Branch

# Create your views here.
class CustomersList(ListView):
    model = Customers    #context : object_list, model_list
    

class CustomersDetail(DetailView):
    model = Customers