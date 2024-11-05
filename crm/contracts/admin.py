from django.contrib import admin

from .models import Contract


@admin.register(Contract)
class CustomersAdmin(admin.ModelAdmin):
    list_display = "name", "cost", "start_date", "end_date", "file", "product"
    list_display_links = ("name",)
    list_editable = ("cost", "end_date", "file", "product")

    def get_queryset(self, request):
        return Contract.objects.select_related("product")
