from django.http import HttpRequest, JsonResponse
from product_module.models import Product
from .models import Order, OrderDetail
from utils.validation import validate_count


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))

    count = request.GET.get('count')
    if not validate_count(count):
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی‌باشد',
            'confirm_button_text': 'مرسی از شما',
            'icon': 'warning'
        })
    count = int(count)
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'confirm_button_text': 'باشه ممنونم',
                'icon': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد',
                'confirm_button_text': 'مرسییییی',
                'icon': 'error'
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'confirm_button_text': 'ورود به سایت',
            'icon': 'error'
        })
