from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'featured_image')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_on']

    class Media:
        css = {
            'all': ('custom_admin.css',)
        }

# Register your models here.
admin.site.register(Post, PostAdmin)

