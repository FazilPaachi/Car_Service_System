from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
)
from django.contrib import messages
from .forms import CustomerForm
from .models import Customer

class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "customers:detail",
            kwargs={"pk": self.object.pk},
        )

def form_valid(self, form):
    response = super().form_valid(form)

    messages.success(
        self.request,
        f'Customer "{self.object.full_name}" created successfully.'
    )

    return response

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"

    def get_queryset(self):
        return Customer.objects.prefetch_related("vehicles")