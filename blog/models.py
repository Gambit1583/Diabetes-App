from django.db import models
from django.contrib.auth.models import User

# Models

# # Allows for author dropdown when creating/editing post in the admin panel.
# class Author(models.Model):
#     name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='images/', default='images/default.jpg', null=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField()

# Orders posts from newest to oldest.
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of this post is {self.title}"