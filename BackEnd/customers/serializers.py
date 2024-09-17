from rest_framework import serializers
from .models import Customers, Branch

class CoustomresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'