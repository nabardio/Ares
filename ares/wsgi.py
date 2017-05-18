# -*- coding: utf-8 -*-
"""
    WSGI config for Ares project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ares.settings")

application = get_wsgi_application()
