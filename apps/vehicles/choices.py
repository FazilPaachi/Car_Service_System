from django.db import models


class VehicleCategory(models.TextChoices):
    HATCHBACK = "HATCHBACK", "Hatchback"
    SEDAN = "SEDAN", "Sedan"
    SUV = "SUV", "SUV"
    MUV = "MUV", "MUV"
    PICKUP = "PICKUP", "Pickup"
    VAN = "VAN", "Van"
    TRUCK = "TRUCK", "Truck"
    BUS = "BUS", "Bus"


class FuelType(models.TextChoices):
    PETROL = "PETROL", "Petrol"
    DIESEL = "DIESEL", "Diesel"
    CNG = "CNG", "CNG"
    ELECTRIC = "ELECTRIC", "Electric"
    HYBRID = "HYBRID", "Hybrid"


class Transmission(models.TextChoices):
    MANUAL = "MANUAL", "Manual"
    AUTOMATIC = "AUTOMATIC", "Automatic"