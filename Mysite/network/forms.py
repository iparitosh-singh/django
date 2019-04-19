from django import forms
from django.contrib.auth import(
     authenticate,
     get_user_model,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post


class UserRegisterrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            }
            #I added the placeholders for password in the django documentation - Paritosh


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="Password")

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('User is Not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


# class UserRegistrationForm(forms.Form):
#     error_messages = {
#         'password_mismatch': _("The two password fields didn't match."),
#     }
#
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}), label='Username')
#     email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label="Password")
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Conformation'}), label="Password Conformation")
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password1',
#             'password2',
#         ]
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         username_qs = User.objects.filter(username=username)
#         if username_qs.exists():
#             raise forms.ValidationError(
#                 "This Username already exists"
#             )
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class Post_Create_Form(forms.Form):
    class Meta:
        model = Post
        fields = ['title','content', 'author', 'image']
