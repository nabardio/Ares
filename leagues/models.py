# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


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

    def clean(self):
        """
        Validate the the values
        """
        today = timezone.localdate()
        if self.registration_date_start <= today:
            raise ValidationError(
                u'Registration starting date must be after today')

        if self.registration_date_end <= self.registration_date_start:
            raise ValidationError(
                u'Registration ending date must be after starting date')

        if self.date_start <= self.registration_date_end:
            raise ValidationError(
                u'League starting date must be after registration ending date')

        if self.date_end <= self.date_start:
            raise ValidationError(
                u'League ending date must be after its starting date')

    def __str__(self):
        return '{} ({})'.format(self.title, self.game)
