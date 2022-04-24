from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, VehicleData

class DriverAdmin(UserAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name', 'is_staff',
        'age', 'score', 'state', 'team', 'make', 'year'
        )

class VechicleDataAdmin(admin.ModelAdmin):
    list_display = ('vin', 'speed', 'speedlimit', 'longitude', 'latitude')

admin.site.register(Driver, DriverAdmin)
admin.site.register(VehicleData, VechicleDataAdmin) 