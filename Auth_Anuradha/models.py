from django.db import models
from uuid import uuid4


class Installation(models.Model):
    __tablename__ = 'installation'
    id = models.UUIDField(primary_key=True, default=uuid4)
    advertising_id = models.CharField(max_length=255, unique=True)
    app_version = models.CharField(max_length=255)
    device_model = models.CharField(max_length=255)
    device_name = models.CharField(max_length=255)
    device_os = models.CharField(max_length=255)
    os_version = models.CharField(max_length=255)
    push_token = models.CharField(max_length=255)
    vendor_id = models.CharField(max_length=255)
    token = models.CharField(max_length=1000)

