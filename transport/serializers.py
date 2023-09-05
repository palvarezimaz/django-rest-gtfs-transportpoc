from rest_framework import serializers
from .models import Stops, Trips, StopTimes


class StopsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Stops
    fields = '__all__'


class ArrivalTimesSerializer(serializers.Serializer):
  trip_id = serializers.CharField()
  arrival_time = serializers.CharField()

  class Meta:
    model = StopTimes
    fields = '__all__'


class TripsSerializer(serializers.ModelSerializer):
  service = serializers.CharField()
  trip_id = serializers.CharField()
  route_direction = serializers.CharField()

  class Meta:
    model = Trips
    fields = ['service', 'trip_id', 'route_direction']