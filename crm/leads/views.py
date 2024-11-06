from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Lead


class LeadsListView(PermissionRequiredMixin, ListView):
    permission_required = "leads.view_lead"
    queryset = Lead.objects.only("first_name", "last_name").all()
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "leads.add_lead"
    queryset = Lead.objects.select_related("ad")
    fields = "__all__"
    success_url = reverse_lazy("leads:leads_list")
    template_name = "leads/leads-create.html"


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "leads.delete_lead"
    model = Lead
    success_url = reverse_lazy("leads:leads_list")
    template_name = "leads/leads-delete.html"


class LeadDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "leads.view_lead"
    queryset = Lead.objects.select_related("ad")
    template_name = "leads/leads-detail.html"


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "leads.change_lead"
    queryset = Lead.objects.select_related("ad")
    fields = "__all__"
    template_name = "leads/leads-edit.html"
