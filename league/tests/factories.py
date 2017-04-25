import pytz

from django.conf import settings

import factory
from factory.fuzzy import FuzzyInteger


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)


# TODO: Make datetime factories follow model logic (i.e date_end generate a date that is after date_start in calendar)
class LeagueFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'league-{0}'.format(n))
    description = factory.Faker('text', max_nb_chars=1000)
    registration_date_start = factory.Faker('date_time', tzinfo=pytz.timezone(settings.TIME_ZONE))
    registration_date_end = factory.Faker('date_time', tzinfo=pytz.timezone(settings.TIME_ZONE))
    date_start = factory.Faker('date_time', tzinfo=pytz.timezone(settings.TIME_ZONE))
    date_end = factory.Faker('date_time', tzinfo=pytz.timezone(settings.TIME_ZONE))
    num_teams = FuzzyInteger(0, 2)

    class Meta:
        model = 'league.League'


class TeamFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    league = factory.SubFactory(LeagueFactory)
    code = factory.django.FileField(
        data=factory.Faker('binary', length=10485).generate(dict()),
        filename=factory.Faker('file_name', extension='py').generate(dict())
    )

    class Meta:
        model = 'league.Team'
