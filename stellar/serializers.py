from rest_framework import serializers
from .models import Driver, VehicleData

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'username', 'age', 'score', 'state', 'team', 'make', 'year', 'groups')

class VehicleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleData
        fields = ('id', 'vin', 'speed', 'speedlimit', 'longitude', 'latitude')