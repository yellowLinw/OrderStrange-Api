#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_exceptions import AddExceptions
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.api import *
from common.jwt import jwt
from config import Config

DEFAULT_APP_NAME = 'ORDER'

DEFAULT_MODULES = [
    (dash, '/dash')
]

# flask_sqlalchemy plugin
db = SQLAlchemy()
# flask_migrate plugin
migrate = Migrate()

exception = AddExceptions()


def create_app(config=Config):
    app = Flask(DEFAULT_APP_NAME)

    setting_modules(app, DEFAULT_MODULES)

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    exception.init_app(app)

    return app


def setting_modules(app, modules):
    # 注册Blueprint模块
    for module, url_prefix in modules:
        app.register_blueprint(module, url_prefix=url_prefix)


from app.models import *
