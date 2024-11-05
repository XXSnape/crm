import uuid
from datetime import datetime
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

from products.models import Product


def contract_path(contract: "Contract", filename: str) -> str:
    return "contracts/contract_{pk}/{filename}".format(
        pk=contract.uuid, filename=filename
    )


def validate_end_date(value: datetime):
    if value.timestamp() < datetime.now().timestamp():
        raise ValidationError("Дата окончания контракта должна быть позже начала")
    return value


class Contract(models.Model):
    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    name = models.CharField(max_length=128, verbose_name="Название")
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="contracts",
        verbose_name="Услуга",
    )
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заключения")
    end_date = models.DateTimeField(
        verbose_name="Действует до", validators=[validate_end_date]
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0"), message="Минимальное значение - 0")
        ],
        verbose_name="Сумма",
    )
    file = models.FileField(null=True, upload_to=contract_path, verbose_name="Документ")

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def get_absolute_url(self):
        return reverse(
            "contracts:contract_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        return f"{self.name}"
