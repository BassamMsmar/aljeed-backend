from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.forms.models import model_to_dict
from num2words import num2words

from shipments.models import Shipment
from shipments.forms import ShipmentForm
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
    
def create_receipt_from_list(request, pk):
    shipment = get_object_or_404(Shipment, pk=pk)
    initial_data = {
        'fare': shipment.fare,
        'premium': shipment.premium,
        'fare_return': shipment.fare_return,
        'days_stayed': shipment.days_stayed,
        'stay_cost': shipment.stay_cost,
        'deducted': shipment.deducted,
        # إذا كانت القيم الباقية لها قيم افتراضية يجب إضافتها هنا
    }

    form_receipt = ReceiptForm(initial=initial_data)

    if request.method == 'POST':
        form_receipt = ReceiptForm(request.POST)

        if form_receipt.is_valid():
            receipt = form_receipt.save(commit=False)

            receipt.user = request.user
            print(receipt.user)
            receipt.shipment = shipment
            receipt.compiled = True
            receipt.save()


            shipment.fare = receipt.fare
            shipment.premium = receipt.premium
            shipment.fare_return = receipt.fare_return
            shipment.days_stayed = receipt.days_stayed
            shipment.stay_cost = receipt.stay_cost
            shipment.deducted = receipt.deducted
            shipment.status = 'Completed'
            shipment.save()
            
            return redirect('receipt_detail', pk=form_receipt.instance.pk)
        else:
            return render(request,'receipt/receipt_form_from_list.html', {'form_receipt': form_receipt,'shipment': shipment, })
    
    return render(request,'receipt/receipt_form_from_list.html', {'form_receipt': form_receipt,'shipment': shipment, })




class ReceiptUpdate(UpdateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'

class ReceiptDetail(DetailView):
    model = Receipt
    template_name = 'receipt/receipt_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_text = num2words(int(self.object.total ) , lang='ar')
        context['total_text'] = total_text
        return context