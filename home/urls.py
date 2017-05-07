from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='home'),
    url('^about/', views.about, name='about'),
    url('^contact/', views.contact, name='contact'),
]
