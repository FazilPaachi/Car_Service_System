from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import CustomerCreateView



app_name = "customers"

urlpatterns = [

    path("", CustomerListView.as_view(), name="list"),
    path("new/", CustomerCreateView.as_view(), name="create"),
    path("<uuid:pk>/", CustomerDetailView.as_view(), name="detail"),
    # path("<uuid:pk>/edit/", CustomerUpdateView.as_view(), name="update"),
]