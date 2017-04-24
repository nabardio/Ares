from django.apps import AppConfig


class LeagueConfig(AppConfig):
    name = 'league'

    def ready(self):
        from league import signals
