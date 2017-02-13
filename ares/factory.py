# -*- coding: utf-8 -*-
"""
    factory
    ~~~~~~~

    This module provides some functions to create and configure a flask app

    :copyright: (c) 2016 by Mehdy Khoshnoody.
    :license: GPLv3, see LICENSE for more details.
"""
import logging
import logging.handlers

from flask import Flask, g, request

from .extensions import db, redis, migrate
from .utils.logger import WebFilter


def create_app(config):
    """
        Creates a flask application and configure it's blueprints,
        extensions and etc.
    :return: a flask application
    """
    app = Flask("Ares")

    app.config.from_object(config)
    configure_logger(app)
    configure_extensions(app)
    register_blueprints(app)

    return app


def configure_logger(app):
    """
        Configures the logger and registers the logger handlers.
    :param app: the flask application
    """
    app.logger.addFilter(WebFilter())
    formatter = logging.Formatter(app.config['LOG_FORMAT'])

    if not app.debug:
        debug_file_handler = logging.handlers.TimedRotatingFileHandler(
            os.path.join(app.config['LOG_PATH'], 'debug.log'),
            when='D',
            backupCount=10)
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(formatter)
        app.logger.addHandler(debug_file_handler)

        error_file_handler = logging.handlers.TimedRotatingFileHandler(
            os.path.join(app.config['LOG_PATH'], 'error.log'),
            when='D',
            backupCount=10)
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(formatter)
        app.logger.addHandler(error_file_handler)


def register_blueprints(app):
    """
        Registers the blueprints on the application.
    :param app: the flask application
    """
    blueprints = app.config['INSTALLED_BLUEPRINTS']
    for blueprint_name in blueprints:
        try:
            bp = __import__(
                'ares.plugins.{0}'.format(blueprint_name),
                fromlist=[blueprint_name])
            app.register_blueprint(bp.controller)
        except ImportError:
            app.logger.warning("couldn't register {} blueprint".format(
                blueprint_name
            ))


def configure_extensions(app):
    """
        Registers the extensions on the application.
    :param app: the flask application
    """
    db.init_app(app)
    migrate.init_app(app)
    redis.init_app(app)
