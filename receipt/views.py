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
    
from django.shortcuts import render, get_object_or_404
from .forms import ReceiptForm
from .models import Shipment

def receipt_create_from_list(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    
    if request.method == 'POST':
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.shipment = shipment
            receipt.save()
            return redirect('receipt_list')
    else:
        # form = ReceiptForm()
        form = ReceiptForm(initial={'shipment': shipment})
    
    
    return render(request, 'receipt/receipt_form.html', {'form': form})

class ReceiptUpdate(UpdateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'

class ReceiptDetail(DetailView):
    model = Receipt
    template_name = 'receipt/receipt_detail.html'