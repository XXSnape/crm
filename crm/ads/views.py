from decimal import Decimal

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
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


class AdsListView(PermissionRequiredMixin, ListView):
    permission_required = "ads.view_ads"
    queryset = Ads.objects.only("name").all()
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "ads.add_ads"
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-create.html"


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "ads.delete_ads"
    model = Ads
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-delete.html"


class AdsDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "ads.view_ads"
    queryset = Ads.objects.select_related("product")
    template_name = "ads/ads-detail.html"


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "ads.change_ads"
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    template_name = "ads/ads-edit.html"


class StatisticsView(LoginRequiredMixin, View):
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

            print("c_pk", contracts_pk)
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
        return render(request, "ads/ads-statistic.html", context={"ads": ads})
