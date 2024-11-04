from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="products_list"),
    path("new/", views.ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_details"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("<int:pk>/edit/", views.ProductUpdateView.as_view(), name="product_update"),
]
