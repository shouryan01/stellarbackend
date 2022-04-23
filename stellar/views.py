from sre_parse import State
from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DriverSerializer
from .models import Driver

# Create your views here.

class DriverView(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'team', 'make', 'year']
