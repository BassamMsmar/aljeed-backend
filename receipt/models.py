from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from shipments.models import Shipment




# Create your models here.
class Receipt(models.Model):
    user = models.ForeignKey(User,  related_name='receipts_user', on_delete=models.SET_NULL, null=True)
    shipment = models.ForeignKey(Shipment,  related_name='receipts_shipment', on_delete=models.SET_NULL, null=True)
    fare = models.IntegerField(_("Fare"), null=True, blank=True)
    premium = models.IntegerField(_("Premium"), null=True, blank=True)
    fare_return = models.IntegerField(_("Return"), null=True, blank=True)
    days_stayed = models.IntegerField(_("Days Stayed "), null=True, blank=True)
    stay_cost = models.IntegerField(_("Stay Cost") , null=True, blank=True)
    deducted = models.IntegerField(_("Deducted") , null=True, blank=True)
    create_at = models.DateTimeField(_("Create At"), default=timezone.now)
    code = models.ImageField(_("Receipt code"), blank=True, null=True, upload_to='receipt_code')
    total = models.IntegerField(_("Total"), default=0)
    compiled = models.BooleanField(_("Compiled"), default=False)



    def save(self, *args, **kwargs):
        # Generate QR code
        super().save(*args, **kwargs)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=4,
        )
        qr.add_data(f'http://127.0.0.1:8000/receite/{self.id}/')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code to image field
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        self.code.save(f'{self.id}_qrcode.png', File(buffer), save=False)

        self.total = (self.fare or 0) + (self.premium or 0) + (self.fare_return or 0) + (self.stay_cost or 0) - (self.deducted or 0)
        super().save(*args, **kwargs)

        
    def __str__(self):
            return str(self.id)




    

