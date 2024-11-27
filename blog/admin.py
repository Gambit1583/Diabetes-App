from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin): 
    ordering = ['-created_on']


# Register your models here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Author)