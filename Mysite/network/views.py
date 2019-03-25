from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from .forms import UserRegisterrationForm

class PostList(ListView):
    model = Post
    context_object_name ='posts'
    ordering = ['-created_on']
    paginated_by = 10

    #template address is already passed in this
    # <app>/<model>_<viewtype>
#here it will be templates/network/Post_List.html

class PostDetail(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post    
    fields = ['title', 'content','image']


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
            return True


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user  == post.author:
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