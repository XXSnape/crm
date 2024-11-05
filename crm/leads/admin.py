from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadsAdmin(admin.ModelAdmin):
    list_display = "first_name", "last_name", "phone", "email", "ad"
    list_editable = ("ad",)

    def get_queryset(self, request):
        return Lead.objects.select_related("ad")
