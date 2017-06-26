# -*- coding: utf-8 -*-
from celery.result import AsyncResult
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
    _match_scheduler_id = models.CharField('match scheduler id',
                                           max_length=36, null=True)

    def __init__(self, *args, **kwargs):
        super(Match, self).__init__(*args, **kwargs)
        self.__original_datetime = self.datetime

    @property
    def match_scheduler(self):
        """
        Match scheduler task
        """
        if self._match_scheduler_id:
            return AsyncResult(self._match_scheduler_id)
        return None

    @match_scheduler.setter
    def match_scheduler(self, scheduler):
        if isinstance(scheduler, AsyncResult):
            self._match_scheduler_id = scheduler.id

    @match_scheduler.deleter
    def match_scheduler(self):
        self._match_scheduler_id = None

    def has_schedule_changed(self):
        """
        Check if the league schedule has changed or not
        """
        return self.datetime != self.__original_datetime

    def __str__(self):
        return '{} vs. {}'.format(self.robot1, self.robot2)
