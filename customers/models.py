from django.db import models
from django.core.validators import MaxLengthValidator
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email Required.")
        if not password:
            raise ValueError("Password Required.")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user 
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("Email Required.")
        if not password:
            raise ValueError("Password Required.")
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user 
    
class Vehicle(models.Model):
    VEHICLE_INFO_CHOICES = [ ('Year', 'Year'), ('Make', 'Make'), ('Model', 'Model')]
    SERVICES_CHOICES = [('Oil Change', 'Oil Change'), ('Repairs', 'Repairs'), ('Diagnostics', 'Diagnostics'), ('Roadside Assistance', 'Roadside Assistance')]

    year = models.CharField(max_length=4, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)

    services = models.CharField(max_length=50, choices=SERVICES_CHOICES, null=True, blank=True)

