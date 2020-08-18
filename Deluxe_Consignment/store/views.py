from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from user.models import (
    Customer, Order, OrderItem, ShippingAddress
)
from django.views.generic import (
    DetailView,
)


# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'store/home.html', context)


def store(request):
    products = Product.objects.all()
    context = {
        'products': products,
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

    try:
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
    except:
        messages.error(request, f'Please create an account first')
    return redirect("product-detail", slug=slug)


def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    try:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if order.orderitem_set.filter(product=product).exists():
            order.orderitem_set.filter(product=product).delete()
            print('4')
            messages.success(request, f'"{product}" has been successfully removed from your shopping bag')
        else:
            messages.error(request, f'Your bag does not contain a {product} item to be removed')
    except:
        messages.error(request, f'Please create an account first')
    return redirect("product-detail", slug=slug)


def checkout(request):
    context = {

    }
    return render(request, 'store/cart.html', context)


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

