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
    featured_image = models.ImageField(upload_to='images/', default='images/default.jpg.webp', null=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='post_upvotes', blank=True) 
    downvotes = models.ManyToManyField(User, related_name='post_downvotes', blank=True) 
    
    def upvotes_count(self): 
        return self.upvotes.count() 
        
    def downvotes_count(self): 
        return self.downvotes.count()

class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments') 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField() # Assuming 'content' instead of 'body' to match usage 
    created_on = models.DateTimeField(auto_now_add=True) 
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True) 
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True) 
    
    def upvotes_count(self): 
        return self.upvotes.count() 
            
        def downvotes_count(self): 
            return self.downvotes.count()
            
# Orders posts from newest to oldest.
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment by {self.post}"