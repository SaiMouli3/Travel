from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html',redirect_authenticated_user=False), name='login'),
]
