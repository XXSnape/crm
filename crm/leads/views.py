from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Lead


class LeadsListView(ListView):
    queryset = Lead.objects.only("first_name", "last_name").all()
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadCreateView(CreateView):
    queryset = Lead.objects.select_related("ad")
    fields = "__all__"
    success_url = reverse_lazy("leads:leads_list")
    template_name = "leads/leads-create.html"


class LeadDeleteView(DeleteView):
    model = Lead
    success_url = reverse_lazy("leads:leads_list")
    template_name = "leads/leads-delete.html"


class LeadDetailView(DetailView):
    queryset = Lead.objects.select_related("ad")
    template_name = "leads/leads-detail.html"


class LeadUpdateView(UpdateView):
    queryset = Lead.objects.select_related("ad")
    fields = "__all__"
    template_name = "leads/leads-edit.html"
