from django import forms 
from .models import Post, Comment 
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'featured_image', 'excerpt', 'content',]

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