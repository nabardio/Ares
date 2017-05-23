# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import League
from .tasks import schedule_matches


@receiver(post_save,
          sender=League,
          dispatch_uid='leagues.signals.create_scheduled_task')
def create_scheduled_task(sender, instance, **kwargs):
    """
    Create a scheduled task for the league to create and organize its 
    matches after it registration time ended
    """
    schedule_matches.apply_async(args=(instance.id,),
                                 eta=instance.registration_end)
