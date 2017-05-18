# -*- coding: utf-8 -*-
import os

import factory
from django.conf import settings
from django.core.files.base import ContentFile
from test_plus.test import TestCase

from . import factories


def get_full_path(media_relative_path):
    """
    Joins a relative path with the media path
    """
    return os.path.join(settings.MEDIA_ROOT, media_relative_path)


class TestModels(TestCase):
    user_factory = factories.UserFactory

    def test__delete_code_after_robot_delete(self):
        robot = factories.RobotFactory()
        code_file_path = get_full_path(robot.code.__str__())
        self.assertEqual(os.path.isfile(code_file_path), True)
        robot.delete()
        self.assertEqual(os.path.isfile(code_file_path), False)
