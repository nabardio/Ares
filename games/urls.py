# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.GameList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.GameDetail.as_view(), name='detail'),
]
