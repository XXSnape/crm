from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .models import Product


class ProductsListView(PermissionRequiredMixin, ListView):
    permission_required = "products.view_product"
    queryset = Product.objects.only("name").all()
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "products.add_product"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products:products_list")
    template_name = "products/products-create.html"


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "products.delete_product"
    model = Product
    success_url = reverse_lazy("products:products_list")
    template_name = "products/products-delete.html"


class ProductDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "products.view_product"
    model = Product
    template_name = "products/products-detail.html"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "products.change_product"
    model = Product
    fields = "__all__"
    template_name = "products/products-edit.html"
