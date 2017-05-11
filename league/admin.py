from django.contrib import admin
from . import models


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'description', 'num_robots']
        }),
        ('Date Information', {
            'fields': [
                'registration_date_start', 'registration_date_end',
                'date_start', 'date_end'
            ]
        }),
    ]

    list_display = ('title', 'num_robots', 'registration_date_start',
                    'registration_date_end', 'date_start', 'date_end')

    list_filter = ('registration_date_start', 'registration_date_end',
                   'date_start', 'date_end')

    search_fields = ('title', 'description')


@admin.register(models.Robot)
class RobotAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['league', 'user', 'code']
        }),
    ]

    list_display = ('user', 'league')

    list_filter = ('league',)

    search_fields = ('user',)


@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['league', 'robot1', 'robot2']
        }),
    ]

    list_display = ('league', 'robot1', 'robot2', 'datetime')

    list_filter = ('league', 'robot1', 'robot2', 'datetime')

    search_fields = ('league', 'robot1', 'robot2')
