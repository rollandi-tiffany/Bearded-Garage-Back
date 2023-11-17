from django.db import models
from django.core.validators import MaxLengthValidator

class Vehicle(models.Model):
    VEHICLE_INFO_CHOICES = [ ('Year', 'Year'), ('Make', 'Make'), ('Model', 'Model')]
    SERVICES_CHOICES = [('Oil Change', 'Oil Change'), ('Repairs', 'Repairs'), ('Diagnostics', 'Diagnostics'), ('Roadside Assistance', 'Roadside Assistance')]

    year = models.CharField(max_length=4, null=True, blank=True)
    make = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)

    services = models.CharField(max_length=50, choices=SERVICES_CHOICES, null=True, blank=True)

