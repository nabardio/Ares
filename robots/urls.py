# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UserRobotList.as_view(), name='user-list'),
    url(r'^(?P<pk>\d+)/$', views.RobotDetail.as_view(), name='detail'),
    url('^create/$', views.CreateRobot.as_view(), name='create'),
    url('^edit/(?P<pk>\d+)/$', views.EditRobot.as_view(), name='edit'),
    url('^delete/(?P<pk>\d+)/$', views.DeleteRobot.as_view(), name='delete'),
]
