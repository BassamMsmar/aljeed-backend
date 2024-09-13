from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Driver


from .models import Driver

# Create your views here.
class DriverList(ListView):
    model = Driver 

class DriverCreateView(CreateView):
    model = Driver
    fields = ['name', 'phone', 'id_number', 'language', 'truck_type']

    def get_success_url(self):
        return reverse_lazy('driver_list')