from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    """Кастомизирует отображение модели услуги в админке"""

    list_display = "name", "description", "cost"
    list_editable = ("cost",)
