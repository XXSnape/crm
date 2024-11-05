from django.contrib import admin

from .models import Ads


@admin.register(Ads)
class CustomersAdmin(admin.ModelAdmin):
    list_display = "name", "budget", "product"
    list_editable = ("budget", "product")

    def get_queryset(self, request):
        return Ads.objects.select_related("product")
