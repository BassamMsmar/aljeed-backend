from rest_framework import viewsets
from .serializers import BranchSerializer, CoustomresSerializer

from .models import Branch, Customers


class CustomersViewSetApi(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CoustomresSerializer


class BranchViewSetApi(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer