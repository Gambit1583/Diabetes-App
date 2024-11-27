from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='images/', null=True, blank=True)
    excerpt = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title