from .serializers import ShipmentSerializer
from rest_framework import generics
from .models import Shipment


class ShipmentListApi(generics.CreateAPIView):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer