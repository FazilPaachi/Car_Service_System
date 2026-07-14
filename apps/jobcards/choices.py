from django.db import models


class JobStatus(models.TextChoices):
    NOT_ASSIGNED = "NOT_ASSIGNED", "Not Assigned"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    WAITING_FOR_PARTS = "WAITING_FOR_PARTS", "Waiting for Parts"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"


class Priority(models.TextChoices):
    LOW = "LOW", "Low"
    NORMAL = "NORMAL", "Normal"
    HIGH = "HIGH", "High"
    URGENT = "URGENT", "Urgent"