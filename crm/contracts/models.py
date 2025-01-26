import uuid
from datetime import datetime
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from products.models import Product


def contract_path(contract: "Contract", filename: str) -> str:
    """
    Генерирует путь до файла в базе данных
    :param contract:
    :param filename:
    :return:
    """
    return "contracts/contract_{pk}/{filename}".format(
        pk=contract.uuid, filename=filename
    )


def validate_end_date(value: datetime) -> datetime:
    """
    Проверяет, чтобы конечная дата была позже начальной
    :param value: дата завершения контракта
    :return: дата завершения контракта
    """
    if value.timestamp() < datetime.now().timestamp():
        raise ValidationError("Дата окончания контракта должна быть позже начала")
    return value


class UnarchivedManager(models.Manager):
    """Менеджер для выбора только неархивированных контрактов"""

    def get_queryset(self):
        return super().get_queryset().filter(archived=Contract.Status.UNARCHIVED)


class Contract(models.Model):
    """Модель контракта"""

    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"

    class Status(models.IntegerChoices):
        ARCHIVED = 1, "Недействителен"
        UNARCHIVED = 0, "Действителен"

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
    archived = models.BooleanField(
        choices=tuple(map(lambda c: (bool(c[0]), c[1]), Status.choices)),
        default=bool(Status.UNARCHIVED),
        verbose_name="Срок действия",
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    unarchived = UnarchivedManager()
    objects = models.Manager()

    def get_absolute_url(self):
        """Генерирует ссылку для перехода к деталям модели"""
        return reverse(
            "contracts:contract_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        """Генерирует строку для отображения"""
        return self.name
