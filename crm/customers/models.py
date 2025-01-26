from contracts.models import Contract
from django.db import models
from django.urls import reverse
from leads.models import Lead


class Customer(models.Model):
    """Модель активного клиента"""

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, verbose_name="Клиент")
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, verbose_name="Контракт"
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("lead_id", "contract_id"),
                name="lead_contract_unique",
                violation_error_message="Клиент уже подписал этот контракт",
            ),
        )
        verbose_name = "Активный клиент"
        verbose_name_plural = "Активные клиенты"

    def get_absolute_url(self):
        """Генерирует ссылку для перехода к деталям модели"""
        return reverse(
            "customers:customer_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        """Генерирует строку для отображения"""
        return f"{self.lead.first_name} {self.lead.last_name}"
