# Inside blog/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', slug='test-post', content='Test content', author=self.user)
        self.comment = Comment.objects.create(content='Test comment', post=self.post, author=self.user)
    
    def test_home_page(self):
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_blog_detail(self):
        response = self.client.get(reverse('blog_detail', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
        self.assertContains(response, self.post.title)

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123'
        })
        print(response.context['form'].errors)  # Debugging: Print form errors within method scope
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_upvote_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('upvote_post', kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, self.post.upvotes.all())

    def test_downvote_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('downvote_post', kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, self.post.downvotes.all())

    def test_upvote_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('upvote_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, self.comment.upvotes.all())

    def test_downvote_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('downvote_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, self.comment.downvotes.all())

    def test_edit_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edit_post', kwargs={'post_id': self.post.id}), {
            'title': 'Updated Title',
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')

    def test_delete_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_post', kwargs={'post_id': self.post.id}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_edit_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('edit_comment', kwargs={'comment_id': self.comment.id}), {
            'content': 'Updated comment'
        })
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment')

    def test_delete_comment(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('delete_comment', kwargs={'comment_id': self.comment.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

    def test_create_post(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'slug': 'new-post',
            'content': 'Content of the new post'
        })
        print(response.context['form'].errors)  # Debugging: Print form errors within method scope
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_custom_password_reset(self):
        response = self.client.post(reverse('custom_password_reset'), {'username': 'testuser'})
        print(response.context['form'].errors)  # Debugging: Print form errors within method scope
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['username'], 'testuser')

    def test_custom_password_reset_confirm(self):
        self.client.session['username'] = 'testuser'
        self.client.session.save()
        response = self.client.post(reverse('custom_password_reset_confirm'), {
            'new_password1': 'new_password123',
            'new_password2': 'new_password123'
        })
        print(response.context['form'].errors)  # Debugging: Print form errors within method scope
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='testuser')
        self.assertTrue(user.check_password('new_password123'))


