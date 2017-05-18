# -*- coding: utf-8 -*-
import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    """
    User Factory generates random users for tests
    """
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    email = factory.Sequence(lambda n: 'user-{0}@example.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', 'password')

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)


class RobotFactory(factory.django.DjangoModelFactory):
    """
    Robot Factory generates random robots for tests
    """
    user = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'robot-{0}'.format(n))
    code = factory.django.FileField(
        data=factory.Faker('binary', length=10485).generate(dict()),
        filename=factory.Faker('file_name', extension='py').generate(dict())
    )

    class Meta:
        model = 'robots.Robot'
