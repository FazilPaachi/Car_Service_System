from django.db import models

# Create your models here.
from apps.core.models import BaseModel
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r"^\+?[0-9]{8,15}$",
    message="Enter a valid phone number.",
)

class Customer(BaseModel):
    full_name = models.CharField(max_length=100, db_index=True)
    phone_number = models.CharField(max_length=15, unique=True, validators=[phone_validator])
    email = models.EmailField(blank=True)
    address = models.TextField(max_length=255, blank=True)

    class Meta:
        ordering = ["full_name"]
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"