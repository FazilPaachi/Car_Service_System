from django.db import models
from apps.core.models import BaseModel


class Service(BaseModel):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    estimated_duration = models.PositiveIntegerField(
        default=30,
        help_text="Estimated duration in minutes",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name