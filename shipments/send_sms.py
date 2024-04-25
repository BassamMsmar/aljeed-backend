from django.shortcuts import render
from shipments.models import Shipment



def send_sms(request, status):
    shipments = Shipment.objects.all()

    
    return render(request, 'shipments/send_sms.html', {'shipments': shipments})