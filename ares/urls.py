# -*- coding: utf-8 -*-
"""
    Ares URL Configuration
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',
         include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('robots/', include(('robots.urls', 'robots'), namespace='robots')),
    path('games/', include(('games.urls', 'games'), namespace='games')),
    path('leagues/', include(('leagues.urls','leagues'), namespace='leagues')),
    path('', include(('home.urls', 'home'), namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
