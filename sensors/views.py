import json

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from sensors.models import SensorData
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def receive_data(request:HttpRequest)->JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'message':'invalid request method'}, status=400)

    SensorData.objects.create(**json.loads(request.body))
    return JsonResponse({'message':'Succes'}, status=200)


def serialize_obj(data: SensorData) -> dict:
    return {
        'device_id': data.device_id,
        'timestamp': data.timestamp.isoformat() ,
        'pm25': str(data.pm25),
        'pm10': str(data.pm10),
        'co': str(data.co),
        'tvoc': str(data.tvoc),
        'eco2': str(data.eco2),
        'co2': str(data.co2),
    }


def charts(request: HttpRequest):
    device_id = request.GET.get('device', 'All')
    data = SensorData.objects.order_by('timestamp')
    data_points = []
    devices = []
    for o in data:
        if o.device_id not in devices:
            devices.append(o.device_id)

        if device_id != 'All' and device_id != o.device_id:
            continue
        data_points.append(serialize_obj(o))

    context = {'data_points': json.dumps(data_points), 'devices': sorted(devices),'selected': device_id}

    return render(request, 'sensors/charts.html', context=context)
