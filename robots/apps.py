# -*- coding: utf-8 -*-
from django.apps import AppConfig


class RobotsConfig(AppConfig):
    """
    Robot app configuration
    """
    name = 'robots'

    def ready(self):
        """
        App will be ready afterward
        """
        from . import signals
