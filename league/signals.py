import os

from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from league.models import Team


@receiver(post_delete, sender=Team, dispatch_uid='league.signals.delete_code_after_team_delete')
def delete_code_after_team_delete(sender, instance, **kwargs):
    """
    This function cleans remaining file field after its related object is deleted from database.
    
        Notes:
            Signal is registered on post_delete to ensure file remains on disk
            in case deleting object from database fails.
              
    :param sender: 
    :param instance: 
    :param kwargs: 
    :return: 
    """
    instance.code.delete(save=False)


@receiver(post_save, sender=Team, dispatch_uid='league.signals.overwrite_code_after_team_change')
def overwrite_code_after_team_change(sender, instance, **kwargs):
    """
    This function overwrites code file if a new file is provided after model is saved in database.

        Notes:
            Signal is registered on post_save to ensure file gets updated
            only if database change is successful.

    :param sender: 
    :param instance: 
    :param kwargs: 
    :return: 
    """
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
