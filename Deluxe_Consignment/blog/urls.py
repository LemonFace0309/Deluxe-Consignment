from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('blog/', blog_views.blog, name='blog')
]