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
