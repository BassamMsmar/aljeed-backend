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

        super().save(*args, **kwargs)