import json
from .models import *
from user.models import (
    Customer, Order, OrderItem, ShippingAddress, Coupon
)
from user.forms import (
    CreateUserForm
)


def cartData(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cart_quantity = order.get_cart_quantity
    cart_total = order.get_cart_total
    return {'order': order, 'items': items, 'cart_quantity': cart_quantity, 'cart_total': cart_total}


def cookieCartData(request, code=None):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        # For first load when cookies are not loaded yet
        cart = {}
    # creating order
    order = {'get_cart_total': 0, 'get_cart_quantity': 0, 'get_discount_total': 0, 'shipping': False}
    items = []

    for i in cart:
        # getting product
        product = Product.objects.get(id=i)
        # getting item total
        total = (product.discount_price * cart[i]['quantity'])

        # incrementing totals in order
        order['get_cart_quantity'] += cart[i]['quantity']
        order['get_cart_total'] += total

        # creating item
        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'brand': product.brand,
                'discount_price': product.discount_price,
                'featured': product.featured,
                'quantity': product.quantity,
                'date_created': product.date_created,
                'description': product.description,
                'slug': product.slug,
                'imageURL': product.imageURL,
                'get_brand': product.get_brand,
            },
            'quantity': cart[i]['quantity'],
            'get_total': total,
        }
        items.append(item)

    cart_quantity = order['get_cart_quantity']
    order['get_cart_total'] = float(order['get_cart_total'])
    cart_total = order['get_cart_total']
    if code is not None:
        coupon = Coupon.objects.get(code=code)
        order['coupon'] = coupon
        order['get_cart_total'] *= (1 - (order['coupon'].discount_percentage / 100))
        cart_total *= order['get_cart_total']
        order['get_discount_total'] = (cart_total / (1 - (coupon.discount_percentage/100))) - cart_total

    return {'order': order, 'items': items, 'cart_quantity': cart_quantity, 'cart_total': cart_total}
