from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "full_name",
            "phone_number",
            "email",
            "address",
        )

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Full Name",
                    "autocomplete": "name",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                    "autocomplete": "tel",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email (Optional)",
                    "autocomplete": "email",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Address",
                    "autocomplete": "street-address",
                }
            ),
        }


def clean_phone_number(self):
    phone = self.cleaned_data["phone_number"].strip()

    if not phone.isdigit():
        raise forms.ValidationError(
            "Phone number should contain only digits."
        )

    if len(phone) != 10:
        raise forms.ValidationError(
            "Phone number must contain exactly 10 digits."
        )

    return phone