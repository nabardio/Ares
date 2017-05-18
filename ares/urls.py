# -*- coding: utf-8 -*-
"""
    Ares URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^robots/', include('robots.urls', namespace='robots')),
    url(r'^games/', include('games.urls', namespace='games')),
    url(r'^leagues/', include('leagues.urls', namespace='leagues')),
    url(r'^', include('home.urls', namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
