from django import forms
from .models import Thread, Post

# Форма для создания Thread
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description']

# Форма для создания Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author']
