from django.db import models

from apps.core.models import BaseModel
from apps.customers.models import Customer
from apps.vehicles.models import Vehicle

from .choices import Priority

from apps.accounts.models import User
from apps.services.models import Service
from .choices import JobStatus

# jon card model to store job card information

class JobCard(BaseModel):
    job_number = models.CharField(
        max_length=20,
        unique=True,
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="job_cards",
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name="job_cards",
    )

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.NORMAL,
    )

    remarks = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.job_number

# job card service model to link job card and service with additional fields

class JobCardService(BaseModel):
    job_card = models.ForeignKey(
        JobCard,
        on_delete=models.CASCADE,
        related_name="services",
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT,
    )

    technician = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"role": User.Roles.MECHANIC},
    )

    status = models.CharField(
        max_length=25,
        choices=JobStatus.choices,
        default=JobStatus.NOT_ASSIGNED,
    )

    remarks = models.TextField(blank=True)

    started_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        unique_together = ("job_card", "service")

    def __str__(self):
        return f"{self.job_card.job_number} - {self.service.name}"