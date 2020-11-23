from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views


app_name = "user"
urlpatterns = [
    path('create-user/', user_views.createUser, name='create-user'),
    path('login-user/', user_views.loginUser, name='login-user'),
    path('logout-user/', user_views.logoutUser, name='logout-user'),
    path('edit-user/', user_views.editUser, name='edit-user'),
    path('subscribe/', user_views.email_list_signup, name='subscribe'),
    
    path('account/', user_views.account, name='account'),
    path('remove-address/<id>/', user_views.removeAddress, name='remove-address'),
    path('edit-address/<id>/', user_views.editAddress, name='edit-address'),

    path('add-coupon/', user_views.addCoupon, name='add-coupon'),
    path('update-delivery/', user_views.updateDelivery, name='update-delivery'),
    path('process-order/', user_views.processOrder, name='process-order'),
]
