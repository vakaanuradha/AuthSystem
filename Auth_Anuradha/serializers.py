from rest_framework import serializers
from .models import Installation


class InstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installation
        fields = ('id', 'advertising_id', 'app_version', 'device_model', 'device_name',
                  'device_os', 'os_version', 'push_token', 'vendor_id')

