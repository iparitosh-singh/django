from django.urls import path, include
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'network'
urlpatterns = [
    path('', user_views.PostList.as_view(), name = 'homepage'),
    path('register/', user_views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(), name="login"),    #we can add the template path manually in as_view()
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),  #default is registration/logout.html
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)