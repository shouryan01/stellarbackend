from rest_framework import serializers
from .models import Driver, VehicleData

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'username', 'age', 'score', 'state', 'team', 'make', 'year', 'groups')

class VehicleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleData
        fields = (
                "vin",
                "speed",
                "speedlimit",
                "ABSIndLampStatus",
                "AutomaticOilChange",
                "Door_Ajar_Status",
                "DriverBelt",
                "FuelLvlLow",
                "LowWasherFluid",
                "MaintenanceReminderStatus",
                "OilLifeSts",
                "PresentGear",
                "TransOverTemp",
                "AvgFuelEcon",
                "EngineRPM",
                "TirePressFL",
                "TirePressFR",
                "TirePressRL",
                "TirePressRR",
                "Altitude",
                "ATMPressure",
                "AverageTemp",
                "Odometer",
                "latitude",
                "longitude",
                "EngineCoolant",
                "EngineOilTemp",
                "SteeringWheelAngle",
                "ExteriorTemperature",
                "AverageTemp",
                "TargetGear",
                "TurnInd_LT_ON",
                "TurnInd_RT_ON")