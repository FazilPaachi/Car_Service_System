from django.contrib import admin
from .models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "registration_number",
        "customer",
        "make",
        "model",
        "category",
        "fuel_type",
        "is_active",
    )

    search_fields = (
        "full_name",
        "phone_number",
        "registration_number",
        "make",
        "model",
        "customer__full_name",
        "customer__phone_number",
    )

    list_filter = (
        "category",
        "fuel_type",
        "transmission",
        "is_active",
    )

    autocomplete_fields = ("customer",)

    ordering = ("registration_number",)