from .models import DriverSats, SatsScores
from rest_framework import viewsets, permissions
from .serializers import DriverSatSerializer, SatScoresSerializer


class DriverViewSet(viewsets.ModelViewSet):
  queryset = DriverSats.objects.all()
  permissions_classes = []
  serializer_class = DriverSatSerializer

class SatScoreViewSet(viewsets.ModelViewSet):
  queryset = SatsScores.objects.all()
  permissions_classes = []
  serializer_class = SatScoresSerializer