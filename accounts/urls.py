from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic import CreateView
from . import forms
from . import views

urlpatterns = [
    url('^register/$',
        CreateView.as_view(
            template_name='registration/register.html',
            form_class=forms.UserRegistrationForm,
            success_url='/accounts/profile'),
        name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(
        redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
]
