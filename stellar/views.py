from sre_parse import State
from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DriverSerializer, VehicleDataSerializer
from .models import Driver, VehicleData

class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'team', 'make', 'year']

class VehicleDataView(viewsets.ModelViewSet):
    serializer_class = VehicleDataSerializer
    queryset = VehicleData.objects.all()
