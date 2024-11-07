from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Настройки приложения"""

    verbose_name = "Все услуги"
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
