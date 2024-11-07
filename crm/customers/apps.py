from django.apps import AppConfig


class CustomersConfig(AppConfig):
    """Настройки приложения"""

    verbose_name = "Активные клиенты"
    default_auto_field = "django.db.models.BigAutoField"
    name = "customers"
