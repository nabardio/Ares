# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models

from utils.storages import CustomStorage


def robot_code_dir(instance, filename):
    """
    Generates a path for uploaded code.
    Generating file names with this methods makes categorizing files easier
    and helps prevent file duplication problems.

    :param instance: the robot instance
    :param filename: the code filename
    :return: the path to writes the code file to
    """
    return 'codes/robots/{}'.format(filename)


class Robot(models.Model):
    """
    Robots are supposed to fight with their codes against other robots.
    """
    name = models.CharField(
        'name',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and '
                  './+/-/_ only.',
        validators=[RegexValidator(regex=r'^[\w\.\+\-]+$')],
        error_messages={
            'unique': 'A robot with that name already exists.',
        },
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='robots', on_delete=models.CASCADE)
    code = models.FileField(upload_to=robot_code_dir,
                            storage=CustomStorage(),
                            validators=[FileExtensionValidator(['py'])])

    def __str__(self):
        return self.name
