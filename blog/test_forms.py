# Inside blog/test_forms.py
from django.test import TestCase
from django.contrib.auth.models import User
from blog.forms import PostForm, CommentForm, CustomPasswordResetForm, CustomSetPasswordForm  # Adjust import to match your app's structure
from blog.models import Post, Comment

class TestPostForm(TestCase):

    def test_form_is_valid(self):
        form_data = {
            'title': 'Test Title',
            'slug': 'test-title',
            'featured_image': None,  # Assuming image upload is optional for the test
            'excerpt': 'This is a test excerpt',
            'content': 'This is the test content'
        }
        post_form = PostForm(data=form_data)
        self.assertTrue(post_form.is_valid())

    def test_form_is_invalid(self):
        form_data = {
            'title': '',  # Invalid because title is required
            'slug': 'test-title',
            'featured_image': None,  # Assuming image upload is optional for the test
            'excerpt': 'This is a test excerpt',
            'content': 'This is the test content'
        }
        post_form = PostForm(data=form_data)
        self.assertFalse(post_form.is_valid(), msg="Form should be invalid because title is empty")


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        form_data = {'content': 'This is a great post', 'parent': None}
        comment_form = CommentForm(data=form_data)
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        form_data = {'content': '', 'parent': None}
        comment_form = CommentForm(data=form_data)
        self.assertFalse(comment_form.is_valid(), msg="Form should be invalid because content is empty")


class TestCustomPasswordResetForm(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_form_is_valid(self):
        form_data = {'username': 'testuser'}
        form = CustomPasswordResetForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form_data = {'username': 'nonexistentuser'}
        form = CustomPasswordResetForm(data=form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid because username does not exist")


class TestCustomSetPasswordForm(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_form_is_valid(self):
        form_data = {
            'new_password1': 'new_secure_password',
            'new_password2': 'new_secure_password'
        }
        form = CustomSetPasswordForm(user=self.user, data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        form_data = {
            'new_password1': 'new_secure_password',
            'new_password2': 'different_password'
        }
        form = CustomSetPasswordForm(user=self.user, data=form_data)
        self.assertFalse(form.is_valid(), msg="Form should be invalid because passwords do not match")



