# from django.core.management.base import BaseCommand
# from blog.models import Post

# class Command(BaseCommand):
#     help = 'Set default image for posts without a featured image'

#     def handle(self, *args, **kwargs):
#         posts = Post.objects.all()
#         for post in posts:
#             if not post.featured_image:
#                 post.featured_image = 'images/default.jpg'
#                 post.save()
#         self.stdout.write(self.style.SUCCESS('Successfully updated posts with default images'))
