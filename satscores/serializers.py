from rest_framework import serializers
from satscores.models import DriverSats, SatsScores

class DriverSatSerializer(serializers.ModelSerializer):
  class Meta:
    model = DriverSats
    fields = '__all__'

class SatScoresSerializer(serializers.ModelSerializer):
  class Meta:
    model = SatsScores
    fields = '__all__'