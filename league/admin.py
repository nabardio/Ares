from django.contrib import admin
from . import models

@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'description', 'num_teams']
        }),
        ('Date Information', {
            'fields': [
                'registration_date_start', 'registration_date_end',
                'date_start', 'date_end'
            ]
        }),
    ]

    list_display = ('title', 'num_teams', 'registration_date_start',
                    'registration_date_end', 'date_start', 'date_end')

    list_filter = ('registration_date_start', 'registration_date_end',
                   'date_start', 'date_end')

    search_fields = ('title', 'description')


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['league', 'user', 'code']
        }),
    ]

    list_display = ('user', 'league')

    list_filter = ('league', )

    search_fields = ('user', )
