# -*- coding: utf-8 -*-
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Game


@receiver(post_delete,
          sender=Game,
          dispatch_uid='games.signals.delete_code_after_game_delete')
def delete_code_after_game_delete(sender, instance, **kwargs):
    """
    Cleans remaining file field after its related object is deleted.
    
        Notes:
            Signal is registered on post_delete to ensure file remains on disk
            in case deleting object from database fails.
    """
    instance.code.delete(save=False)
