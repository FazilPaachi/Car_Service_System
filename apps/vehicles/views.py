from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from apps.customers.models import Customer

from .forms import VehicleForm
from .models import Vehicle


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicles/vehicle_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.customer = get_object_or_404(
            Customer,
            pk=kwargs["customer_pk"],
            is_active=True,
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.customer = self.customer

        response = super().form_valid(form)

        messages.success(
            self.request,
            "Vehicle added successfully.",
        )

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = self.customer
        return context

    def get_success_url(self):
        return reverse(
            "customers:detail",
            kwargs={"pk": self.customer.pk},
        )