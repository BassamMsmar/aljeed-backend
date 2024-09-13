from django import forms

from .models import Shipment 
class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['fare', ]  # Add or remove fields as needed

   