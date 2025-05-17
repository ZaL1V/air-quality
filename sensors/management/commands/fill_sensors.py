import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from sensors.models import SensorData


class Command(BaseCommand):
    def execute(self, *args, **options):
        SensorData.objects.all().delete()

        def bounds(value, minimum, maximum):
            return min(max(value, minimum), maximum)

        timestamp = datetime.now()
        pm25=random.uniform(12, 150)
        pm10=random.uniform(12, 150)
        co=random.uniform(10, 50)
        tvoc=random.uniform(1, 10)
        eco2=random.uniform(1, 10)
        co2=random.uniform(10, 50)

        for _ in range(1000):
            device_id = f'Device #{random.randint(1, 9)}'
            timestamp = timestamp + timedelta(minutes=random.randint(1, 59), seconds=random.randint(1, 59))
            pm25 = bounds(pm25 + random.uniform(-1, 1), 12, 150)
            pm10 = bounds(pm10 + random.uniform(-1, 1), 12, 150)
            co = bounds(co + random.uniform(-1, 1), 10, 50)
            tvoc = bounds(tvoc + random.uniform(-0.5, 0.5), 1, 10)
            eco2 = bounds(eco2 + random.uniform(-0.5, 0.5), 1, 10)
            co2 = bounds(co2 + random.uniform(-1, 1), 10, 50)

            SensorData.objects.create(
                device_id=device_id,
                timestamp=timestamp,
                pm25=pm25,
                pm10=pm10,
                co=co,
                tvoc=tvoc,
                eco2=eco2,
                co2=co2,
            )
