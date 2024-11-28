from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'featured_image')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']

    class Media:
        css = {
            'all': ('custom_admin.css',)
        }

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
