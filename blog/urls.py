from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
]