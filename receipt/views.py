from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.forms.models import model_to_dict

from shipments.models import Shipment
from .models import Receipt
from .forms import ReceiptForm
# Create your views here.



# Create your views here.

class ReceiptList(ListView):
    model = Receipt
    template_name = 'receipt/receipt_list.html'

class ReceiptCreate(CreateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'
  
 
    def get_success_url(self):
        return reverse_lazy('receipt_detail', kwargs={'pk': self.object.pk})
    

class ReceiptUpdate(UpdateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'

class ReceiptDetail(DetailView):
    model = Receipt
    template_name = 'receipt/receipt_detail.html'