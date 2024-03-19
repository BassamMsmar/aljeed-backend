from django.shortcuts import render, redirect
from django.views.generic import ListView

from shipments.models import Shipment

# Create your views here.
def home(request):
    if request.user.is_authenticated and request.user.is_superuser:
    # return render(request, 'base.html')
        shipments = Shipment.objects.select_related('driver', 'customer_branch', 'user').all().order_by('-create_at')
        recieved_shipment = Shipment.objects.get(status__status='Recieved')
        processed_shipment = Shipment.objects.all().filter(status__status='Processed')
        shipped_shipment = Shipment.objects.all().filter(status__status='Shipped')
        delivered_shipment = Shipment.objects.all().filter(status__status='Delivered')
        feedback_shipment = Shipment.objects.all().filter(status__status='Feedback')
        late_shipment = Shipment.objects.all().filter(status__status='late')
        completed_shipment = Shipment.objects.all().filter(status__status='Completed')

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

    elif request.user.is_authenticated :
            return redirect('shipment_list', status='All')
    
    else:
        return redirect('login')
        
    
