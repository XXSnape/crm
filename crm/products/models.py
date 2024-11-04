from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Стоимость",
        validators=[MinValueValidator(Decimal("0.01"))],
    )

    def get_absolute_url(self):
        return reverse(
            "products:product_details",
            kwargs={"pk": self.pk},
        )
