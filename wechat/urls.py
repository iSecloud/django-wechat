"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic.base import TemplateView
from moments.views import comment, delete_comment, friend, home, like, register_user, show_status, show_user, submit_post, update_user
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name="homepage.html")),
    path('user', show_user),
    path('status', show_status),
    path('post', submit_post),
    path('exit', LogoutView.as_view(next_page='/')),
    path('friends', friend),
    path('register', register_user),
    path('update', update_user),
    path('like', like),
    path('comment', comment),
    path('comment/delete', delete_comment),
]
