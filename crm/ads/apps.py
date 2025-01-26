from django.apps import AppConfig


class AdsConfig(AppConfig):
    """Настройки приложения"""

    verbose_name = "Рекламные компании"
    default_auto_field = "django.db.models.BigAutoField"
    name = "ads"
