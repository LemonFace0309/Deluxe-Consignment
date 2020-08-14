from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'store/home.html', context)


def store(request):
    context = {

    }
    return render(request, 'store/store.html', context)


def products(request):
    shoeProducts = Shoe.objects.all()
    bagProducts = Bag.objects.all()
    accessoryProducts = Accessory.objects.all()
    slgProducts = SLGS.objects.all()

    context = {
        'shoeProducts':shoeProducts,
        'bagProducts':bagProducts,
        'jewelryProducts':accessoryProducts,
        'slgProducts':slgProducts,
    }
    return render(request, 'store/products.html', context)


def consign(request):
    context ={

    }
    return render(request, 'store/consign.html', context)


def about(request):
    context ={

    }
    return render(request, 'store/about.html', context)