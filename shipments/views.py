from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Shipments
# Create your views here.

class ShipmentList(ListView):
    model = Shipments

    def get_queryset(self):
        # Get the status from the URL parameter, or default to 'All' if not provided
        status = self.kwargs.get('status', 'All')
        print( f'status = {status}')
        if status == 'All':
            # If 'All' is selected, return all shipments
            return Shipments.objects.all()
        else:
            # Filter shipments based on the selected status
            return Shipments.objects.filter(status=status)

