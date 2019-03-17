from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name = 'homepage'),
    path('register/', views.register, name="register"),
]