from django.urls import path
from . import views as store_views
from django.views.decorators.cache import never_cache
from .views import (
    ProductDetailView,
    StoreListView,
)

app_name = "shop"
urlpatterns = [
    path('', store_views.home, name='home'),
    path('store/', store_views.StoreListView.as_view(), name='store'), #idk what nevercahe is, might need to add it -jim
    path('product/<slug>/', never_cache(ProductDetailView.as_view()), name='product-detail'),  # never_cache prevents
    # web_browser from caching the page and re-triggering an add/remove item model if clicked on previously
    path('cart/', store_views.cart, name="cart"),
    path('checkout/', store_views.checkout, name="checkout"),
    path('consign/', store_views.consign, name='consign'),
    path('about/', store_views.about, name='about'),
    path('payment-policy/', store_views.paymentPolicy, name='payment-policy'),
    path('test-test-test/', store_views.test, name="test"),
    path('order-summary/<str:transaction_id>/', store_views.orderSummary, name='order-summary'),

    path('add-to-cart/<slug>/', store_views.add_to_cart, name='add-to-cart'),
    path('subtract-from-cart/<slug>/', store_views.subtract_from_cart, name='subtract-from-cart'),
    path('remove-from-cart/<slug>/', store_views.remove_from_cart, name='remove-from-cart'),
    path('update-cookie-cart-quantity/', store_views.update_cookie_cart_quantity, name="update-cookie-cart-quantity")
]

# Figure out why order manipulation (add/remove from cart) is being undone after going back in the browser in JUST
# the product detail view
