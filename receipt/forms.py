from django import forms

from .models import Receipt
from shipments.models import Shipment 
class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['user', 'shipment', 'total']  # Add or remove fields as needed

   