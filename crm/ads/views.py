from decimal import Decimal

from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead
from .models import Ads


class AdsListView(ListView):
    queryset = Ads.objects.only("name").all()
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsCreateView(CreateView):
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-create.html"


class AdsDeleteView(DeleteView):
    model = Ads
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-delete.html"


class AdsDetailView(DetailView):
    queryset = Ads.objects.select_related("product")
    template_name = "ads/ads-detail.html"


class AdsUpdateView(UpdateView):
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    template_name = "ads/ads-edit.html"


class StatisticsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        ads_models = Ads.objects.select_related("product").all()
        ads = []
        for ad in ads_models:
            leads_count = Lead.objects.filter(ad_id=ad.pk).aggregate(count=Count("pk"))[
                "count"
            ]
            contracts_pk = Contract.objects.filter(
                product_id=ad.product_id
            ).values_list("pk", flat=True)

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
                    "profit": result.get("summa") / ad.budget,
                }
            )
        return render(request, "ads/ads-statistic.html", context={"ads": ads})
