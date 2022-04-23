from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'username', 'age', 'score', 'state', 'team', 'make', 'year', 'groups')