from django.urls import path
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='home')
]