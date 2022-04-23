from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver

class DriverAdmin(UserAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name', 'is_staff',
        'age', 'score', 'state', 'team', 'make', 'year'
        )

admin.site.register(Driver, DriverAdmin), 