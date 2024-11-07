from ads.models import Ads
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Lead(models.Model):
    """Модель потенциального клиента"""

    class Meta:
        verbose_name = "Клиенты"
        verbose_name_plural = "Клиенты"

    first_name = models.CharField(max_length=64, verbose_name="Имя")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия")
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Номер телефона должен быть в формате: '+999999999'. Не больше 15 цифр.",
            )
        ],
        verbose_name="Номер телефона",
    )
    email = models.EmailField(max_length=64, verbose_name="Почта")
    ad = models.ForeignKey(
        Ads,
        null=True,
        on_delete=models.SET_NULL,
        related_name="leads",
        verbose_name="Рекламная компания",
    )

    def get_absolute_url(self):
        """Генерирует ссылку для перехода к деталям модели"""
        return reverse(
            "leads:lead_details",
            kwargs={"pk": self.pk},
        )

    def __str__(self) -> str:
        """Генерирует строку для отображения"""
        return f"{self.last_name} {self.first_name}"
