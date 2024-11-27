from django.shortcuts import render
from .models import Post

# Create your views here.
def home_page(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list})