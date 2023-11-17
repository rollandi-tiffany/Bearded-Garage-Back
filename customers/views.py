from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Vehicle
from .serializers import UserSerializer, VehicleSerializer
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    return HttpResponse('<h1>hello</h1')

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer