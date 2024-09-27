from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend




from .serializers import ShipmentSerializer
from .models import Shipment
from .filter import ShipmentFilter





class ShipmentListApi(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShipmentFilter
