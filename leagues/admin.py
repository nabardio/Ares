# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    """
    League admin panel configuration
    """
    fieldsets = [
        (None, {
            'fields': ['title', 'description', 'game', 'num_robots']
        }),
        ('Date Information', {
            'fields': [
                ('registration_start', 'registration_end'),
                ('start',),
                ('match_start_time', 'match_end_time')
            ]
        }),
        ('Robots', {
            'fields': [
                'robots',
            ]
        }),
    ]

    filter_horizontal = ('robots',)

    list_display = ('title', 'game', 'num_robots', 'registration_start',
                    'registration_end', 'start')

    list_filter = ('game', 'registration_start', 'registration_end', 'start')

    search_fields = ('title', 'description')
