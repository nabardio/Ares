# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.Home.as_view(), name='home'),
    url('^about/', views.About.as_view(), name='about'),
    url('^contact/', views.Contact.as_view(), name='contact'),
]
