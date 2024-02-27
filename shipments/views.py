from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from .models import Shipment
# Create your views here.


class ShipmentList(ListView):
    model = Shipment

    def get_queryset(self):
        # Get the status from the URL parameter, or default to 'All' if not provided
        status = self.kwargs.get('status', 'All')
        print(f'status = {status}')
        if status == 'All':
            # If 'All' is selected, return all shipments
            return Shipment.objects.all()
        else:
            # Filter shipments based on the selected status
            return Shipment.objects.filter(status=status)


class ShipmentsDetail(UpdateView):
    model = Shipment
    template_name = 'shipments/shipment_detail.html'
    fields = ['driver', 'customer_branch', 'fare', 'days_stayed', 'stay_cost', 'deducted',
              'status', 'destination', 'expected_arrival_date', 'actual_delivery_date']

    def get_success_url(self):
        return reverse('shipment_detail', kwargs={'pk': self.object.pk})


class waybill(DetailView):
    model = Shipment
    template_name = 'shipments/waybill.html'


class catch_receipt(DetailView):
    model = Shipment
    template_name = 'shipments/catch_receipt.html'


class ShipmentCreateView(CreateView):
    model = Shipment
    fields = ['driver', 'customer_branch', 'fare', 'premium', 'status', 'destination', 'expected_arrival_date']

    def form_valid(self, form):
        # Set the user field of the form with the current user
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('shipment_list', kwargs={'status': 'All'})
