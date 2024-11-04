from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products:products_list")
    template_name = "products/products-create.html"


class ProductsListView(ListView):
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"
