# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.Logout.as_view(), name='logout'),
    url(r'^(?P<username>[\w.@+\-]+)/$', views.Profile.as_view(),
        name='profile'),
]
