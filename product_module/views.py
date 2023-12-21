from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST["product_id"]
        product = Product.objects.get(pk=product_id)
        request.session["product_favorite"] = product_id
        return redirect(product.get_absolute_url())
