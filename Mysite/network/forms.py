from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UserRegisterrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class Post_Create_Form(forms.Form):
    class Meta:
        model = Post
        fields = ['title','content', 'author', 'image']
        