from django.db.models import Q
from django.views.generic import ListView

from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        queryset = Customer.objects.prefetch_related("vehicles")

        query = self.request.GET.get("q")

        if not query:
            return queryset.none()

        return queryset.filter(
            Q(full_name__icontains=query)
            | Q(phone_number__icontains=query)
            | Q(vehicles__registration_number__icontains=query)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context