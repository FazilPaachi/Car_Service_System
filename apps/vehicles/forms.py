from django import forms

from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle

        exclude = (
            "id",
            "customer",
            "created_at",
            "updated_at",
            "is_active",
        )

        widgets = {
            "registration_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "KL09AB1234",
                    "autocomplete": "off",
                }
            ),
            "make": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Toyota",
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Corolla",
                }
            ),
            "variant": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "VX",
                }
            ),
            "manufacture_year": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "2022",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "fuel_type": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "transmission": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "White",
                }
            ),
            "odometer_reading": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "45000",
                }
            ),
            "engine_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "chassis_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }


def clean_registration_number(self):
    registration = (
        self.cleaned_data["registration_number"]
        .replace(" ", "")
        .strip()
        .upper()
    )

    return registration