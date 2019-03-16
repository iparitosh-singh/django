from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView
)

posts = [
    {
        'author': 'Paritosh',
        'content': 'Hello World',
        'created_on': 'September 15, 2018',
    }
    {
        'author': 'Pratyush',
        'content': 'Hello NIBBAS',
        'created_on': 'February 7 , 2018',
    }
]
]

class PostList(ListView):
    model = Post
    context_object_name ='posts'
    ordering = ['title']
    paginated_by = 10

    #template address is already passed in this
    # <app>/<model>_<viewtype>
    #here it will be templates/network/Post_List.html

