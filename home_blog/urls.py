"""
URL configuration for home_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import (
    text_response,
    template,
    post_list_view,
    post_detail_view,
    post_create_view,
    post_update_view,
    TestView,
    PostListView,
    PostDetailView,
    PostCreateView,
)
from user.views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('text_response/', text_response),
    path('', template, name='template'),
    path('posts/', post_list_view, name='post_list'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view, name='post_create'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('post/<int:post_id>/update', post_update_view, name='post_update'),
    path('test/', TestView.as_view(), name='test'),
    path('posts2/', PostListView.as_view(), name='post_list2'),
    path('post/<int:pk>/class/', PostDetailView.as_view(), name='post_detail2'),
    path('posts2/create/', PostCreateView.as_view(), name='post_create2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


