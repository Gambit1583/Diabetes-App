from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm, CustomPasswordResetForm, CustomSetPasswordForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

# Blog home page view
def home_page(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})

# Blog detail view with comment functionality
def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(parent__isnull=True)

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

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home_page')
        else:
            messages.error(request, form.errors.as_text())  # Display form errors
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

    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You are unable to edit this post!")

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('blog_detail', slug=post.slug)

    return render(request, 'blog/edit_post.html', {'post': post})

# Delete post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author and not request.user.is_staff:
        return HttpResponseForbidden("You are unable to delete this post!")

    post.delete()
    return render(request, 'blog/post_deleted.html')

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

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

    if request.user != comment.author and not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to delete this comment.")

    post_slug = comment.post.slug
    comment.delete()
    return redirect('blog_detail', slug=post_slug)

# Create post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home_page')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Custom Password Reset Views
def custom_password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            request.session['username'] = username
            return redirect('custom_password_reset_confirm')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'registration/custom_password_reset_form.html', {'form': form})

def custom_password_reset_confirm(request):
    username = request.session.get('username')
    if not username:
        return redirect('custom_password_reset')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('custom_password_reset')

    if request.method == 'POST':
        form = CustomSetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password has been reset successfully.")
            return redirect('login')
    else:
        form = CustomSetPasswordForm(user=user)
    return render(request, 'registration/custom_password_reset_confirm.html', {'form': form})

# About page view
def about(request):
    return render(request, 'about.html')
