from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Shipment, Receipt

# Create your views here.

class ReceiptList(ListView):
    model = Receipt
    template_name = 'shipments/catch_receipt.html'

class ReceiptCreate(CreateView):
    model = Shipment
    template_name = 'shipments/receipt.html'
    # fields = ['driver', 'customer_branch', 'fare', 'premium','status', 'destination', 'expected_arrival_date']

class ReceiptDetail(DetailView):
    model = Shipment
    template_name = 'shipments/receipt.html'