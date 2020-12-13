from django.urls import path
from . import views as blog_views


app_name = "blog"
urlpatterns = [
    path('home/', blog_views.home, name='home'),
    path('post/<slug:slug>/', blog_views.post, name="post"),
]