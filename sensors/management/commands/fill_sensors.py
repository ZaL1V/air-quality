import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from sensors.models import SensorData


class Command(BaseCommand):
    def execute(self, *args, **options):
        timestamp = datetime.now() - timedelta(days=random.randint(1, 10))

        for _ in range(100):
            device_id = f'Device #{random.randint(1, 10)}'
            timestamp = timestamp + timedelta(minutes=random.randint(1, 59), seconds=random.randint(1, 59))
            SensorData.objects.create(
                device_id=device_id,
                timestamp=timestamp,
                pm25=random.uniform(12, 150),
                pm10=random.uniform(12, 150),
                co=random.uniform(10, 50),
                tvoc=random.uniform(1, 10),
                eco2=random.uniform(1, 10),
                co2=random.uniform(10, 50),
            )
