from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib import messages
from django.views.generic import (
    ListView,DetailView
)
from .forms import UserRegisterrationForm

class PostList(ListView):
    model = Post
    context_object_name ='posts'
    ordering = ['title']
    paginated_by = 10

    #template address is already passed in this
    # <app>/<model>_<viewtype>
#here it will be templates/network/Post_List.html

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
