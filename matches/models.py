# -*- coding: utf-8 -*-
from django.db import models


class Match(models.Model):
    """
    Match is fight between to robot
    """
    datetime = models.DateTimeField('date and time')
    finished = models.BooleanField('finished', default=False)
    game = models.ForeignKey('games.Game', related_name='matches')
    robot1 = models.ForeignKey('robots.Robot', related_name='matches1',
                               on_delete=models.CASCADE)
    robot2 = models.ForeignKey('robots.Robot', related_name='matches2',
                               on_delete=models.CASCADE)
    robot1_score = models.FloatField(default=0)
    robot2_score = models.FloatField(default=0)
    log = models.TextField(null=True)
    league = models.ForeignKey('leagues.League', related_name='matches',
                               blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} vs. {}'.format(self.robot1, self.robot2)
