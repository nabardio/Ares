# -*- coding: utf-8 -*-
"""
    extensions
    ~~~~~~~~~~

    This module contains flask extensions

    :copyright: (c) 2016 by Mehdy Khoshnoody.
    :license: GPLv3, see LICENSE for more details.
"""
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.redis import FlaskRedis


db = SQLAlchemy()
migrate = Migrate()
redis = FlaskRedis()