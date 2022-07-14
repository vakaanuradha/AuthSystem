from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import jwt

from .models import Installation
from .serializers import InstallationSerializer


def health_check(request):
    return JsonResponse("Authentication app")


@csrf_exempt
def installation_api(request):
    if request.method == 'POST':
        installation_data = JSONParser().parse(request)
        installation_serializer = InstallationSerializer(data=installation_data)
        if installation_serializer.is_valid():
            installation_serializer.save()

            installation = Installation.objects.get(advertising_id=installation_data['advertising_id'])
            installation_serializer = InstallationSerializer(installation)
            payload = installation_serializer.data
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
            installation.token = jwt_token['token']
            installation.save(update_fields=['token'])
            return JsonResponse(jwt_token,safe=False)



