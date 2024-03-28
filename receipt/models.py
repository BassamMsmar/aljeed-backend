from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import qrcode
from io import BytesIO
from django.core.files import File

from django.utils.translation import gettext_lazy as _
from shipments.models import Shipment




# Create your models here.
class Receipt(models.Model):
    user = models.ForeignKey(User,  related_name='receipts_user', on_delete=models.SET_NULL, null=True)
    shipment = models.ForeignKey(Shipment,  related_name='receipts_shipment', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(_("Create At"), default=timezone.now)
    code = models.ImageField(_("Receipt code"), blank=True, null=True, upload_to='receipt_code')
    total = models.IntegerField(_("Total"), default=0)



    def save(self, *args, **kwargs):
        # Generate QR code
        super().save(*args, **kwargs)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=4,
            border=4,
        )
        qr.add_data(f'http://127.0.0.1:8000/shipment/catch_receipt/{self.id}/')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code to image field
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        self.code.save(f'{self.id}_qrcode.png', File(buffer), save=False)

        
        if self.shipment:
            fare = self.shipment.fare or 0
            premium = self.shipment.premium or 0
            fare_return = self.shipment.fare_return or 0
            stay_cost = self.shipment.stay_cost or 0
            deducted = self.shipment.deducted or 0

            self.total = fare + premium + fare_return + stay_cost - deducted
                

        super().save(*args, **kwargs)


    def __str__(self):
            return str(self.id)