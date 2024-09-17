from rest_framework import serializers
from .models import Customers, Branch

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    customers = CustomersSerializer(read_only=True)
    class Meta:
        model = Branch
        fields = '__all__'