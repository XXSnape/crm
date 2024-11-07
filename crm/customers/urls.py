from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("", views.CustomersListView.as_view(), name="customers_list"),
    path("new/", views.CustomerCreateView.as_view(), name="customer_create"),
    path("<int:pk>/", views.CustomerDetailView.as_view(), name="customer_details"),
    path(
        "<int:pk>/delete/", views.CustomerDeleteView.as_view(), name="customer_delete"
    ),
    path("<int:pk>/edit/", views.CustomerUpdateView.as_view(), name="customer_update"),
]
