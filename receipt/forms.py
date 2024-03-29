from django import forms
from .models import Receipt
from shipments.models import Shipment 
class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['fare', 'premium', 'fare_return', 'days_stayed', 'stay_cost', 'deducted' ]  # Add or remove fields as needed
