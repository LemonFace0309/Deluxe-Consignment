from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.views.generic import (
    DetailView,
)


# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'store/home.html', context)


def store(request):
    context = {

    }
    return render(request, 'store/store.html', context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product.html'

    # Getting Product
    def get_object(self):
        return get_object_or_404(Product, name=''.join(self.kwargs.get('product_name').split('-')))


def checkout(request):
    context = {

    }
    return render(request, 'store/cart.html', context)


def consign(request):
    context ={

    }
    return render(request, 'store/consign.html', context)


def about(request):
    context ={

    }
    return render(request, 'store/about.html', context)