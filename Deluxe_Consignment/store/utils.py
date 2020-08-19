import json
from user.models import (
    Customer, Order, OrderItem, ShippingAddress
)


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_quantity = order.get_cart_items
        return {'order': order, 'items': items, 'cart_quantity': cart_quantity}
    else:
        pass
    return
