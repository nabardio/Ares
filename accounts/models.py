# -*- coding: utf-8 -*-
from hashlib import md5

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    """
    Customized User model
    """
    avatar = models.URLField('avatar')

    username_validator = RegexValidator(
        regex=r'^[\w.+-]+$',
        message='Enter a valid username. This value may contain only letters, '
                'numbers, and ./+/-/_ characters.')

    def check_avatar(self):
        """
        Check if user doesn't have an avatar set the gravatar for it 
        """
        gravatar_url = 'https://gravatar.com/avatar/{}?s=500'
        self.avatar = self.avatar or gravatar_url.format(
            md5(self.email.encode()).hexdigest())

    def save(self, *args, **kwargs):
        self.check_avatar()
        super(User, self).save(*args, **kwargs)
