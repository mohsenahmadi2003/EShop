from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from product_module.models import Product


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            # get current user open order
            # add product to order
            pass
    else:
        return JsonResponse({
            'status': 'not_auth'
        })
