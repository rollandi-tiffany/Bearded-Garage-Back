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
    path("vehicles/", views.VehicleViewSet.as_view({"get": "list", "post": "create"}), name="vehicle-list"),
    path("vehicles/<int:pk>/", views.VehicleViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="vehicle-detail")
   
]
