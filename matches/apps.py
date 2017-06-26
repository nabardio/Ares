# -*- coding: utf-8 -*-
from django.apps import AppConfig


class MatchesConfig(AppConfig):
    """
    Match app configuration
    """
    name = 'matches'

    def ready(self):
        """
        App will be ready afterward
        """
        from . import signals