from django.shortcuts import render
from django.views.generic import ListView

from shipments.models import Shipments

# Create your views here.
def home(request):
    # return render(request, 'base.html')
    shipments = Shipments.objects.all()
    recieved_shipment = Shipments.objects.all().filter(status='Recieved')
    processed_shipment = Shipments.objects.all().filter(status='Processed')
    shipped_shipment = Shipments.objects.all().filter(status='Shipped')
    delivered_shipment = Shipments.objects.all().filter(status='Delivered')
    feedback_shipment = Shipments.objects.all().filter(status='Feedback')
    late_shipment = Shipments.objects.all().filter(status='late')
    completed_shipment = Shipments.objects.all().filter(status='Completed')

    context = {
        'shipments':shipments,
        'recieved_shipment':recieved_shipment,
        'processed_shipment':processed_shipment,
        'shipped_shipment':shipped_shipment,
        'delivered_shipment':delivered_shipment,
        'feedback_shipment':feedback_shipment,
        'late_shipment':late_shipment,
        'completed_shipment':completed_shipment,
    }
    return render(request, 'settings/home.html', context)
