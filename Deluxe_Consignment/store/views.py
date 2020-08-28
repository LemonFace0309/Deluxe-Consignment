from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .utils import *
from user.models import (
    Customer, Order, OrderItem, ShippingAddress
)
from user.forms import (
    CreateUserForm
)
from django.views.generic import (
    DetailView,
    ListView,

)


# Create your views here.
def home(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        data = cartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
    else:
        data = cookieCartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
    context = {
        'products': products,
        'items': items,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'store/home.html', context)


class StoreListView(ListView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        search = request.GET.get('searchBar')
        s = request.GET.get('s')
        category = request.GET.get('category')
        sort = request.GET.get('sort')

        productlist = list(Product.objects.all())
        for product in productlist:
            print(product)
        # print(productlist)

        if search != '' and search is not None:
            products = products.filter(name__icontains=search)

        if sort == 'pricelow':
            for product in products:
                print(f'{product.name} cost {product.price} disc {product.discount_price}')
                if product.discount_price:
                    product.price = product.discount_price
                    products = products.order_by('price')

            # for product in products:
            #     if product.discount_price:
            #         products = products.order_by('price')
            #         product.price = product.discount_price

        if category is None:
            print('cat is none')

        print(category)
        # print(sortOption)
        print("sort!")
        print(products)

        # from django.db.models.utils import list_to_queryset
        # productlist = list_to_queryset(productlist)

        if request.user.is_authenticated:
            data = cartData(request)
            items = data['items']
            cart_quantity = data['cart_quantity']
        else:
            data = cookieCartData(request)
            items = data['items']
            cart_quantity = data['cart_quantity']

        context = {
            'products': products,
            'items': items,
            'cart_quantity': cart_quantity,
        }
        return render(request, 'store/store.html', context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product.html'

    # # Getting Product
    # def get_object(self):
    #     return get_object_or_404(Product, name=''.join(self.kwargs.get('product_name').split('-')))


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # Updating order item quantity
        if orderItem.quantity < product.quantity:
            orderItem.quantity += 1
            orderItem.save()
            messages.success(request, f'{product} has been successfully added to your shopping bag')
        else:
            messages.error(request, f'You\'ve reached the maximum number of {product}s available for purchase')
    # return redirect("product-detail", slug=slug)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if order.orderitem_set.filter(product=product).exists():
            order.orderitem_set.filter(product=product).delete()
            messages.success(request, f'"{product}" has been successfully removed from your shopping bag')
        else:
            messages.error(request, f'Your bag does not contain a {product} item to be removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update_cookie_cart_quantity(request):
    data = json.loads(request.body)
    # getting product
    product = Product.objects.get(id=data['productId'])
    # getting order item quantity
    itemQuantity = data['itemQuantity']
    print(itemQuantity)
    # getting action
    action = data['action']

    if action == 'add':
        if int(itemQuantity) < product.quantity:
            messages.success(request, f'{product} has been successfully added to your shopping bag')
            return JsonResponse('add', safe=False)
        else:
            messages.error(request, f'You\'ve reached the maximum number of {product}s available for purchase')
            return JsonResponse('', safe=False)
    elif action == 'remove':
        if int(itemQuantity) != 0:
            messages.success(request, f'"{product}" has been successfully removed from your shopping bag')
            return JsonResponse('remove', safe=False)
        else:
            messages.error(request, f'Your bag does not contain a {product} item to be removed')
            return JsonResponse('remove', safe=False)

def checkout(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        data = cartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
    else:
        data = cookieCartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
    context = {
        'products': products,
        'items': items,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'store/checkout.html', context)


def consign(request):
    context = {

    }
    return render(request, 'store/consign.html', context)


def about(request):
    context = {

    }
    return render(request, 'store/about.html', context)


def paymentPolicy(request):
    context = {

    }
    return render(request, 'store/paymentPolicy.html', context)


def test(request):
    return render(request, 'store/test.html')
