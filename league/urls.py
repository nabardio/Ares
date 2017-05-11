from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.LeagueList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.LeagueDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/register/$', views.LeagueRegister.as_view(),
        name='register')
]
