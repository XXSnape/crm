from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse
from products.models import Product


class Ads(models.Model):
    """Модель рекламной компании"""

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

    name = models.CharField(max_length=128, verbose_name="Название")
    promotion_channel = models.CharField(
        max_length=128, verbose_name="Канал продвижения"
    )
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Бюджет",
        validators=[
            MinValueValidator(Decimal("0"), message="Минимальное значение - 0")
        ],
    )
    product = ForeignKey(
        Product, on_delete=models.CASCADE, related_name="ads", verbose_name="Услуга"
    )

    def get_absolute_url(self):
        """Генерирует ссылку для перехода к деталям модели"""
        return reverse(
            "ads:ads_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        """Генерирует строку для отображения"""
        return self.name
