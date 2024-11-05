from django.urls import path
from . import views

app_name = "contracts"

urlpatterns = [
    path("", views.ContractsListView.as_view(), name="contracts_list"),
    path("new/", views.ContractCreateView.as_view(), name="contract_create"),
    path("<int:pk>/", views.ContractDetailView.as_view(), name="contract_details"),
    path(
        "<int:pk>/delete/", views.ContractDeleteView.as_view(), name="contract_delete"
    ),
    path("<int:pk>/edit/", views.ContractUpdateView.as_view(), name="contract_update"),
]
