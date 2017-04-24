import os

from django.db import models
from django.conf import settings

from league.storages import OverwriteStorage


def user_directory_path(instance, filename):
    """
    Generated a unique name for user uploaded file based on username and league id.
    Generating file names with this methods makes categorizing files easier
    and helps prevent file duplication problems!
    
        Notes:
            Original file name provided by user will change to `code`!
    
    :param instance: 
    :param filename: 
    :return: 
    """
    return os.path.join(
        'codes',
        'league_{league_id}'.format(league_id=instance.league.id),
        'user_{user_id}'.format(user_id=instance.user.id),
        'code.{extension}'.format(extension=filename.split('.')[-1])
    )


class League(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    registration_date_start = models.DateTimeField('registration starting date')
    registration_date_end = models.DateTimeField('registration ending date')
    date_start = models.DateTimeField('starting date')
    date_end = models.DateTimeField('ending date')
    num_teams = models.PositiveSmallIntegerField('number of teams')

    def __str__(self):
        return '{title} ({num_teams})'.format(title=self.title, num_teams=self.num_teams)


class Team(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    code = models.FileField(upload_to=user_directory_path, storage=OverwriteStorage())

    def __str__(self):
        return self.user.username


class Game(models.Model):
    datetime = models.DateTimeField('date')
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    team1_score = models.FloatField()
    team2_score = models.FloatField()
