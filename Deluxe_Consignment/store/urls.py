from django.urls import path
from . import views as store_views
from .views import (
    ProductDetailView
)

urlpatterns = [
    path('', store_views.home, name='home'),
    path('store/', store_views.store, name='store'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('checkout/', store_views.checkout, name="checkout"),
    path('consign/', store_views.consign, name='consign'),
    path('about/', store_views.about, name='about'),
    path('paymentPolicy/', store_views.paymentPolicy, name='paymentPolicy'),
    path('test/', store_views.test, name="test")
]