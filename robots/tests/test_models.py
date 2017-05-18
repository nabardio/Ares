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

    def test__overwrite_code_after_robot_change(self):
        robot = factories.RobotFactory()
        old_code_file_path = get_full_path(robot.code.__str__())
        with open(old_code_file_path, 'rb') as old_file:
            old_code_file_content = old_file.read()
        robot.code.save(
            name=factory.Faker('file_name', extension='py').generate(dict()),
            content=ContentFile(factory.Faker('binary', length=10485).generate(
                dict()))
        )
        new_code_file_path = get_full_path(robot.code.__str__())
        with open(new_code_file_path, 'rb') as new_file:
            new_code_file_content = new_file.read()
        self.assertTrue(os.path.isfile(new_code_file_path), True)
        self.assertEqual(old_code_file_path, new_code_file_path)
        self.assertNotEqual(old_code_file_content, new_code_file_content)
