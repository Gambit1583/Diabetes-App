from django.urls import path
from . views import home_page, blog_detail, upvote_post, downvote_post, upvote_comment, downvote_comment

urlpatterns = [
    path('', home_page, name='home_page'),
    path('post/<slug:slug>/', blog_detail, name='blog_detail'),
    path('post/<int:post_id>/upvote/', upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', downvote_post, name='downvote_post'),
    path('comment/int:comment_id>/upvote/', upvote_comment, name='upvote_comment'),
    path('comment/int:comment_id>/downvote/', downvote_comment, name='downvote_comment'),
]

