# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import League
from .tasks import schedule_matches


@receiver(pre_save,
          sender=League,
          dispatch_uid='leagues.signals.check_scheduler')
def check_scheduler(sender, instance, **kwargs):
    """
    Check to see if it needs a rescheduling or not
    """
    if instance.pk and instance.has_schedule_changed():
        if instance.match_scheduler:
            instance.match_scheduler.revoke()
        instance.match_scheduler = schedule_matches.apply_async(
            args=(instance.id,), eta=instance.registration_end)


@receiver(post_save,
          sender=League,
          dispatch_uid='leagues.signals.create_scheduled_task')
def create_scheduled_task(sender, instance, **kwargs):
    """
    Create a scheduled task for the league to create and organize its 
    matches after it registration time ended
    """
    if not instance.match_scheduler:
        instance.match_scheduler = schedule_matches.apply_async(
            args=(instance.id,), eta=instance.registration_end)
        instance.save()
