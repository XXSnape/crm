from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products:products_list")
    template_name = "products/products-create.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("products:products_list")
    template_name = "products/products-delete.html"


class ProductsListView(ListView):
    queryset = Product.objects.only("name").all()
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/products-detail.html"


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = "products/products-edit.html"
