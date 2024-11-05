from django.apps import AppConfig


class CustomersConfig(AppConfig):
    verbose_name = "Активные клиенты"
    default_auto_field = "django.db.models.BigAutoField"
    name = "customers"
