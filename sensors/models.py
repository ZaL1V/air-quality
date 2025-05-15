from django.db import models



class SensorData(models.Model):
    device_id = models.CharField(max_length=128)
    timestamp = models.DateTimeField()    
    pm25 = models.DecimalField(max_digits=10, decimal_places=2)
    pm10 = models.DecimalField(max_digits=10, decimal_places=2)
    co = models.DecimalField(max_digits=10, decimal_places=2)
    tvoc = models.DecimalField(max_digits=10, decimal_places=2)
    eco2 = models.DecimalField(max_digits=10, decimal_places=2)
    co2 = models.DecimalField(max_digits=10, decimal_places=2)
