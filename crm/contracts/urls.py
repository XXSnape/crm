from django.urls import path
from . import views

app_name = "contracts"

urlpatterns = [path("", views.show_contracts)]
