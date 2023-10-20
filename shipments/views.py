from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Shipments
# Create your views here.

class ShipmentList(ListView):
    model = Shipments