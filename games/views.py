# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView

from .models import Game


class GameList(ListView):
    """
    List of the games
    """
    model = Game
    template_name = 'games.html'
    context_object_name = 'games'


class GameDetail(DetailView):
    """
    Game detail view
    """
    model = Game
    template_name = 'game.html'
    context_object_name = 'game'
