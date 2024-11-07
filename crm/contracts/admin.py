from django.contrib import admin
from django.http import HttpRequest

from .models import Contract


@admin.register(Contract)
class ContractsAdmin(admin.ModelAdmin):
    """Кастомизирует отображение модели контракта в админке"""

    list_display = (
        "name",
        "cost",
        "start_date",
        "end_date",
        "file",
        "product",
        "archived",
    )
    list_display_links = ("name",)
    list_editable = ("cost", "end_date", "file", "product")

    def get_queryset(self, request: HttpRequest):
        return Contract.objects.select_related("product")
