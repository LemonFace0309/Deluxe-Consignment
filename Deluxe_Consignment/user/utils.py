from .models import *
from store.utils import cookieCartData
from store.models import Product


def guestOrder(request, data):
    customer, created = Customer.objects.get_or_create(email=data['form']['email'])
    customer.name = data['form']['name']
    customer.save()

    order, created = Order.objects.get_or_create(
        customer=customer,
        complete=False,
    )
    if created:
        # adding coupon code
        if 'code' in request.session:
            coupon = Coupon.objects.get(code=request.session['code'])
            order.coupon = coupon

        # appending order items
        cookieData = cookieCartData(request)
        items = cookieData['items']

        for item in items:
            product = Product.objects.get(id=item['product']['id'])

            orderItem = OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )
    return customer, order
