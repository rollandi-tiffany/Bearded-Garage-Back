from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
#from rest_framework import routers
#from .views import UserViewSet
from . import views



urlpatterns = [
    
    path("signup", views.UserSignup.as_view(), name="signup"),
    path("login", views.UserLogin.as_view(), name="login"),
    path("logout", views.UserLogout.as_view(), name="logout"),
    path("user", views.UserView.as_view(), name="user"),
    path("vehicle", views.VehicleViewSet.as_view(), name="vehicle"),
   
]
