from django.db import models
from apps.core.models import BaseModel
from apps.customers.models import Customer
from .choices import (
    VehicleCategory,
    FuelType,
    Transmission,
)

from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date


class Vehicle(BaseModel):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="vehicles",
    )

    registration_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        help_text="Vehicle registration number",
    )
    make = models.CharField(max_length=50)

    model = models.CharField(max_length=50)

    variant = models.CharField(
        max_length=50,
        blank=True,
    )

    manufacture_year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(date.today().year + 1),
        ],
        null=True,
        blank=True,
        help_text="year of manufacture(YYYY)",
    )

    color = models.CharField(
        max_length=30,
        blank=True,
        help_text="Vehicle color",  
    )

    category = models.CharField(
        max_length=20,
        choices=VehicleCategory.choices,
        
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FuelType.choices,
        blank=True,
    )

    transmission = models.CharField(
        max_length=20,
        choices=Transmission.choices,
        blank=True,
    )

    odometer_reading = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Current odometer reading",
    )

    chassis_number = models.CharField(
        max_length=50,
        blank=True,
    )

    engine_number = models.CharField(
        max_length=50,
        blank=True,
    )


    def save(self, *args, **kwargs):
        if self.registration_number:
            self.registration_number = (
                self.registration_number
                    .replace(" ", "")
                    .strip()
                    .upper()
                )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["registration_number"]
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return f"{self.registration_number} - {self.make} {self.model}"

@property

def display_name(self):
    return f"{self.make} {self.model}"