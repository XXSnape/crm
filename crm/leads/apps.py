from django.apps import AppConfig


class LeadsConfig(AppConfig):
    """Настройки приложения"""

    verbose_name = "Потенциальные клиенты"
    default_auto_field = "django.db.models.BigAutoField"
    name = "leads"
