from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='home'),
    path('store', store_views.store, name='store'),
    path('products', store_views.products, name='products'),
]