from django.shortcuts import render, redirect
from .models import Post, Profile
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, forms
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .forms import( 
    #UserRegistrationForm,
    Post_Create_Form, 
    UserLoginForm,
    UserRegisterrationForm,
    Post_Form,
)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginated_by = 10

    #template address is already passed in this
    # <app>/<model>_<viewtype>
#here it will be templates/network/Post_List.html


class PostDetail(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post    
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

        
def register(request):
    if request.method == 'POST':
        form = UserRegisterrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account have been registered!,{username}')
            return redirect('network:login')
    else:
        form = UserRegisterrationForm()
    return render(request=request,
                  template_name="network/registration_view.html",
                  context={'form': form})


class ProfileDetail(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['image', 'profile_cover', 'bio']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


def login_register(request):
    if request.method == "POST":
        form_log = UserLoginForm(data=request.POST or None)
        # form_reg = UserRegistrationForm(data=request.POST or None)
        form_reg = UserRegisterrationForm(request.POST)
        if 'sign_up' in request.POST:
            # if form_reg.is_valid():
            #     user = form_reg.save(commit=False)
            #     password = form_reg.cleaned_data.get('password1')
            #     user.set_password(password)
            #     user.save()
            #     login(request, user)
            #     username = form_reg.cleaned_data.get('username')
            #     messages.success(request, f'Your account have been registered!,{username}')
            #     return redirect('network:homepage')
            if form_reg.is_valid():
                user = form_reg.save()
                username = form_reg.cleaned_data.get('username')
                login(request, user)
                messages.success(request, f'Your account was created, with username: {username}')
                return redirect('network:homepage')
        elif 'sign_in' in request.POST:
            if form_log.is_valid():
                username = form_log.cleaned_data.get('username')
                password = form_log.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('network:homepage'))

    else:
        form_reg = UserRegisterrationForm()
        form_log = UserLoginForm()
    return render(request,"network/bothpage.html", {'form_reg': form_reg, 'form_log': form_log})

class TestViewPost(LoginRequiredMixin, CreateView):
     
    if request.POST:
        form_post = Post_Form(data = request.POST) 
        if form_post.is_valid():
            form_post.save()
    else
        form_post = Post_Form()
    
    return  render(request, "network/postcreate.html", context = 'form_post': form_post) 