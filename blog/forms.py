from django import forms
from django.forms import ModelForm
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'text_min', 'text', 'tags', 'description', 'keywords', 'image',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('text',)

