from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm

# Home view
def home(request):
    return render(request, 'home.html')

# Blog home page view
def home_page(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

# Blog detail view with comment functionality
def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments, 'form': form})

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Voting functionalities for posts and comments
@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    post.upvotes.add(request.user)
    return JsonResponse({'upvotes': post.upvotes_count(), 'downvotes': post.downvotes_count()})

@login_required
def downvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
    post.downvotes.add(request.user)
    return JsonResponse({'upvotes': post.upvotes_count(), 'downvotes': post.downvotes_count()})

@login_required
def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.downvotes.all():
        comment.downvotes.remove(request.user)
    comment.upvotes.add(request.user)
    return JsonResponse({'upvotes': comment.upvotes_count(), 'downvotes': comment.downvotes_count()})

@login_required
def downvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.upvotes.all():
        comment.upvotes.remove(request.user)
    comment.downvotes.add(request.user)
    return JsonResponse({'upvotes': comment.upvotes_count(), 'downvotes': comment.downvotes_count()})
