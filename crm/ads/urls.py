from django.urls import path

from . import views

app_name = "ads"

urlpatterns = [
    path("", views.AdsListView.as_view(), name="ads_list"),
    path("new/", views.AdsCreateView.as_view(), name="ads_create"),
    path("<int:pk>/", views.AdsDetailView.as_view(), name="ads_details"),
    path("<int:pk>/delete/", views.AdsDeleteView.as_view(), name="ads_delete"),
    path("<int:pk>/edit/", views.AdsUpdateView.as_view(), name="ads_update"),
    path("statistic/", views.StatisticsView.as_view(), name="statistics"),
]
