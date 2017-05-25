# -*- coding: utf-8 -*-
from django.apps import AppConfig


class LeaguesConfig(AppConfig):
    """
    League app configuration
    """
    name = 'leagues'

    def ready(self):
        """
        App will be ready afterward
        """
        from . import signals

