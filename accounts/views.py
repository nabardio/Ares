# -*- coding: utf-8 -*-
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView

from .forms import UserRegistrationForm
from .models import User


class Register(CreateView):
    """
    User registration view
    """
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = '/'


class Login(LoginView):
    """
    User login view
    """
    redirect_authenticated_user = True


class Logout(LogoutView):
    """
    User logout view
    """
    pass


class Profile(DetailView):
    """
    User profile view
    """
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'profile.html'
    context_object_name = 'profile'
