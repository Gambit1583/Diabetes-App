from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'excerpt', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'parent': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class CustomPasswordResetForm(forms.Form): 
    username = forms.CharField(max_length=150) 
    
    def clean_username(self): 
        username = self.cleaned_data['username'] 
        try: 
            User.objects.get(username=username) 
        except User.DoesNotExist: 
            raise forms.ValidationError("User does not exist.") 
        return username 
        
class CustomSetPasswordForm(SetPasswordForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)

