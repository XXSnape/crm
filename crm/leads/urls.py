from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("", views.LeadsListView.as_view(), name="leads_list"),
    path("new/", views.LeadCreateView.as_view(), name="lead_create"),
    path("<int:pk>/", views.LeadDetailView.as_view(), name="lead_details"),
    path("<int:pk>/delete/", views.LeadDeleteView.as_view(), name="lead_delete"),
    path("<int:pk>/edit/", views.LeadUpdateView.as_view(), name="lead_update"),
]
