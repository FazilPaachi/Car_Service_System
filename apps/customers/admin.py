from django.contrib import admin

# Register your models here.

from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone_number",
        "email",
        "is_active",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone_number",
        "email",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = ("full_name",)