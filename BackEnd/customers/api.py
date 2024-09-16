from rest_framework import viewsets
from .serializers import BranchSerializer, CoustomresSerializer

from .models import Branch, Customers

class BranchViewSetApi(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer()