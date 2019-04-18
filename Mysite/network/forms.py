from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class UserRegisterrationForm(UserCreationForm):
    email = forms.EmailField(widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password Conformation'}),
            }

class UserLoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Username'}), label = 'Username')
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : 'Password'}), label = "Password")
    class Meta:
        model = User
        fields = ['username', 'password']


class Post_Create_Form(forms.Form):
    class Meta:
        model = Post
        fields = ['title','content', 'author', 'image']
        