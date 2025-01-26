# Generated by Django 5.1.2 on 2024-11-06 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contracts", "0001_initial"),
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contracts.contract",
                        verbose_name="Контракт",
                    ),
                ),
                (
                    "lead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="leads.lead",
                        verbose_name="Клиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Активный клиент",
                "verbose_name_plural": "Активные клиенты",
                "constraints": [
                    models.UniqueConstraint(
                        fields=("lead_id", "contract_id"),
                        name="lead_contract_unique",
                        violation_error_message="Клиент уже подписал этот контракт",
                    )
                ],
            },
        ),
    ]
