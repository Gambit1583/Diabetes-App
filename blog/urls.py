from django.urls import path
from . views import home_page, blog_detail

urlpatterns = [
    path('', home_page, name='home_page'),
    path('post/<slug:slug>/', blog_detail, name='blog_detail'),
]