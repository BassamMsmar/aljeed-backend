# Generated by Django 4.2.6 on 2024-03-21 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipments', '0019_shipment_status2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='status2',
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create At')),
                ('code', models.ImageField(blank=True, null=True, upload_to='receipt_code', verbose_name='Receipt code')),
                ('shipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipts_shipment', to='shipments.shipment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipts_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
