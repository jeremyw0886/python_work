from django import forms
from .models import Blog, Post


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
