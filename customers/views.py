from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Customers, Branch

# Create your views here.
class CustomersList(ListView):
    model = Branch    #context : object_list, model_list


class CustomersDetail(DetailView):
    model = Customers