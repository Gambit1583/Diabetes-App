from django.urls import path
from .views import home_page, blog_detail, upvote_post, downvote_post, upvote_comment, downvote_comment
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),
    path('comment/<int:comment_id>/downvote/', views.downvote_comment, name='downvote_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]





