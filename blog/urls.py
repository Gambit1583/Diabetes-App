from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import the views module from the current directory

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('post/<int:post_id>/upvote/', views.upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', views.downvote_post, name='downvote_post'),
    path('comment/<int:comment_id>/upvote/', views.upvote_comment, name='upvote_comment'),  # Corrected URL
    path('comment/<int:comment_id>/downvote/', views.downvote_comment, name='downvote_comment'),  # Corrected URL
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]




