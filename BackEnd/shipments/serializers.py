from rest_framework import serializers

from .models import Shipment, City, ShipmentStatus
from customers.models import Customers, Branch
from drivers.models import Driver
from django.contrib.auth.models import User


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id',]


class ShipmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentStatus
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['name']


class BranchSerializer(serializers.ModelSerializer):
    customers = CustomersSerializer(read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):

    destination = CitySerializer(read_only=True)
    customer_branch = BranchSerializer(read_only=True)
    driver = DriverSerializer(read_only=True)
    status = ShipmentStatusSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Shipment
        fields = '__all__'
