from django.db import models
from django.contrib.auth.models import User

# Models

# Allows for author dropdown when creating/editing post in the admin panel.
# class Author(models.Model):
#     name = models.CharField(max_length=100)

from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=260)
    slug = models.SlugField(unique=True, blank=True, null=True)  # Make slug optional
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='images/default.jpg', null=True, blank=True)
    excerpt = models.TextField(blank=True, null=True)  # Make excerpt optional
    content = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='post_downvotes', blank=True)
    
    def upvotes_count(self):
        return self.upvotes.count()
        
    def downvotes_count(self):
        return self.downvotes.count()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField() # Assuming 'content' instead of 'body' to match usage 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True) 
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE) 
    
    def upvotes_count(self): 
        return self.upvotes.count() 
            
    def downvotes_count(self): 
        return self.downvotes.count()
            
# Orders posts from newest to oldest.
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"