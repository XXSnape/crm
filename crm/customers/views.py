from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Customer


class CustomersListView(ListView):
    queryset = Customer.objects.select_related("lead").only(
        "lead__last_name", "lead__first_name"
    )
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomerCreateView(CreateView):
    queryset = Customer.objects.select_related("lead", "contract")
    fields = "__all__"
    success_url = reverse_lazy("customers:customers_list")
    template_name = "customers/customers-create.html"


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy("customers:customers_list")
    template_name = "customers/customers-delete.html"


class CustomerDetailView(DetailView):
    queryset = Customer.objects.select_related("lead")
    template_name = "customers/customers-detail.html"


class CustomerUpdateView(UpdateView):
    queryset = Customer.objects.select_related("lead", "contract")
    fields = "__all__"
    template_name = "customers/customers-edit.html"
