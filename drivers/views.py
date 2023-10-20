from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Driver

# Create your views here.
class DriverList(ListView):
    model = Driver 