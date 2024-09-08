from .serializers import ShipmentSerializer
from rest_framework import viewsets
from .models import Shipment


class ShipmentListApi(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer