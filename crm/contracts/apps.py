from django.apps import AppConfig


class ContractsConfig(AppConfig):
    """Настройки приложения"""

    verbose_name = "Все контракты"
    default_auto_field = "django.db.models.BigAutoField"
    name = "contracts"
