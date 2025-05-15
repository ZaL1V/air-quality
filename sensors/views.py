
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from sensors.models import SensorData
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_data(request:HttpRequest)->JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'message':'invalid request method'}, status=400)
    
    SensorData.objects.create(**json.loads(request.body))
    return JsonResponse({'message':'Succes'}, status=200)
