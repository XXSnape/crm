from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Ads
from .service import get_statistic


class AdsListView(PermissionRequiredMixin, ListView):
    """Отображает рекламные компании"""

    permission_required = "ads.view_ads"
    queryset = Ads.objects.only("name").all()
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsCreateView(PermissionRequiredMixin, CreateView):
    """Создает рекламную компанию"""

    permission_required = "ads.add_ads"
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-create.html"


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    """Удаляет рекламную компанию"""

    permission_required = "ads.delete_ads"
    model = Ads
    success_url = reverse_lazy("ads:ads_list")
    template_name = "ads/ads-delete.html"


class AdsDetailView(PermissionRequiredMixin, DetailView):
    """Отображает детали рекламной компании"""

    permission_required = "ads.view_ads"
    queryset = Ads.objects.select_related("product")
    template_name = "ads/ads-detail.html"


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    """Обновляет рекламную компанию"""

    permission_required = "ads.change_ads"
    queryset = Ads.objects.select_related("product")
    fields = "__all__"
    template_name = "ads/ads-edit.html"


class StatisticsView(LoginRequiredMixin, View):
    """Отображает статистику о рекламных компаниях"""

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Метод get для возврата статистики

        :param request: HttpRequest
        :return: HttpResponse
        """
        context = get_statistic()
        return render(request, "ads/ads-statistic.html", context=context)
