from django.urls import path
from .views import home_page, blog_detail, register, login_view, upvote_post, downvote_post, upvote_comment, downvote_comment, edit_post, delete_post, edit_comment, delete_comment, create_post, custom_password_reset, custom_password_reset_confirm
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page view
    path('', home_page, name='home_page'),

    # User authentication views
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),  # Use custom login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Custom password reset views
    path('password_reset/', custom_password_reset, name='custom_password_reset'),
    path('password_reset/confirm/', custom_password_reset_confirm, name='custom_password_reset_confirm'),

    # Blog post detail view
    path('post/<slug:slug>/', blog_detail, name='blog_detail'),

    # Voting functionalities for posts and comments
    path('blog/post/<int:post_id>/upvote/', upvote_post, name='upvote_post'),
    path('blog/post/<int:post_id>/downvote/', downvote_post, name='downvote_post'),
    path('blog/comment/<int:comment_id>/upvote/', upvote_comment, name='upvote_comment'),
    path('blog/comment/<int:comment_id>/downvote/', downvote_comment, name='downvote_comment'),

    # Create Post
    path('create/', create_post, name='create_post'),

    # Edit and delete post views
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),

    # Edit and delete comment views
    path('comment/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]

