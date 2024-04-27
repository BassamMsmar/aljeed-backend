# Generated by Django 4.2.6 on 2024-03-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0002_receipt_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='days_stayed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Days Stayed '),
        ),
        migrations.AddField(
            model_name='receipt',
            name='deducted',
            field=models.IntegerField(blank=True, null=True, verbose_name='Deducted'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='fare',
            field=models.IntegerField(default=0, verbose_name='Fare'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='fare_return',
            field=models.IntegerField(blank=True, null=True, verbose_name='Return'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='premium',
            field=models.IntegerField(blank=True, null=True, verbose_name='Premium'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='stay_cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Stay Cost'),
        ),
    ]
