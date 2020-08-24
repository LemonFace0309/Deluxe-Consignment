from django.urls import path
from django.views.decorators.cache import never_cache
from . import views as store_views
from .views import (
    ProductDetailView
)

urlpatterns = [
    path('', store_views.home, name='home'),
    path('store/', store_views.store, name='store'),
    path('product/<slug>/', never_cache(ProductDetailView.as_view()), name='product-detail'),  # never_cache prevents
    # web_browser from caching the page and re-triggering an add/remove item model if clicked on previously
    path('checkout/', store_views.checkout, name="checkout"),
    path('consign/', store_views.consign, name='consign'),
    path('about/', store_views.about, name='about'),
    path('payment-policy/', store_views.paymentPolicy, name='payment-policy'),
    path('test-test-test/', store_views.test, name="test"),

    path('add-to-cart/<slug>/', store_views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', store_views.remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity/<slug>/', store_views.reduce_quantity, name='reduce-quantity'),
]

# Figure out why order manipulation (add/remove from cart) is being undone after going back in the browser in JUST
# the product detail view
