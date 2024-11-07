from django.contrib import admin

from .models import Customer


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    """Кастомизирует отображение модели активного клиента в админке"""

    list_display = "lead", "contract"
    list_display_links = ("lead",)
    list_editable = ("contract",)

    def get_queryset(self, request):
        return Customer.objects.select_related("lead", "contract")
