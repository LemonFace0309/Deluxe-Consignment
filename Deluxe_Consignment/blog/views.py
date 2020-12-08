from django.shortcuts import render
from .models import Blog
from store.utils import *


def blog(request):
    blogs = Blog.objects.all().order_by('-date_created')

    if request.user.is_authenticated:
        data = cartData(request)
    else:
        data = cookieCartData(request)

    items = data['items']
    cart_quantity = data['cart_quantity']


    context = {
        'blogs': blogs,
        'items': items,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'store/blog.html', context)
