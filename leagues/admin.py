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
                ('registration_date_start', 'registration_date_end'),
                ('date_start', 'date_end')
            ]
        }),
        ('Robots', {
            'fields': [
                'robots',
            ]
        }),
    ]

    filter_horizontal = ('robots',)

    list_display = ('title', 'game', 'num_robots', 'registration_date_start',
                    'registration_date_end', 'date_start', 'date_end')

    list_filter = ('game', 'registration_date_start', 'registration_date_end',
                   'date_start', 'date_end')

    search_fields = ('title', 'description')
