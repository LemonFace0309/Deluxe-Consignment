from django.shortcuts import render
from .models import Post
from store.utils import *


def home(request):
    posts = Post.objects.all().order_by('-date_created')

    if request.user.is_authenticated:
        data = cartData(request)
    else:
        data = cookieCartData(request)

    items = data['items']
    cart_quantity = data['cart_quantity']

    context = {
        'posts': posts,
        'items': items,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'blog/home.html', context)


def post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.user.is_authenticated:
        data = cartData(request)
    else:
        data = cookieCartData(request)

    items = data['items']
    cart_quantity = data['cart_quantity']

    context = {
        'post': post,
        'items': items,
        'cart_quantity': cart_quantity,
    }
    return render(request, 'blog/post.html', context)

