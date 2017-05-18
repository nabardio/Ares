# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    """
    Game admin panel configuration
    """
    fieldsets = [
        (None, {
            'fields': ['name', 'description', 'code']
        }),
        ('Instructions and Rules', {
            'fields': ['instruction', 'rules']
        }),
    ]

    list_display = ('name',)

    search_fields = ('name', 'description')
