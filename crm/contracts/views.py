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


class ContractsListView(ListView):
    queryset = Contract.objects.only("name").all()
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"


class ContractCreateView(CreateView):
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contracts_list")
    template_name = "contracts/contracts-create.html"


class ContractDeleteView(DeleteView):
    model = Contract
    success_url = reverse_lazy("contracts:contracts_list")
    template_name = "contracts/contracts-delete.html"


class ContractDetailView(DetailView):
    queryset = Contract.objects.select_related("product")
    template_name = "contracts/contracts-detail.html"


class ContractUpdateView(UpdateView):
    queryset = Contract.objects.select_related("product")
    fields = "__all__"
    template_name = "contracts/contracts-edit.html"
