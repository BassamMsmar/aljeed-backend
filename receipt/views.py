from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import  Receipt
from shipments.models import Shipment

# Create your views here.

class ReceiptList(ListView):
    model = Receipt
    template_name = 'receipt/receipt_list.html'

class ReceiptCreate(CreateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'

    def get_initial(self):
        initial = super().get_initial()
        shipment_id = self.kwargs.get('shipment_id')  # Assuming you pass the shipment_id in URL
        shipment = Shipment.objects.get(pk=shipment_id)
        # Set initial values for the fields based on the specific shipment
        initial['shipment'] = shipment
        # You can set other initial values here if needed
        return initial

    def get_success_url(self):
        return reverse_lazy('receipt_detail', kwargs={'pk': self.object.pk})


class ReceiptUpdate(UpdateView):
    model = Receipt
    template_name = 'receipt/receipt_form.html'
    fields = '__all__'

class ReceiptDetail(DetailView):
    model = Receipt
    template_name = 'receipt/receipt_detail.html'