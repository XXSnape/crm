import os
import shutil

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from .forms import ContractForm
from .models import Contract


class ContractsListView(PermissionRequiredMixin, ListView):
    permission_required = "contracts.view_contract"
    queryset = Contract.unarchived.only("name")
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"


class ContractCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "contracts.add_contract"
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contracts_list")
    template_name = "contracts/contracts-create.html"


class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "contracts.delete_contract"
    model = Contract
    success_url = reverse_lazy("contracts:contracts_list")
    template_name = "contracts/contracts-delete.html"

    def form_valid(self, form):
        shutil.rmtree(self.object.file.path.rsplit("/", 1)[0])
        return super().form_valid(form)


class ContractDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "contracts.view_contract"
    queryset = Contract.objects.select_related("product")
    template_name = "contracts/contracts-detail.html"


class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "contracts.change_contract"
    queryset = Contract.objects.select_related("product")
    fields = "__all__"
    template_name = "contracts/contracts-edit.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        os.remove(self.get_object().file.path)
        return super().form_valid(form)
