from rest_framework import viewsets
from .serializers import BranchSerializer, CustomersSerializer

from .models import Branch, Customers


class CustomersViewSetApi(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class BranchViewSetApi(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer