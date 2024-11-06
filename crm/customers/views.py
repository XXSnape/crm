from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from contracts.models import Contract
from .models import Customer


class CustomersListView(PermissionRequiredMixin, ListView):
    permission_required = "customers.view_customer"
    queryset = Customer.objects.select_related("lead").only(
        "lead__last_name", "lead__first_name"
    )
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "customers.add_customer"
    queryset = Customer.objects.select_related("lead", "contract").filter(
        contract__archived=Contract.Status.UNARCHIVED
    )
    fields = "__all__"
    success_url = reverse_lazy("customers:customers_list")
    template_name = "customers/customers-create.html"


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "customers.delete_customer"
    model = Customer
    success_url = reverse_lazy("customers:customers_list")
    template_name = "customers/customers-delete.html"


class CustomerDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "customers.view_customer"
    queryset = Customer.objects.select_related("lead")
    template_name = "customers/customers-detail.html"


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "customers.change_customer"
    queryset = Customer.objects.select_related("lead", "contract")
    fields = "__all__"
    template_name = "customers/customers-edit.html"
