from django.db import models
from django.contrib.auth.models import AbstractUser

class Driver(AbstractUser):
    age = models.IntegerField(default=18)
    score = models.IntegerField(default=650)
    state = models.CharField(max_length=120, default="MI")
    team = models.IntegerField(blank=True, default=1001)
    make = models.CharField(max_length=120, default="Stellantis")
    year = models.IntegerField(default=2022)

class VehicleData(models.Model):
    vin = models.CharField(max_length=120)
    speed = models.DecimalField(max_digits=30, decimal_places=15)
    speedlimit = models.DecimalField(max_digits=30, decimal_places=15) 
    longitude = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)
    ABSIndLampStatus = models.IntegerField(default=0)
    AutomaticOilChange = models.IntegerField(default=0)
    Door_Ajar_Status = models.IntegerField(default=0)
    DriverBelt = models.IntegerField(default=0)
    FuelLvlLow = models.IntegerField(default=0)
    LowWasherFluid = models.IntegerField(default=0)
    MaintenanceReminderStatus = models.IntegerField(default=0)
    OilLifeSts = models.IntegerField(default=0)
    PresentGear = models.IntegerField(default=0)
    TransOverTemp = models.IntegerField(default=0)
    AvgFuelEcon = models.DecimalField(default=0.0, max_digits=30, decimal_places=15)
    EngineRPM = models.IntegerField(default=0)
    TirePressFL = models.IntegerField(default=0)
    TirePressFR = models.IntegerField(default=0)
    TirePressRL = models.IntegerField(default=0)
    TirePressRR = models.IntegerField(default=0)
    Altitude = models.IntegerField(default=0)
    ATMPressure = models.IntegerField(default=0)
    AverageTemp = models.IntegerField(default=0)
    Odometer = models.IntegerField(default=0)
    EngineCoolant = models.IntegerField(default=0)
    EngineOilTemp = models.IntegerField(default=0)
    SteeringWheelAngle = models.IntegerField(default=0)
    ExteriorTemperature = models.IntegerField(default=0)
    AverageTemp = models.IntegerField(default=0)
    TargetGear = models.IntegerField(default=0)
    TurnInd_LT_ON = models.IntegerField(default=0)
    TurnInd_RT_ON = models.IntegerField(default=0)

    def _str_(self):
        return self.vin
