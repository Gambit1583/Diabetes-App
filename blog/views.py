from django.http import JsonResponse # HttpResponseForbidden 
from django.views.decorators.http import require_http_methods 
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Blog home page view
def home_page(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

# Blog detail view with comment functionality
def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent__isnull=True) # This will only get top-level functions

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'comments': comments, 'form': form})

# User registration view
# Register View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('home_page')  # Redirect to home or another page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Voting functionalities for posts and comments


@require_http_methods(["POST"])
@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count()})

@require_http_methods(["POST"])
@login_required
def downvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    else:
        post.downvotes.add(request.user)
    return JsonResponse({'upvotes': post.upvotes.count(), 'downvotes': post.downvotes.count()})



@require_http_methods(["POST"])
@login_required
def upvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.downvotes.all():
        comment.downvotes.remove(request.user)
    if request.user in comment.upvotes.all():
        comment.upvotes.remove(request.user)
    else:
        comment.upvotes.add(request.user)
    return JsonResponse({'upvotes': comment.upvotes.count(), 'downvotes': comment.downvotes.count()})

@require_http_methods(["POST"])
@login_required
def downvote_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.upvotes.all():
        comment.upvotes.remove(request.user)
    if request.user in comment.downvotes.all():
        comment.downvotes.remove(request.user)
    else:
        comment.downvotes.add(request.user)
    return JsonResponse({'upvotes': comment.upvotes.count(), 'downvotes': comment.downvotes.count()})

# Edit post

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Confirm user is author or admin deny edit if other
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You are unable to edit this post!")

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blod_detail', slug=post.slug)

    return render(request, 'blog/edit_post.html', {'post': post})

# Delete Post if user

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the user is the author or an admin
    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You are unable to delete this post!")  # Properly indented

    post.delete()
    return render(request, 'blog/post_deleted.html')

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author or an admin
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to edit this comment.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author or an admin
    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    post_slug = comment.post.slug  # Save the post slug for redirecting
    comment.delete()
    return redirect('blog_detail', slug=post_slug)

# Create Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # This handles uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')

    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})