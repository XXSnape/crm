from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
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
