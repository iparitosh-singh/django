from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
)
from .forms import UserRegistrrationForm

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
        form = UserRegistrrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            message.success(request,f'Your account have been registered!,{username}')

    else:
        form = UserRegistrrationForm()
    return render(request=request,
                  template_name="network/registration_view.html",
                  context={'form': form})

