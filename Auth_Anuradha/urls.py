
from django.urls import path
from . import views

urlpatterns = [
    path('health_check', views.health_check),
    path('v1/installation', views.installation_api),
]