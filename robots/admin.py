# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.Robot)
class RobotAdmin(admin.ModelAdmin):
    """
    Robot admin panel configuration
    """
    fieldsets = [
        (None, {
            'fields': ['name', 'user', 'code']
        }),
    ]

    list_display = ('name', 'user')

    list_filter = ('user',)

    search_fields = ('name', 'user')
