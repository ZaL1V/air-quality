from django.contrib import admin
from sensors.models import SensorData

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display=[
        'id', 'device_id', "timestamp", "pm25", "pm10", "co", "tvoc", "eco2", "co2"
    ]
