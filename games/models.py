# -*- coding: utf-8 -*-
from django.db import models

from utils.storages import CustomStorage


def game_code_dir(instance, filename):
    """
    Generates a path for uploaded code.
    Generating file names with this methods makes categorizing files easier
    and helps prevent file duplication problems.

    :param instance: the game instance
    :param filename: the code filename
    :return: the path to writes the code file to
    """

    return 'codes/games/{}'.format(filename)


class Game(models.Model):
    """
    Games to apply the logic and rules to a match
    """
    name = models.CharField(
        'name',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer.',
        error_messages={
            'unique': 'A game with that name already exists.',
        },
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    instruction = models.TextField()
    rules = models.TextField()
    code = models.FileField(upload_to=game_code_dir, storage=CustomStorage())

    def __str__(self):
        return self.name
