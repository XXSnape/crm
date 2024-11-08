from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Product(models.Model):
    """Модель услуги"""

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Стоимость",
        validators=[MinValueValidator(Decimal("0"))],
    )

    def get_absolute_url(self):
        """Генерирует ссылку для перехода к деталям модели"""
        return reverse(
            "products:product_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        """Генерирует строку для отображения"""
        return self.name
