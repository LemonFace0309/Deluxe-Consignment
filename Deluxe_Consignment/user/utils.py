from .models import *
from store.utils import cookieCartData
from store.models import Product


def guestOrder(request, data):
    customer, created = Customer.objects.get_or_create(email=data['form']['email'])
    customer.name = data['form']['name']
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

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
