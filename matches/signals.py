# -*- coding: utf-8 -*-
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Match
from .tasks import run_match


@receiver(pre_save,
          sender=Match,
          dispatch_uid='matches.signals.check_scheduler')
def check_scheduler(sender, instance, **kwargs):
    """
    Check to see if it needs a rescheduling or not
    """
    if instance.pk and instance.has_schedule_changed():
        if instance.match_scheduler:
            instance.match_scheduler.revoke()
        instance.match_scheduler = run_match.apply_async(
            args=(instance.id,), eta=instance.datetime)


@receiver(post_save,
          sender=Match,
          dispatch_uid='matches.signals.create_scheduled_task')
def create_scheduled_task(sender, instance, **kwargs):
    """
    Create a scheduled task for the match to run
    """
    if not instance.match_scheduler:
        instance.match_scheduler = run_match.apply_async(
            args=(instance.id,), eta=instance.datetime)
        instance.save()
