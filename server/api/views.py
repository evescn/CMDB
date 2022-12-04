from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def aseet(request):
    # print(request.POST)
    data = json.loads(request.body.decode('utf-8'))
    print(data, type(data))
    return JsonResponse({'status': '200'})
