from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
#from rest_framework import routers
#from .views import UserViewSet
from . import views



urlpatterns = [
    
    path("signup"),
    path("login"),
    path("logout"),
    path("user"),
    path("vehicle"),
   
]
