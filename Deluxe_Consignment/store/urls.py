from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='home'),
    path('store', store_views.store, name='store'),
    path('products', store_views.products, name='products'),
    path('consign', store_views.consign, name='consign'),
    path('about', store_views.about, name='about'),
    path('paymentPolicy', store_views.paymentPolicy, name='paymentPolicy')
]