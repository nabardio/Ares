#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    manager
    ~~~~~~~

    This module provides some basic commands for managing the project via
    command line.

    :copyright: (c) 2016 by Mehdy Khoshnoody.
    :license: GPLv3, see LICENSE for more details.
"""
from flask.ext.script import Manager, prompt_bool

from ares.factory import create_app
from flask.ext.migrate import MigrateCommand
from ares.extensions import db

manager = Manager(create_pp)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

if __name__ == "__main__":
    manager.run()
