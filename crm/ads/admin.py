from django.contrib import admin
from django.http import HttpRequest

from .models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    """Кастомизирует отображение модели рекламы в админке"""

    list_display = "name", "budget", "product"
    list_editable = ("budget", "product")

    def get_queryset(self, request: HttpRequest):
        return Ads.objects.select_related("product")
