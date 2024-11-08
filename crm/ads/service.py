from decimal import Decimal

from ads.models import Ads
from contracts.models import Contract
from customers.models import Customer
from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from leads.models import Lead


def get_statistic() -> dict[str, list[dict[str, int | float]]]:
    """
    Проходится по всем рекламным компаниям,
    считает клиентов, привлеченных компанией,
    находит контракты, заключенные с услугой, которая заказывала рекламу,
    делит стоимость всех подписанных контрактов на бюджет рекламы

    :return словарь с данными
    """
    ads_models = Ads.objects.select_related("product").all()
    ads = []
    for ad in ads_models:
        leads_count = Lead.objects.filter(ad_id=ad.pk).aggregate(count=Count("pk"))[
            "count"
        ]
        contracts_pk = Contract.objects.filter(product_id=ad.product_id).values_list(
            "pk", flat=True
        )
        result = (
            Customer.objects.filter(contract_id__in=contracts_pk)
            .prefetch_related("contract")
            .aggregate(
                count=Coalesce(Count("lead_id", distinct=True), 0),
                summa=Coalesce(Sum("contract__cost"), Decimal("0")),
            )
        )

        ads.append(
            {
                "name": ad.name,
                "leads_count": leads_count,
                "customers_count": result.get("count"),
                "profit": round(result.get("summa") / ad.budget, 2),
            }
        )
    return {"ads": ads}
