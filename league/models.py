import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, pre_delete
from django.dispatch.dispatcher import receiver

def user_directory_path(instance, filename):
    return 'codes/league_{}/user_{}/{}'.format(instance.league.id,
                                               instance.user.id, filename)

class League(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    registration_date_start = models.DateTimeField('registration starting date')
    registration_date_end = models.DateTimeField('registration ending date')
    date_start = models.DateTimeField('starting date')
    date_end = models.DateTimeField('ending date')
    num_teams = models.PositiveSmallIntegerField('number of teams')

    def __str__(self):
        return '{} ({})'.format(self.title, self.num_teams)

class Team(models.Model):
    user = models.ForeignKey(User)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    code = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.user.username

class Game(models.Model):
    datetime = models.DateTimeField('date')
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team1 = models.ForeignKey(
        Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(
        Team, related_name='team2', on_delete=models.CASCADE)
    team1_score = models.FloatField()
    team2_score = models.FloatField()

# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.pre_delete, sender=Team)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    instance.code.delete(False)

@receiver(models.signals.pre_save, sender=Team)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Team.objects.get(pk=instance.pk).code
    except Team.DoesNotExist:
        return False

    new_file = instance.code
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
