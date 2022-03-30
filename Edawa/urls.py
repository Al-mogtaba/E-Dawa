"""Edawa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from User import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.RegisterView.as_view() , name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html') , name='logout'),
    path('', include('main.urls')),
    path('dashboard/', include('dashboard.urls')),
]
