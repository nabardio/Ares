# -*- coding: utf-8 -*-
from django.db import models


class League(models.Model):
    """
    Leagues for robots
    """
    title = models.CharField(
        'title',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer.',
        error_messages={
            'unique': 'A league with that name already exists.',
        },
    )
    description = models.CharField(max_length=1000, blank=True, null=True)
    registration_date_start = models.DateField('registration starting date')
    registration_date_end = models.DateField('registration ending date')
    date_start = models.DateField('starting date')
    date_end = models.DateField('ending date')
    num_robots = models.PositiveSmallIntegerField('number of robots')
    game = models.ForeignKey('games.Game', related_name='leagues')
    robots = models.ManyToManyField('robots.Robot', blank=True,
                                    related_name='leagues')

    def __str__(self):
        return '{} ({})'.format(self.title, self.game)
