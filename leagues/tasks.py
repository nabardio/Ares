# -*- coding: utf-8 -*-
import random

from celery import shared_task
from django.utils import timezone

from .models import League


@shared_task(name='leagues.tasks.schedule_matches')
def schedule_matches(league_id):
    """
    After the registration this task will schedule the matches 
    """
    league = League.objects.get(pk=league_id)
    if league.robots.count() == league.num_robots:
        robots = list(league.robots.all())
        random.shuffle(robots)

        # a period of time to schedule a set of matches in
        period = timezone.timedelta(1)
        # duration within a period to schedule the matches
        duration = timezone.timedelta(
            minutes=((league.match_end_time.hour -
                      league.match_start_time.hour) * 60) +
                    (league.match_end_time.minute -
                     league.match_start_time.minute))
        # interval between two matches within a same period
        interval = duration // (league.num_robots // 2)
        start_time = timezone.make_aware(
            timezone.datetime.combine(
                league.start, league.match_start_time))

        for turn in range(league.num_robots - 1):
            for i in range(league.num_robots // 2):
                time = start_time + (turn * period) + (i * interval)
                # Home match
                league.matches.create(
                    datetime=time,
                    game=league.game,
                    robot1=robots[i],
                    robot2=robots[league.num_robots - i - 1])
                # Away match
                time += (turn + league.num_robots - 1) * period
                league.matches.create(
                    datetime=time,
                    game=league.game,
                    robot1=robots[league.num_robots - i - 1],
                    robot2=robots[i])
            robots.insert(1, robots.pop())
