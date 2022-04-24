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
    # absindlampstatus
    # automaticoilchange
    # doorajarstatus
    # DriverBelt
    # FuelLvlLow
    # LowWasherFluid
    # MaintenanceReminderStatus
    # OilLifeSts
    # PresentGear
    # TransOverTemp
    # AvgFuelEcon
    # EngineRPM
    # TirePressFL
    # TirePressFR
    # TirePressRL
    # TirePressRR
    # Altitude
    # ATMPressure
    # AverageTemp
    # Odometer
    # EngineCoolant
    # EngineOilTemp
    # SteeringWheelAngle
    # ExteriorTemperature
    # AverageTemp
    # TargetGear
    # TurnInd_LT_ON
    # TurnInd_RT_ON

    def _str_(self):
        return self.vin
