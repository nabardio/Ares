from hashlib import md5
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.URLField('avatar')

    def save(self, *args, **kwargs):
        self.avatar = 'https://www.gravatar.com/avatar/{}?s=500'.format(
            md5(self.email.encode()).hexdigest())
        super(User, self).save(*args, **kwargs)
