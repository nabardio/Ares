from django.conf.urls import include, url
from django.views.generic import CreateView
from . import forms

urlpatterns = [
    url('^register/',
        CreateView.as_view(
            template_name='registration/register.html',
            form_class=forms.UserRegistrationForm,
            success_url='/accounts/profile'),
        name='register'),
    url('^', include('django.contrib.auth.urls')),
]
