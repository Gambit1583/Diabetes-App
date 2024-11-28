from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Comment

# Create your views here.
def home_page(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)   
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    post.upvotes.add(request.user)
    return JsonResponse({'upvotes': post.upvotes_count(), 'downvotes': post.downvotes_count()})

def downvote_post(request, post_id): 
    post = get_object_or_404(Post, id=post_id) 
    if request.user in post.upvotes.all(): 
        post.upvotes.remove(request.user) 
    post.downvotes.add(request.user) 
    return JsonResponse({'upvotes': post.upvotes_count(), 'downvotes': post.downvotes_count()})

def upvote_comment(request, comment_id): 
    comment = get_object_or_404(Comment, id=comment_id) 
    if request.user in comment.downvotes.all(): 
        comment.downvotes.remove(request.user) 
    comment.upvotes.add(request.user) 
    return JsonResponse({'upvotes': comment.upvotes_count(), 'downvotes': comment.downvotes_count()})

def downvote_comment(request, comment_id): 
    comment = get_object_or_404(Comment, id=comment_id) 
    if request.user in comment.upvotes.all(): 
        comment.upvotes.remove(request.user) 
    comment.downvotes.add(request.user) 
    return JsonResponse({'upvotes': comment.upvotes_count(), 'downvotes': comment.downvotes_count()})  