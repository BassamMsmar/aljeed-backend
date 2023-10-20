from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Count


from .models import Customers, Branch

# Create your views here.
class CustomersList(ListView):
    model = Branch    #context : object_list, model_list
    queryset = Branch.objects.annotate(shipment_count=Count('shipments_company'))

class CustomersDetail(DetailView):
    model = Customers