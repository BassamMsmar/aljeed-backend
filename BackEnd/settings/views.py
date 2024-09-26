from django.shortcuts import render, redirect
from django.views.generic import ListView

from shipments.models import Shipment, ShipmentStatus
import easyaudit

# Create your views here.


def home(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # return render(request, 'base.html')
        shipments = Shipment.objects.select_related(
            'driver', 'customer_branch', 'user').all().order_by('-created_at')

        # احصل على كائن ShipmentStatus لكل حالة
        shipped_status = ShipmentStatus.objects.get(name_en='Shipped')
        delivered_status = ShipmentStatus.objects.get(name_en='Delivered')
        feedback_status = ShipmentStatus.objects.get(name_en='Feedback')
        late_status = ShipmentStatus.objects.get(name_en='Late')

        # استخدم الكائنات المأخوذة في التصفية
        Shipped_shipment = Shipment.objects.filter(status=shipped_status)
        delivered_shipment = Shipment.objects.filter(status=delivered_status)
        feedback_shipment = Shipment.objects.filter(status=feedback_status)
        late_shipment = Shipment.objects.filter(status=late_status)

        context = {
            'shipments': shipments,
            'Shipped_shipment': Shipped_shipment,
            'delivered_shipment': delivered_shipment,
            'feedback_shipment': feedback_shipment,
            'late_shipment': late_shipment,
        }
        return render(request, 'settings/home.html', context)

    elif request.user.is_authenticated:
        return redirect('shipment_list', status='All')

    else:
        return redirect('login')
