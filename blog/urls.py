from django.urls import path
from .views import home_page, blog_detail, register, upvote_post, downvote_post, upvote_comment, downvote_comment, edit_post, delete_post, edit_comment, delete_comment
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page view
    path('', home_page, name='home_page'),

    # User authentication views
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Blog post detail view
    path('post/<slug:slug>/', blog_detail, name='blog_detail'),

    # Voting functionalities for posts and comments
    path('post/<int:post_id>/upvote/', upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', downvote_post, name='downvote_post'),
    path('comment/<int:comment_id>/upvote/', upvote_comment, name='upvote_comment'),
    path('comment/<int:comment_id>/downvote/', downvote_comment, name='downvote_comment'),

    # Edit and delete post views
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),

    # Edit and delete comment views
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
