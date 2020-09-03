from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .utils import *
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from user.models import (
    Customer, Order, OrderItem, ShippingAddress
)
from user.forms import (
    ShippingAddressForm
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
        products = Product.objects.all().order_by('id')
        search = request.GET.get('q')
        sort = request.GET.get('sort')
        brand = request.GET.get('brand')
        category = request.GET.get('category')
        pricemax = request.GET.get('pricemax')

        brands = []
        for choice in BRAND_CHOICES:
            if products.filter(brand__icontains=choice[1]).count() != 0:
                brands += [choice[1]]

        if search != '' and search is not None:
            products = products.filter(name__icontains=search)

        if sort == 'pricelow':
            products = products.order_by('discount_price', Lower('name'))
        elif sort == 'pricehigh':
            products = products.order_by('-discount_price', Lower('name'))
        elif sort == 'a-z':
            products = products.order_by(Lower('name'), 'discount_price')
        elif sort == 'z-a':
            products = products.order_by(Lower('-name'), 'discount_price')

        if brand != '' and brand is not None:
            products = products.filter(brand__icontains=brand)


        if category == 'shoes':
            products = products.filter(shoe__gt=0)
        elif category == 'bags':
            products = products.filter(bag__gt=0)
        elif category == 'accessories':
            products = products.filter(accessory__gt=0)
        elif category == 'slgs':
            products = products.filter(slg__gt=0)

        if pricemax != 0 and pricemax is not None:
            products = products.filter(discount_price__lte=pricemax)

        # Pagination
        paginator = Paginator(products, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

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
            'brands': brands,
            'page_obj': page_obj,
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


def subtract_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # Updating order item quantity
        if orderItem.quantity > 1:
            orderItem.quantity -= 1
            orderItem.save()
            messages.success(request, f'{product} quantity has successfully been updated')
        else:
            orderItem.delete()
            messages.success(request, f'{product} has been removed from cart')
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
            messages.success(request, f'"{product}" has been successfully added to your shopping bag')
            return JsonResponse('add', safe=False)
        else:
            messages.error(request, f'You\'ve reached the maximum number of {product}s available for purchase')
            return JsonResponse('', safe=False)
    elif action == 'subtract':
        if int(itemQuantity) != 0:
            messages.success(request, f'Order quantity of "{product}" has been successfully reduced')
            return JsonResponse('subtract', safe=False)
        else:
            messages.error(request, f'Your bag does not contain a {product} item to be reduced')
            return JsonResponse('subtract', safe=False)
    elif action == 'remove':
        if int(itemQuantity) != 0:
            messages.success(request, f'"{product}" has been successfully removed from your shopping bag')
            return JsonResponse('remove', safe=False)
        else:
            messages.error(request, f'Your bag does not contain a {product} item to be removed')
            return JsonResponse('remove', safe=False)

def cart(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        data = cartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
        cart_total = data['cart_total']
    else:
        data = cookieCartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
        cart_total = data['cart_total']
    context = {
        'products': products,
        'items': items,
        'cart_quantity': cart_quantity,
        'cart_total': cart_total
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        data = cartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
        cart_total = data['cart_total']
    else:
        data = cookieCartData(request)
        items = data['items']
        cart_quantity = data['cart_quantity']
        cart_total = data['cart_total']

    products = Product.objects.all()
    form = ShippingAddressForm()
    context = {
        'products': products,
        'items': items,
        'cart_quantity': cart_quantity,
        'cart_total': cart_total,
        'form': form,
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