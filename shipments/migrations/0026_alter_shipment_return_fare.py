# Generated by Django 4.2.6 on 2024-03-29 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0025_shipment_return_fare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='return_fare',
            field=models.IntegerField(blank=True, null=True, verbose_name='Return Fare'),
        ),
    ]
